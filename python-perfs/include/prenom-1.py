"""Generate french names."""

from itertools import count
from pathlib import Path
import argparse
from random import choice


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", help="Download from https://www.insee.fr/fr/statistiques/fichier/2540004/nat2021_csv.zip", type=Path)
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
    for i in count():
        ngram = text[i: i+length]
        if len(ngram) != length:
            break
        yield ngram


def main():
    args = parse_args()
    firstnames = parse_csv(args.csv.read_text())
    markov = {}
    for firstname in firstnames:
        for ngram in ngrams(firstname, length=4):
            if ngram[:-1] not in markov:
                markov[ngram[:-1]] = []
            markov[ngram[:-1]].append(ngram[-1])
    start = choice(list(markov.keys()))
    for i in range(10):
        try:
            start = start + choice(markov[start[-3:]])
        except KeyError:
            break
    print(start, end=' ')
    if start in firstnames:
        print("(not new)")
    else:
        print("(new)")

if __name__ == '__main__':
    main()
