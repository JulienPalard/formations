# Langage

## `id` et `is`

Notes:

- `is` : pour les singletons `None`, `True`, `False`.
- `id` : identifiant unique, l'adresse mémoire en CPython.
- `is` : proche de `id(left) == id(right)` mais attention au GC.


## Parenthèse sur les singletons

Notes:

Un module est un singleton.


## String interning

```python
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

## Les gestionnaires de contexte

```python
with open("/etc/hosts") as f:
    f.read()
```

Notes:

En initiation on apprend a les utiliser.
En avancé on apprend à en faire.


## Les gestionnaires de contexte

- ``__enter__``
- ``__exit__``


Notes:

Expliquer le protocole.


## Les gestionnaires de contexte

```python
class transaction:
    def __init__(self, db):
        self.db = db
    def __enter__(self):
        self.db.begin()
    def __exit__(self, type, value, tb):
        if type is None:
            self.db.commit()
        else:
            self.db.rollback()
```

Notes:

C'est un exemple de gestionnaire de contexte de transaction de base de donnée.

Astuce, `__enter__` peut renvoyer un tuple, qu'on peut décomposer à
droite du as, typiquement `ifile`, `ofile`.


## Les décorateurs

`@`

Notes:

En initiation on apprend a les utiliser.
En avancé on apprend à en faire.


Just for doctest:
```python
def clock(f=None, *args, **kwargs):
    return lambda *args: None
```

## Les décorateurs

```python
@clock
def fib(n):
    ...
```

équivaut à

```python
fib = clock(fib)
```

Notes:

Bien insister sur le fait que `@` est bien séparé de son
`dotted_name`, pas n'importe quelle expression.  sur le fait qu'on
peut les empiler (clarifier l'ordre).


## Les décorateurs

```python
@clock(deadline=10)
def fib(n):
    ...
```

équivaut à

```python
fib = clock(deadline=10)(fib)
```

Notes:

Rappeler que `()` n'est qu'un opérateur.


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

Leur faire implémenter @memoize qui prend en paramètre une limite.

En profiter pour parler de `global`, `nonlocal`, et des closures.


## Les décorateurs

Les utiliser pour leurs effets de bord.

Notes:

`@route("/")` par exemple.


## Les décorateurs

- `@staticmethod`
- `@classmethod`
- `@property`


## contextlib

- `@suppress`
- `@contextmanager`


## contextlib

Un décorateur peut-il être aussi un gestionnaire de contexte ?

Est-ce utile ? Pertinent ?

Notes:

Oui, par exemple Django `@atomic` et with `atomic:`, `contextlib.ContextDecorator`.

Parler des gestionnaires de contextes réutilisables, puis réentrants.


## The Walrus Operator

`:=`

Notes:

Démo REPL avec re.match, rappeler que les parenthèses sont souvent
obligatoires.


## Les listes en compréhension

```python
l = []
for i in range(5):
  if i % 2 == 0:
    for j in range(5):
      if j % 2 == 0:
        for k in range(5):
          if k % 2 == 0:
            if i + j + k == 4:
              l.append((i,j,k))
```

## Les listes en compréhension

```python
>>> [(i, j, k)
...  for i in range(5)
...  if i % 2 == 0
...  for j in range(5)
...  if j % 2 == 0
...  for k in range(5)
...  if k % 2 == 0
...  if i + j + k == 4]
[(0, 0, 4), (0, 2, 2), (0, 4, 0), (2, 0, 2), (2, 2, 0), (4, 0, 0)]
```

Notes:

Juste pour doctest:

```python
factors = lambda i: [i]
```

## Les listes en compréhension

```python
{x: factors(x)
 for x in range(1000)
 if len(factors(x)) == 3}
```

Notes: si factors est lent (spoiler: il l'est), c'est du gâchis.


## Les listes en compréhension

```python
{x: prime_factors
 for x in range(1000)
 if len(prime_factors := factors(x)) == 3}
```
