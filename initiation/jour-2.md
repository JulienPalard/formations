# Python

Jour 2

# Les chaînes

```python
>>> """Anne Elk's Theory est "mieux"."""
'Anne Elk\'s Theory est "mieux".'
```

## Les docstrings

```python
def une_fonction():
    """Une courte description."""
    ...
    return ...
```

# Les nombres

## Les opérateurs mathématiques

```python
>>> 0.1 + 0.1
0.2
```


## Les opérateurs mathématiques

```python
>>> 0.1 + 0.2
0.30000000000000004
```

::: notes

https://0.30000000000000004.com


# `for` et `while`

## `break` et `continue`

Break sert à interrompre une boucle, continue sert à passer à l'élément
suivant. Qu'on soit dans un `for` ou dans un `while`.


## `break`

```python
>>> sq, gues = 5, 2
>>> while True:
...     gues = (gues + sq / gues) / 2
...     error = abs(sq - gues * gues)
...     if error < 0.0001:
...         break
>>> gues
2.2360679779158037
```


## `continue`

```python-repl
>>> for i in range(5):
...     if i == 0:
...         continue
...     print(i)
1
2
3
4
```


## Les exceptions : `try`

```python
>>> try:
...     int("abc")
... except ValueError:
...     print("Raté")
Raté
```


# La notation en compréhension

C'est transformer ça :

```python
>>> accumulator = []
>>> for i in range(10):
...    accumulator.append(2 ** i)
>>> accumulator
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```



## La notation en compréhension

en :

```python
>>> [2 ** i for i in range(10)]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```


## La notation en compréhension

Ou :

```python
def phi(n):
    numbers = []
    for i in range(n):
        if math.gcd(i, n) == 1:
            numbers.append(i)
    return len(numbers)
```


## La notation en compréhension

en :

```python
def phi(n):
    return len(
        [
            i
            for i in range(n)
            if math.gcd(i, n) == i
        ]
    )

```

::: notes

Elle devrait s'écrire sur une seule ligne, mais, vidéoprojecteur...



# Les tranches

*slices* en anglais

Notes:
```python
seq = list("ABCDEF")
```


# Les *slices*



```python
>>> seq
['A', 'B', 'C', 'D', 'E', 'F']
>>> seq[0]
'A'
```


## Les *slices*

```python
>>> seq[0:3]
['A', 'B', 'C']
```


## Les *slices*

```python
>>> seq[3:6]
['D', 'E', 'F']
```


## Les *slices*

```python
>>> seq[:]
['A', 'B', 'C', 'D', 'E', 'F']
```


## Les *slices*

```python
>>> seq[1:]
['B', 'C', 'D', 'E', 'F']
```


## Les *slices*

```python
>>> seq[-1]
'F'
```


## Les *slices*

```python
>>> seq[:-2]
['A', 'B', 'C', 'D']
```


## Les *slices*

```python
>>> seq[0:5:2]
['A', 'C', 'E']
```


## Les *slices*

```python
>>> seq[::-1]
['F', 'E', 'D', 'C', 'B', 'A']
```


## Les *slices*

`seq[<start>:<stop>:<step>]`


# `*`, `**`


## `*`

Signifie « plusieurs », comme dans une liste ou un *n*-uplet.

```python
>>> begin, *rest = range(5)
>>> begin
0
>>> rest
[1, 2, 3, 4]
```

Notes:

Attention, initiation : Le but est de savoir que ça existe, savoire le
lire.

Équivaut à:
begin, rest = seq[0], seq[1:]




## `*`

```python
>>> def sum(*args):
...    print(args)
...
>>> sum(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)
```


## `*`

```python
>>> [0, 0, 0, *range(3)]
[0, 0, 0, 0, 1, 2]
```


## `*`

```python
>>> print(*range(5))
0 1 2 3 4
```


## `**`

Signifie « plusieurs, nommés », comme dans un dictionnaire.


```python
>>> def p(**kwargs):
...    for key, value in kwargs.items():
...        print(key, "→", value)
...
>>> p(x=10, y=12)
x → 10
y → 12
```


## `**`

```python
>>> defaults = {"path": "./",
...             "pattern": "*.txt"}
>>> {**defaults, "pattern": "*.md"}
{'path': './', 'pattern': '*.md'}
```


## `**`

```python
>>> def p(x, y):
...    print(f"x → {x}")
...    print(f"y → {y}")
...
>>> point = {"x": 10, "y": 12}
>>> p(**point)
x → 10
y → 12
```


# L'encodage


## encoder

C'est transformer une chaîne en octets, pour son transport ou stockage :

```python
>>> "L'été".encode()
b"L'\xc3\xa9t\xc3\xa9"
>>> list("L'été".encode())
[76, 39, 195, 169, 116, 195, 169]
```


## décoder

C'est le contraire ...

```python
>>> bytes([76, 39, 195, 169, 116, 195, 169]).decode()
"L'été"
```

Notes:

Parler d'unicode, d'UTF-8, de latin-1. Ne pas oubilier de mentionner
que latin-1 et companie sont à taille fixe, et qu'UTF-8 est à taille
variable.


# Les classes


## La syntaxe

```python
class LeNomDeLaClasse:
    """Sa docstring, comme pour une
    fonction.
    """
    # Le corps de la classe.
```

Notes:

Dédiaboliser l'héritage, l'héritage multiple, les interfaces,
les classes abstraites, les méthodes virtuelles, ...


## À retenir

On pourrait trier les données en deux types :

- celles dont on connaît les attributs → classes
- celles dont on ne connaît pas les attributs → dictionnaires


Notes:

Le contexte, le métier, les bibliothèques utilisées peuvent générer
des cas particuliers, cette règle n'est pas absolue.

préciser peut être : "dont on connaît à toutes les étapes du programme".



## Exemple

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Notes: On connaît les attributs.


## Exemple

```python
>>> ISIN = {
...   "GLE": "FR0000130809",
...   "PARRO": "FR0004038263",
...   "AM": "FR0000121725",
... }
```

Notes: On ne les connaît pas.


## Syntaxe → les méthodes

```python
class Dice:
    def throw(self):
        self.value = 4
        # Chosen by fair dice roll.
        # Guaranteed to be random.
```

Notes: Une classe *ne sert pas* à stocker des fonctions, mais des
données. Pensez aux structs C.

La données d'abord, l'algorithme après.


## Syntaxe → le constructeur

```python
class DiceCup:
    def __init__(self, dices):
        self.dices = dices

    def shake(self):
        ...
```

Notes: Leur faire faire implémenter le __repr__, min, max, et mean.

Leur faire faire 1000 tirages dans un Counter, avec des valeurs ENTIẼRES.


## Utilisation

```python
>>> dice = Dice()
>>> dice.throw()
>>> dice.value
4
```


## Utilisation

```python
>>> cup = DiceCup(
...    [Dice() for _ in range(10)]
... )
>>> cup.shake()
```

Notes:

Faire quelques exemples d'héritage simples avant de passer a la suite.

super() considered super() !


# pip, venvs, conda


## pip

C'est l'outil standard pour installer un paquet.

```bash
$ python3 -m pip install <package-name>
```

Mais, ça installe où ?


## venv

C'est l'outil standard pour indiquer où installer les paquets.

*On peut ainsi avoir plusieurs environnements, un par projet par exemple*.

Notes:

Pratique pour avoir des versions différentes.


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


## conda

```bash
$ conda create --name test
$ conda activate test
(test) $ conda install numpy
```


# Les bonnes pratiques

Notes: Prérequis: pip et venv.


## Bonnes habitudes

> There are 2 hard problems in computer science: cache invalidation,
> naming things, and off-by-1 errors.


## Bonnes habitudes

Pas plus de 7.


## Garder son code lisible

Attention au code vieillissant, au « je ne rajoute qu'une ligne ou
deux à cette fonction et c'est réglé ».

Notes: Deux ans après la fonction fait 800 lignes, et personne ne l'a
vu venir. flake8 peut aider.


## Garder son API évolutive

Utilisez correctement `/` et `*` dans les prototypes de fonction.

Notes:

help(sum)


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


## flake8

Dans un venv :

```bash
(test) $ pip install flake8
(test) $ pip install flake8-bugbear
(test) $ flake8 --max-complexity 9 *.py
```

Notes:

Flake8 est rapide, n'effectuant pas les `imports` il ne peut repérer
qu'une catégorie de problèmes.

9 est trop bas, 15 est probablement un bon choix.


## pylint

```bash
(test) $ pip install pylint
(test) $ pylint is_prime.py
```


## mypy

`mypy` fonctionne avec des annotations de types.

```bash
(test) $ pip install mypy
(test) $ mypy is_prime.py
```

Notes: --ignore-missing-imports


## bandit

Bandit cherche les failles de sécurité...

```bash
(test) $ pip install bandit
(test) $ bandit is_prime.py
```


## tox

Permet de lancer les tests:
- sur plusieurs interpréteurs (s'ils sont installés),
- de plusieurs outils,
- en parallèle.

Notes: c.f. gh/JulienPalard/oeis.
