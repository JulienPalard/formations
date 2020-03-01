# Le packaging

## Petite parenthèse

La différence entre un paquet et un module ?

Notes:

Pour Python il n'y en a pas, tout est module, pour nous, un paquet est
un dossier.  Aborder rapidement les paquets-espace-de-noms.


## Digression

`__main__` et `__main__.py`.


## venv

Notes:

Et ses alternatives : virtualenv / conda.


## pip

Notes:

Jamais `sudo`, toujours dans un `venv`.


## pip install -e .

Notes:

Probablement celui qu'on utilise le plus souvent.


## Packager

- Source dist
- Binary dist


# La suite


- Packaging
 - cookiecutter : docs/, tests/, README, setup.cfg, setup.py, ...

- List comprehension avancé
  - Double for, double if, walrus

- Multiprocessing / Multithreading / Asyncio
 - IO Bound vs CPU Bound
 - Locks vs Queues

- Code quality
- import this, explicit is better
 - sémantique : les ternaires, les listes en intension, sont des
   expressions, elles doivent être utilisées comme des expressions,
   pas comme des instructions.
 - TDD
 - pas de print, logging FTW.
 - pas de "logging tiers", personne ne connaît, on reste sur `logging`.
 - -Xdev
 - black, ..., pass
 - pytest, doctest
 - pytest-cov
 - hypothesis
 - flake8
 - flake8-bugbear
 - tox
 - mypy
 - black
 - pdb, breakpoint()
 - EAFP, LBYL

- Performance
 - Les types natifs : Leur complexité algorithmique
 - Cython
 - pypy
 - cffi
 - cprofile / pstats

- Libs
 - re
 - argparse
 - pathlib
 - logging
 - numpy
 - jupyter
