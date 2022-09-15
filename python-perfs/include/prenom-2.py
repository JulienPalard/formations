"""Generate french names."""

from itertools import count
from pathlib import Path
import pickle
import argparse
from collections import defaultdict
from random import choice


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    subparser = parser.add_subparsers()
    parse = subparser.add_parser("parse")
    parse.add_argument("csv", help="Download from https://www.insee.fr/fr/statistiques/fichier/2540004/nat2021_csv.zip", type=Path)
    parse.set_defaults(func=main_parse)
    gen = subparser.add_parser("gen")
    gen.set_defaults(func=main_gen)
    return parser.parse_args()


def parse_csv(firstnames_csv):
    firstnames = []
    for lineno, line in enumerate(firstnames_csv.splitlines()):
        if lineno == 0:
            continue
        if line.split(";")[1][0] != "_":
            firstnames.append(line.split(";")[1].lower())
    return firstnames


def ngrams(text, length=3):
    for i in range(0, len(text) - length + 1):
        ngram = text[i: i+length]
        yield ngram


def main():
    args = parse_args()
    args.func(args)


def main_parse(args):
    firstnames = parse_csv(args.csv.read_text())
    markov = defaultdict(list)
    for firstname in firstnames:
        for ngram in ngrams(firstname, length=4):
            markov[ngram[:-1]].append(ngram[-1])
    with open("prenom.pickle", "wb") as prenom_pickle:
        pickle.dump((dict(markov), set(firstnames)), prenom_pickle)


def main_gen(args):
    with open("prenom.pickle", "rb") as prenom_pickle:
        markov, firstnames = pickle.load(prenom_pickle)
    start = choice(list(markov.keys()))
    for _ in range(10):
        try:
            start = start + choice(markov[start[-3:]])
        except KeyError:
            break
    print(start.capitalize(), end=' ')
    if start in firstnames:
        print("(not new)")
    else:
        print("(new)")

if __name__ == '__main__':
    main()
