# Les tranches

*slices* en anglais

Notes:
```python
seq = list("ABCDEF")
```

----

# Les *slices*



```python
>>> seq
['A', 'B', 'C', 'D', 'E', 'F']
>>> seq[0]
'A'
```

----

# Les *slices*

```python
>>> seq[0:3]
['A', 'B', 'C']
```

----

# Les *slices*

```python
>>> seq[3:6]
['D', 'E', 'F']
```

----

# Les *slices*

```python
>>> seq[:]
['A', 'B', 'C', 'D', 'E', 'F']
```

----

# Les *slices*

```python
>>> seq[1:]
['B', 'C', 'D', 'E', 'F']
```

----

# Les *slices*

```python
>>> seq[-1]
'F'
```

----

# Les *slices*

```python
>>> seq[:-2]
['A', 'B', 'C', 'D']
```

----

# Les *slices*

```python
>>> seq[0:5:2]
['A', 'C', 'E']
```

----

# Les *slices*

```python
>>> seq[::-1]
['F', 'E', 'D', 'C', 'B', 'A']
```

----

# Les *slices*

`seq[<start>:<stop>:<step>]`

---

# `*`, `**`

----

## `*` pour aggréger

```python
>>> begin, *rest = range(5)
>>> begin
0
>>> rest
[1, 2, 3, 4]
```

Notes:
Équivaut à:
begin, rest = seq[0], seq[1:]

----

## `*` pour aggréger

```python
>>> def sum(*args):
...    print(args)
...
>>> sum(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)
```

----

## `*` pour déconstruire

```python
>>> [0, 0, 0, *range(3)]
[0, 0, 0, 0, 1, 2]
```

----

## `*` pour déconstruire

```python
>>> print(*range(5))
0 1 2 3 4
```

----

## `**` pour aggréger

```python
>>> def p(**kwargs):
...    for key, value in kwargs.items():
...        print(key, "→", value)
...
>>> p(x=10, y=12)
x → 10
y → 12
```

----

## `**` pour déconstruire

```python
>>> defaults = {"path": "./",
...             "pattern": "*.txt"}
>>> {**defaults, "pattern": "*.md"}
{'path': './', 'pattern': '*.md'}
```

----

## `**` pour déconstruire

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

---

# L'encodage

----

# encoder

C'est transformer une chaîne en octets, pour son transport ou stockage :

```python
>>> "L'été".encode()
b"L'\xc3\xa9t\xc3\xa9"
>>> list("L'été".encode())
[76, 39, 195, 169, 116, 195, 169]
```

----

# décoder

C'est le contraire ...

```python
>>> bytes([76, 39, 195, 169, 116, 195, 169]).decode()
"L'été"
```

Notes:

Parler d'unicode, d'UTF-8, de latin-1. Ne pas oubilier de mentionner
que latin-1 et companie sont à taille fixe, et qu'UTF-8 est à taille
variable.

---

# Les classes

----

## La syntaxe

```python
class LeNomDeLaClasse:
    """Sa docstring, comme pour une
    fonction.
    """
    # Le corps de la classe.
```

Notes:

Dédramatiser l'héritage, l'héritage multiple, les interfaces,
les abstraites, les virtuelles, ...

----

## À retenir

On pourrait trier les données en deux types :

- celles dont on connaît¹ les attributs → classes
- celles dont on ne connaît pas les attributs → dictionnaires

1) à toutes les étapes du programme.


----

## Exemple

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Notes: On connaît les attributs.

----

## Exemple

```python
>>> headers = {"X-Csrf-Tok": "i8XNjC4"}
```

Notes: On ne les connaît pas.

----

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

----

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

----

## Utilisation

```python
>>> dice = Dice()
>>> dice.throw()
>>> dice.value
4
```

----

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

---

# pip, venvs, conda

----

## pip

C'est l'outil standard pour installer un paquet.

```bash
$ python3 -m pip install <package-name>
```

Mais, ça installe où ?

----

## venv

C'est l'outil standard pour indiquer où installer les paquets.

*On peut ainsi avoir plusieurs environnements, un par projet par exemple*.

Notes:

Pratique pour avoir des versions différentes.

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

----

## conda

```bash
$ conda create --name test
$ conda activate test
(test) $ conda install numpy
```

---

# Les bonnes pratiques

Notes: Prérequis: pip et venv.

----

## Bonnes habitudes

> There are 2 hard problems in computer science: cache invalidation,
> naming things, and off-by-1 errors.

----

## Bonnes habitudes

Pas plus de 7.

----

## Garder son code lisible

Attention au code vieillissant, au « je ne rajoute qu'une ligne ou
deux à cette fonction et c'est réglé ».

Notes: Deux ans après la fonction fait 800 lignes, et personne ne l'a
vu venir. flake8 peut aider.

----

## Garder son API évolutive

Utilisez correctement `/` et `*` dans les prototypes de fonction.

Notes:

help(sum)

----

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
(test) $ pip install flake8
(test) $ pip install flake8-bugbear
(test) $ flake8 --max-complexity 9 *.py
```

Notes:

Flake8 est rapide, n'effectuant pas les `imports` il ne peut repérer
qu'une catégorie de problèmes.

9 est trop bas, 15 est probablement un bon choix.

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
(test) $ mypy is_prime.py
```

Notes: --ignore-missing-imports

----

## bandit

Bandit cherche les failles de sécurité...

```bash
(test) $ pip install bandit
(test) $ bandit is_prime.py
```

----

## tox

Permet de lancer les tests:
- sur plusieurs interpréteurs (s'ils sont installés),
- de plusieurs outils,
- en parallèle.

Notes: c.f. gh/JulienPalard/oeis.

---

# Le packaging

----

## Le packaging

Restez dans les standards : `setup.py`, `setup.cfg`.

----

## setup.py

```
__import__('setuptools').setup()
```

## setup.cfg

- https://github.com/JulienPalard/teacher
- https://setuptools.readthedocs.io/

----

## pip

```bash
(test) $ pip install -e .
```

----

## pytest

```bash
(test) $ mkdir tests/
(test) $ pip install pytest
(test) $ editor tests/test_dice.py
```

Notes: C'est l'occasion de parler de assert.

----

## hypothesis

```
@given(integers(min_value=2,
                max_value=1000))
def test_fib(i):
    assert fib(i) == fib(i-1) + fib(i-2)
```

----

## pdb

----

## PYTHONDEVMODE=y

Et `./configure --with-pydebug`.

Notes: Voir mon bashrc :] Surtout "viable" depuis la 3.8.


---

# Les modules utiles

- argparse
- re
- csv (quand on a pas Pandas)
- subprocess

---

# La communauté

> Come for the language, stay for the community

— Brett Cannon


----

## Les PyCons

La PyConFr ! Les meetups locaux.
