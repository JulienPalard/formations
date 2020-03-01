# Python Introduction Slides

https://mdk.fr/python-initiation/


## TODO

- Les imports
- Attention avec `def fib` jour 1 on montre les fonctions avant de les
  avoir expliquées.
- with statement


## Notes

**Aucune** fonction n'est montée avant le 3, (à part des méthodes sur
les types natifs).

Souci : Jour 1 pytest nécessite Jour 2 pip...


# La suite du programme avancé


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
