#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
from math import *
from pprint import pprint


class stock:
    """ Object permettant de manipuler un etat """

    def __init__(self, etat, maximum=20):
        self.etat = etat
        self.maximum = maximum

    def charge(self, charge):
        """ incremente l'etat """

        self.etat += charge
        self.etat = min(self.etat, self.maximum)

    def decharge(self, decharge):
        """ decrement l'etat """

        self.etat -= decharge
        self.etat = max(self.etat, 0)

    def force_etat(self, etat):
        """ definit l'etat a une valeur forcée """

        self.etat = etat
        return self.etat


class hydrogen(stock):
    """ Objet heritant des proprietées de stock """

    """ avec notion de rendement                """

    def __init__(self, etat, rendement):
        stock.__init__(self, etat, 140)
        self.rendement = rendement

    def calcul_charge(self, charge):
        """ Retourne decharge en vue du rendement """

        return floor(charge / self.rendement)

    def calcul_decharge(self, decharge):
        """ Retourne decharge en vue du rendement """

        return decharge * self.rendement


class energie:
    """ Objet pour connaitre la production des sources """

    def __init__(self, sources):
        self.sources = sources

    def production(self, source, heure):
        """ Retourne la production d'une """
        """ source pour une heure donnée """
        return self.sources[source].get(heure, 0)


class implications:
    """ Generateur d'implicaitons """

    def __init__(self, sources, destinations):
        self.sources = sources
        self.destinations = destinations

    def combinations(self, L):
        """ Retourne la combinaison de deux listes """

        for i in range(0, len(L) + 1):
            for combination in itertools.combinations(L, i):

                yield combination

    def connections(self):
        """ Retourne les connections simultanées """
        """ possiblibles vers les destinations   """

        choosed = []
        generated = []
        possibles = self.possibles()

        while possibles:
            choosed, generated, possibles = self.gen_connection(
                possibles, choosed, generated
            )

        return generated

    def gen_connection(self, possibles, choosed=[], generated=[]):

        choice = possibles.pop(0)
        choosed += choice

        for possible in possibles:
            if not choice[0] in possible[0]:

                if len(choice[1]) == 0:
                    generated += [(choice, possible)]
                else:
                    if not self.is_used(choice[1], possible[1]):
                        generated += [(choice, possible)]

        return choosed, generated, possibles

    def connections_list(self):
        """ genere une liste de dictionaires de connections possibles """

        connections = []
        for connection in self.connections():
            implications = {}
            for destination_tuple in connection:
                destination, elements = destination_tuple
                if len(elements) != 0:
                    implications.update({destination: list(elements)})
            connections += [implications]

        return connections

    def possibles(self):
        """ Retourne les combinaisons possibles entre sources """
        """ et destinations (une source ne peut pas etre sa   """
        """ propre destination)                               """

        combinations = list(self.combinations(self.sources))

        possibles = []

        for destination in self.destinations:
            for elements in combinations:
                if not destination in elements:

                    possibles += [(destination, elements)]

        return possibles

    def is_used(self, choice, possible):
        used = False

        for element in choice:
            if element in possible:
                used = True

        return used


class partie:
    def __init__(self, temps, connections_list, batterie, hydrogen, sources):
        self.gagne = False
        self.temps = temps
        self.connections_list = connections_list
        self.batterie = batterie
        self.hydrogen = hydrogen
        self.productions = energie(sources)
        self.solutions = {}

    def demarre(self):
        print("Etat batterie initial: {}".format(self.batterie.etat))
        print("Etat hydrogen initial: {}".format(self.hydrogen.etat))

        i = 0
        for heure in range(1, self.temps + 1):
            nouvelles_solutions = {}
            for connections in self.connections_list:

                if not self.solutions:
                    etat_suivant = self.etats_suivant(heure, connections)
                    nouvelles_solutions.update({i: etat_suivant})
                    i += 1

                else:
                    for sid, solution in self.solutions.items():
                        for heure_solution, infos_solution in solution.items():
                            if heure_solution == heure - 1:
                                etat_suivant = self.etats_suivant(heure, connections)
                                etat_suivant.update(solution)
                                nouvelles_solutions.update({i: etat_suivant})
                                i += 1

            choix = self.choix_solution(heure, nouvelles_solutions)
            self.solutions.update(choix)
            # print('choix:', choix)
            print()

    def etats_suivant(self, heure, connections):
        self.change_etats(heure, connections)
        self.pause()

        etat = {
            heure: {
                "etat": {
                    "batterie": self.batterie.etat,
                    "hydrogen": self.hydrogen.etat,
                    "partie_gagnante": self.gagne,
                },
                "connections": connections,
            }
        }
        self.gagne = False

        return etat

    def choix_solution(self, heure, new_solutions):
        solutions = {}

        #  On recupere la valeur max de l'etat de batterie
        etats_batterie = []
        for sid, s in new_solutions.items():
            for h, infos in s.items():
                if h == heure:
                    etats_batterie.append(infos["etat"]["batterie"])

        max_batterie = max(etats_batterie)

        solutions_max_batterie = {}
        for sid, s in new_solutions.items():
            for h, infos in s.items():
                if infos["etat"]["batterie"] == max_batterie:
                    solutions_max_batterie.update({sid: s})
        print(len(solutions_max_batterie))

        #  On recupere la valeur max de l'etat de lh'hydrogen
        etats_hydrogen = []
        for sid, s in new_solutions.items():
            for h, infos in s.items():
                if h == heure:
                    etats_hydrogen.append(infos["etat"]["hydrogen"])

        max_hydrogen = max(etats_hydrogen)

        solutions_max_hydrogen = {}
        for sid, s in new_solutions.items():
            for h, infos in s.items():
                if infos["etat"]["hydrogen"] == max_hydrogen:
                    solutions_max_hydrogen.update({sid: s})
        print(len(solutions_max_hydrogen))

        print("Max batterie:", max_batterie)
        print("Max hygrogen:", max_hydrogen)

        # on ne garde, que la premiere solution trouvée avec l'etat de bantterie max
        choix = {}
        for sid, s in new_solutions.items():
            for h, infos in s.items():
                etat_batterie = infos["etat"]["batterie"]
                etat_hydrogen = infos["etat"]["hydrogen"]

                if not choix:
                    if h == heure and etat_batterie == max_batterie:
                        choix.update({sid: s})

        solutions.update(choix)

        return solutions

    def changements(self, heure, connexions):
        charge_batterie = 0
        charge_hydrogen = 0
        decharge_hydrogen = 0
        decharge_batterie = 5

        for destination, sources in connexions.items():
            for source in sources:

                production = self.productions.production(source, heure)
                if production:
                    if destination == "batterie":
                        charge_batterie += production

                        if source == "hydrogen":
                            decharge_hydrogen = self.hydrogen.calcul_decharge(
                                production
                            )

                    elif destination == "hydrogen":
                        charge_hydrogen += self.hydrogen.calcul_charge(production)

        return {
            "charge": {"batterie": charge_batterie, "hydrogen": charge_hydrogen},
            "decharge": {"batterie": decharge_batterie, "hydrogen": decharge_hydrogen},
        }

    def change_etats(self, heure, connexions):
        changements = self.changements(heure, connexions)

        if changements["charge"]["batterie"] != 0:
            self.batterie.charge(changements["charge"]["batterie"])

        if changements["charge"]["hydrogen"] != 0:
            self.hydrogen.charge(changements["charge"]["hydrogen"])

        if changements["decharge"]["hydrogen"] != 0:
            self.hydrogen.decharge(changements["decharge"]["hydrogen"])

        if changements["decharge"]["batterie"] != 0:
            self.batterie.decharge(changements["decharge"]["batterie"])

    def pause(self):
        if self.batterie.etat > 0:
            self.gagne = True


if __name__ == "__main__":

    sources = {
        "eolienne": {
            1: 5,
            2: 2,
            3: 1,
            4: 0,
            5: 3,
            6: 4,
            7: 3,
            8: 0,
            9: 2,
            10: 1,
            11: 6,
            12: 5,
            13: 4,
            14: 4,
            15: 6,
            16: 2,
            17: 0,
            18: 0,
            19: 2,
            20: 3,
            21: 2,
            22: 0,
            23: 1,
            24: 3,
            25: 4,
            26: 6,
            27: 1,
            28: 2,
            29: 3,
            30: 4,
            31: 6,
            32: 4,
            33: 0,
            34: 1,
            35: 0,
            36: 0,
            37: 3,
            38: 2,
            39: 0,
            40: 0,
            41: 3,
            42: 1,
            43: 0,
            44: 3,
            45: 4,
            46: 3,
            47: 1,
            48: 0,
            49: 0,
        },
        "solaire": {
            7: 2,
            8: 5,
            9: 10,
            10: 7,
            11: 8,
            12: 11,
            13: 6,
            14: 6,
            15: 13,
            16: 10,
            17: 7,
            18: 9,
            19: 8,
            20: 3,
            31: 3,
            32: 6,
            33: 8,
            34: 10,
            35: 14,
            36: 9,
            37: 8,
            38: 6,
            39: 11,
            40: 9,
            41: 5,
            42: 8,
            43: 7,
            44: 3,
        },
        "hydrogen": {
            1: 4,
            2: 4,
            2: 4,
            4: 4,
            5: 4,
            6: 4,
            7: 4,
            8: 4,
            9: 4,
            10: 4,
            11: 4,
            12: 4,
            13: 4,
            14: 4,
            15: 4,
            16: 4,
            17: 4,
            18: 4,
            19: 4,
            20: 4,
            21: 4,
            22: 4,
            23: 4,
            24: 4,
            25: 4,
            26: 4,
            27: 4,
            28: 4,
            29: 4,
            30: 4,
            31: 4,
            32: 4,
            33: 4,
            34: 4,
            35: 4,
            36: 4,
            37: 4,
            38: 4,
            39: 4,
            40: 4,
            41: 4,
            42: 4,
            43: 4,
            44: 4,
            45: 4,
            46: 4,
            47: 4,
            48: 4,
        },
    }

    destinations = ["hydrogen", "batterie"]
    g = implications(sources=sources, destinations=destinations)

    temps = 48

    stock_batterie = stock(20)
    stock_hydrogen = hydrogen(40, 2)

    p = partie(temps, g.connections_list(), stock_batterie, stock_hydrogen, sources)

    p.demarre()

    for sid, solution in p.solutions.items():
        if len(solution) == temps:
            pprint(solution)
