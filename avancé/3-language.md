# Langage

## `id` et `is`

Notes:

- `is` pour les singletsons `None`, `True`, `False`.
- `id` : identifiant unique, l'adresse mémoire en CPython.
- `is` sémantiquement est donc `id(left) == id(right)` mais attention au GC.


## Parenthèse sur les singletons

Notes:

Un module est un singleton.


## String interning

```python3
a = "Bonjour !"
b = "Bonjour !"
a is b
```

?

Notes:

- C'est dépendant de l'implémentation, ça change d'une version à l'autre de Python.
- Les chaînes ne contenant que des [a-zA-Z0-9_] sont internées.


## IEEE 754

```python
f"http://{.1 + .2}.com"
```

Notes:

Notez ! Et au besoin utilisez le module Decimal.


## Définir vos propres exceptions

Il suffit d'hériter d'`Exception`, rien de plus.

```
>>> class DBError(Exception): pass
...
>>> raise DBError("No such entry")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.DBError: No such entry
```

Notes:

library/exceptions.html → hierarchy


## try, finally, else, except

Dans quel ordre ?

Notes: Oui, il y a un else ici aussi.


## try, except, else, finally

## Les décorateurs

```python
with open("/etc/hosts") as f:
    f.read()
```

Notes:

En initiation on apprend a les utiliser.
En avancé on apprend à en faire.

## Les décorateurs

Faire ses propres décorateurs.

Notes:

Leur faire implémenter un décorateur @clock.
```python
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() -t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f"[{elapsed:.08f}s] {name}({arg_str}) -> {result!r}")
        return result
    return clocked
```


## Les décorateurs

Faire ses décorateurs paramétrés.

Notes:

Leur faire implémenter @memoize qui prend paramètre une limite.

En profiter pour parler de `global`, `nonlocal`, et des closures.


## Les décorateurs

Les utiliser pour leurs effets de bord.

Notes:

`@route("/")` par exemple.


# La suite


- Langage, syntaxe, datamodel
  - Les décorateurs, les décorateurs paramétrés
    - global, nonlocal
    - closures
    - @property
  - Les gestionnaires de contexte, montrer `with ... as (a, b):`
  - Datamodel / Special method names (depends on classes) : en parler
    en abordant les différents sujets.

- L'encodage
 - Unicode, UTF-8
 - str, bytes

- Packaging
 - pip install -e .
 - Rappel sur la distinction module / package, venv / pip
 - setuptools, wheel, sdist, bidst_wheel
 - __main__
 - cookiecutter : docs/, tests/, README, setup.cfg, setup.py, ...

- List comprehension avancé
  - Double for, double if, walrus

- Multiprocessing / Multithreading / Asyncio
 - IO Bound vs CPU Bound
 - Locks vs Queues

- Code quality
- import this, explicit is better
 - TDD
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
