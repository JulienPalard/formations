
---

# pip, conda, et venvs

---

## pip

C'est l'outil standard pour installer un paquet.

```bash
$ python3 -m pip install <package-name>
```

Mais, ça installe où ?

----

## venv

C'est l'outil standard pour indiquer où installer les paquets, et donc
où ils sont.

*On peut ainsi avoir plusieurs environnements, un par projet par exemple*.

----

## venv

```bash
$ python3 -m venv --prompt test .venv/
$ source .venv/bin/activate
(test) $ python3 -m pip install pytest
```

Notes: Dépendant du shell, les envoyer sur library/venv.html.
Insister sur le côté "trashable du venv" :
- Ne rien mettre dans .venv
- rm -fr .venv  # au moindre souci

---

# Conda

The Anaconda package manager.

----

## conda

`conda` peut créer ses propres environnements :

```bash
$ conda create --name test
$ conda activate test
(test) $ conda install numpy
```

---

# Les bonnes pratiques

Notes: Prérequis: pip et venv.

---

## Les « linters »

Il existe plusieurs outils pour « relire » votre code :
- flake8,
- pylint,
- mypy,
- black,
- bandit,
- isort.

Et un pour les unifier tous : `tox`.

Notes: Leur faire implémenter un `is_prime(x)` pour jouer avec.

La règle des 7.

----

## flake8

Dans un venv :

```bash
(test) $ pip install flake8 flake8-bugbear
(test) $ flake8 --max-complexity 15 is_prime.py
```

Notes:

Flake8 est rapide, n'effectuant pas les `imports` il ne peut repérer
qu'une catégorie de problèmes.

----

## pylint

```bash
(test) $ pip install pylint
(test) $ pylint is_prime.py
```

----

## mypy

`mypy` fonctionne avec des annotations de types.

```bash
(test) $ pip install mypy
(test) $ mypy --ignore-missing-imports is_prime.py
```

----

## bandit

Bandit cherche les failles de sécurité...

```bash
(test) $ pip install bandit
(test) $ bandit is_prime.py
```


----

## isort

`isort` vérifie la propreté des imports

---

# Les classes en Python

----

## La syntaxe

```python
class TheClassName:
    """The class documentation
    """
    # the class body
```

----

## À retenir

Les données d'abord le code après.


----

## À retenir

On pourrait classer les données en deux types :

- celles dont on connaît les attributs → classes
- celles dont on ne connaît pas les attributs → dictionnaires


----

## Exemple

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

----

## Exemple

```python
>>> headers = {"X-Csrf-Token": "i8XNjC4"}
```
