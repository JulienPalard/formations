# Python Introduction Slides

https://mdk.fr/python-initiation/


## TODO

- http://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial
- `*` peut être vu comme de l'unpacking vers des noms qu'on ne voit pas.
- Ajouter une slide sur "jamais de \ en fin de ligne", il y a toujours
  un moyen plus lisible.
- https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html Why numbering should start at zero
- Les imports
- Attention avec `def fib` jour 1 on montre les fonctions avant de les
  avoir expliquées.
- with statement


## Notes

Les arguments par defaut conservés peuvent service de memoizer:

    def fib(x, memo={}):
        ...

**Aucune** fonction n'est montée avant le 3, (à part des méthodes sur
les types natifs).

Souci : Jour 1 pytest nécessite Jour 2 pip...


# La suite du programme avancé


- Packaging
 - cookiecutter : docs/, tests/, README, setup.cfg, setup.py, ...

- Multiprocessing / Multithreading / Asyncio
 - IO Bound vs CPU Bound
 - Locks vs Queues

- Code quality
- import this, explicit is better
 - sémantique : les ternaires, les listes en compréhension, sont des
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
