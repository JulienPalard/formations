# Python 3.8
<tt>en ~38 minutes</tt>

par

Julien Palard <julien@palard.fr>

Notes: Introduce yourself!

Ça couvre les types de bases survol quelques stricutres de contrôle,
et quelques fonctions natives.

----

## Python : Introduction

Python est un langage de programmation permettant de s'exprimer de
manière **concise** et **lisible**.

----

## Qui utilise Python ?

YouTube, Dropbox, Reddit, Instagram, Spotify, NASA…

![](static/Black-hole-M87.jpg)

----

## Combien utilisent Python ?

![](static/Evolution_of_Python.png)

----

## Installation

https://python.org

— ou —

![](static/Anaconda_Logo.png)


Notes:
- On windows use the WSL, or gitforwindows.org if you can't
- https://docs.python.org/3/using/windows.html
- https://docs.python.org/3/using/mac.html
- On windows, don't install from the Microsoft Store.

----

## Démarrer un interpréteur

Sur Windows :

```text
py
```

Sur tous les autres OS :

```text
python3
```

Notes:
- Définir « Interpréteur »
- `py` sur Windows trouve l'interpréteur le plus récent.

----

## L'interpréteur

Parfois appelé le *REPL* ou *la console interactive*.

```bash
$ python3
>>> 10800 / 60 / 60
3.0
>>>
```

Notes:

Permet d'essayer un peu de Python sans pour autant ouvrir un fichier.

Et oui, même après 10 ans de Python, on l'utilise encore.

Expliquer les parties "R", "E", "P", "L".

----

## L'interpréteur

Il en existe plusieurs : Celui natif à Python, IDLE, IPython, …

Il ressemble généralement soit à ça :

```bash
>>>
```
soit à ça :
```bash
In [1]:
```

----

## Testons l'interpréteur

```python
>>> 10
10
```
Notes:

L'interpréteur à lu les caractères `1` `0`, a compris que c'était un
nombre entier, l'a stocké dans sa représentation interne, un objet,
puis nous l'a représenté à son tour avec deux caractères `1` et `0`
pour qu'on puisse le lire.

----

## C'est votre nouvelle calculatrice

```python
>>> 60 * 60 * 4
14400
```

----

## Les exceptions

```python
>>> 5 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Notes:
Lisez *TOUJOURS* la dernière ligne en premier !

---

# Types natifs

Les types natifs, leurs opérateurs et leurs méthodes, les variables.

----

## Booléens

```python
>>> True
True
>>> False
False
```

----

## Entiers

```python
>>> 42
42
```

----

## Entiers

```python
>>> 18446744073709551616
18446744073709551616
```

----

## Virgule flottante

```python
>>> 3.1415
3.1415
```

----

## Virgule flottante

```python
>>> 0.1 + 0.2
0.30000000000000004
```

https://0.30000000000000004.com

----

## Chaînes de caractères

```python
>>> "Anne Elk's Theory"
"Anne Elk's Theory"
```
Notes:

Expliquer ce qu'est une chaîne, sans parler de pointeurs, on est pas
dans un cours de C89.

----

## Chaînes de caractères

```python
>>> 'Colin "Bomber" Harris'
'Colin "Bomber" Harris'
```
----

## Chaînes de caractères

```python
>>> """Anne Elk's Theory est "mieux"."""
'Anne Elk\'s Theory est "mieux".'
```

----


## Listes

```python
>>> [2, 3, 5, 7]
[2, 3, 5, 7]
```

Notes:

La représentation est souvent du Python valide.

----

## Listes

```python
>>> [1, 1.5, 2, 2.5]
[1, 1.5, 2, 2.5]
```

Notes:

Attention à ne pas abuser du mélange autorisé des types.

----

## Listes

```python
>>> [[1, 1], [1, 2], [2, 1], [2, 2]]
[[1, 1], [1, 2], [2, 1], [2, 2]]
```
Notes:
Une liste c'est de la donnée, ce qu'elle contint c'est de la donnée.

----

## *n*-uplets
```python
>>> 1, 2
(1, 2)
>>> "Graham", "John", "Terry"
('Graham', 'John', 'Terry')
```
Notes:
C'est la virgule qui fait le n-uplet, pas les parenthèses.

Pensez au *n*-uplet comme une structure C, *a record*, pas comme une
liste, par exemple des coordonnées : (x, y).

----

## Ensembles
```python
>>> {101, 103, 107, 109}
{109, 107, 101, 103}

```
Notes:
Un ensemble n'est pas ordonné.

----

## Dictionnaires

```python
>>> {"Zero": 0, "Un": 1, "Deux": 2}
{'Zero': 0, 'Un': 1, 'Deux': 2}
```
Notes:

On associe une valeur à une clé. Utile *seulement* si on ne connaît
pas les clefs à l'avance, sinon c'est une classe.

---

# Les opérateurs

----

## Les opérateurs
### Mathématiques

```python
>>> 10 + 10
20
>>> 1j * 1j
(-1+0j)
>>> 10.5 + 2
12.5
```

----

## Les opérateurs
### Mathématiques

```python
>>> (4 * 10 ** 1) + (2 * 10 ** 0)
42
```

----

## Les opérateurs
### Mathématiques

```python
>>> 10 / 2
5.0
```
----

## Les opérateurs


```python
>>> "La vie " + "de Brian"
'La vie de Brian'
```
Notes:
It's called concatenation of strings.

----

## Les opérateurs

```python
>>> "Tu tum pak " * 2
'Tu tum pak Tu tum pak '
```
Notes:
Tant qu'il n'y a pas d'ambiguité, c'est implémenté.

----

## Les opérateurs

```python
>>> [2, 3, 5] + [7, 11, 13, 17]
[2, 3, 5, 7, 11, 13, 17]
```

----

## Les Comparisons


```python
>>> 10 < 1
False
>>> 10 == 10
True
>>> 10 >= 20
False
```

Notes:

Déconseiller l'utilisation de `is`, de toute facons PyLint leur dira
quand l'utiliser.

----

## Logique

```python
>>> True or False
True
>>> True and False
False
>>> not True
False
```


----

## Test d'appartenance

```python
>>> "aa" in "sacré graal"
True
```

----

## Test d'appartenance

```python
>>> 7 in {2, 3, 5, 7, 11}
True
```


----

## Travailler avec les ensembles

```python
>>> {1, 2} | {1, 3, 4} == {1, 2, 3, 4}
True
```

Notes:
C'est une union.

----

## Travailler avec les ensembles

```python
>>> {"a", "b"} & {"a", "x", "y"}
{'a'}
```

Notes:
Une intersection.

----

## Mais en cas d'ambiguité…

```python
>>> "D'oh!" * "D'oh!"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```

----

## Mais en cas d'ambiguité…

```python
>>> {"a", "b"} + {"a", "x", "y"}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
```

---

# Variables

----

## Affectation

```python
>>> x = 10
>>> y = 10
>>> x + y
20
```

Notes:

« x » est assigné à 10.

JAMAIS dire: 10 est assigné à « x ».
JAMAIS JAMAIS dire : On met 10 dans « x ».

----

## Affectation multiple

```python
>>> x, y = 2, 3
>>> x
2
>>> y
3
```


----

## Accès par indice

```python
>>> first_primes = [2, 3, 5, 7, 11, 13]
>>> first_primes[0]
2
>>> first_primes[1]
3
```
Notes:
On réutilise le nom pour accéder au contenu.

Bien prendre le temps d'expliquer la syntaxe ici.

----

## Accès par clé

```python
>>> d = {"zero": 0, "un": 1, "deux": 2}
>>> d["deux"] + d["deux"]
4
```

---

# Les méthodes
----

## Sur les chaînes
```python
>>> s = "The prime numbers."
>>> s.title()
'The Prime Numbers.'
>>> s.startswith("The")
True
>>> s.split()
['The', 'prime', 'numbers.']
```

----

## Sur les listes

```python
>>> l = [2, 3, 5, 7]
>>> l.append(11)
>>> l.sort(reverse=True)
>>> l
[11, 7, 5, 3, 2]
```

----

## Sur les dictionnaires

```python
>>> d = {"zero": 0, "un": 1, "deux": 2}
>>> d.keys()
dict_keys(['zero', 'un', 'deux'])
>>> d.values()
dict_values([0, 1, 2])
>>> d.items()
dict_items([('zero', 0), ('un', 1), ('deux', 2)])
```

---

# Les fonctions

Les fonctions natives, et comment en créer.

----

## Fonctions natives

docs.python.org/3/library/functions.html

----

## print

```python
>>> print("zero")
zero
```

Notes:

C'est leur première fonction, s'attarder sur la syntaxe !

----

## print

```python
>>> print("√2 =", 2 ** 0.5)
√2 = 1.4142135623730951
```

Notes:

En effet, le P de REPL étant `print`, le print est implicite dans un REPL.

Mais le REPL sert a tester : on peut bien tester print dans le REPL.

----

## len

```python
>>> len([1, 2, 3])
3
>>> len("Bonjour")
7
```

----

## range

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
```

----

## all

```python
>>> all([True, False, True])
False
>>> all([True, True, True])
True
>>> all([False, False, False])
False
```

----

## any

```python
>>> any([True, False, True])
True
>>> any([True, True, True])
True
>>> any([False, False, False])
False
```

----

## breakpoint

Invoque un débugger Python, très utile, plus tard.

----

## help

Affiche la documentation de n'importe quoi, essayez :

   - `help()` pour un mode interactif.
   - `help(str)`
   - `help(list)`
   - `help("list")`

Notes:

Accepte aussi une variable mais attention: si la variable est une
chaîne, help n'affichera pas la documentation des chaînes.

----

## enumerate

```python
>>> txt = """Zero
... Un
... Deux"""
>>> lines = txt.split("\n")
>>> list(enumerate(lines))
[(0, 'Zero'), (1, 'Un'), (2, 'Deux')]
```

----

## sorted

```python
>>> sorted([2, 1, 7, 6])
[1, 2, 6, 7]
```

----

## exit

Appeler `exit()` quitte simplement le REPL.

Notes: Préferer `sys.exit()` dans un programme.

---

# Les instructions

----

## if

```python
>>> if 1 in {2, 3, 5, 7, 11}:
...     print("1 serait-il premier ?")
...
>>>
```

Notes:

Parler de l'indentation !

Notez le `...`, on a du appyer un coup en « entrée » pour fermer ce bloc.

1 était premier, avant, mais ça casse le théorème « Every possible
whole number can be written as a _unique_ product of primes ».

----

## for

```python
>>> d = {"zero": 0, "un": 1, "deux": 2}
>>> for number in d:
...     print(number)
...
zero
un
deux
>>>
```

----

## for

```python
>>> d = {"zero": 0, "un": 1, "deux": 2}
>>> for number, value in d.items():
...     print(number, value)
...
zero 0
un 1
deux 2
>>>
```

---

## for

```python
>>> for i in range(5):
...     print(i)
0
1
2
3
4
```

---

# Les instructions (suite)

Notes:

On couvre un peu plus de syntaxe après quelques exercices.

----

## L'instruction `while`

Très rarement utilisée car le `for` est bien plus pratique, sert
cependant dans quelques cas:

- `while True:`
- `while il_reste_du_travail_à_faire:`

----

## L'instruction `while`

```python
>>> sq = 5
>>> gues = 2
>>> error = abs(sq - gues * gues)
>>> while error > 0.0001:
...     gues = (gues + sq / gues) / 2
...     error = abs(sq - gues * gues)
>>> gues
2.2360679779158037
```

Notes:
Je sais pour la faute de frappe sur guess, mais sinon ça dépasse.

Méthode_de_Héron.

----

## `break` et `continue`

Break sert à interrompre une boucle, continue sert à passer à l'élément
suivant. Qu'on soit dans un `for` ou dans un `while`.

----

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

----

## `continue`

```python
>>> for i in range(5):
...     if i == 0:
...         continue
...     print(i)
1
2
3
4
```

----

## Le `else`

Après un bloc `if`, on peut ajouter un bloc `else` :

```python
def fib(x):
    if x < 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
```

Notes:
(Juste pour doctest :)
```python
>>> [fib(x) for x in range(10)]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

----

## Le `elif`

Après un `if`, on peut ajouter un ou des bloc `elif` :

```python
def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        ...
```

Notes: Parler de `pass` et de `...`.

----


## Les exceptions

```python
>>> int("abc")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
```

----

## Les exceptions : `try`

```python
>>> try:
...     int("abc")
... except ValueError:
...     print("Raté")
Raté
```

---

## La notation par intension

C'est transformer ça :

```python
>>> accumulator = []
>>> for i in range(10):
...    accumulator.append(2 ** i)
>>> accumulator
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```


----

## La notation par intension

en :

```python
>>> [2 ** i for i in range(10)]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

----

## La notation par intension

Ou :

```python
def phi(n):
    numbers = []
    for i in range(n):
        if math.gcd(i, n) == 1:
            numbers.append(i)
    return len(numbers)
```

----

## La notation par intension

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

Notes: Elle devrait s'écrire sur une seule ligne, mais, vidéoprojecteur...

---

# Les variables (suite)

----

## Le type des variables

En Python, les variables ne sont que des noms.

*Des « étiquettes » qu'on colle aux objets.*

Seul les valeurs sont typées.

*Toutes les valeurs sont des objets.*

Notes: Sans. Exceptions.

On peut « coller » plusieurs étiquettes à une même valeur.

C'est pour ça que pour `n = 10` on dit "n est assigné à 10", et non "10 est mis dans n".


----

## La portée des variables

Dans une fonction :
- Si on ne fait qu'accéder, ce sera une globale.
- Si on affecte, c'est une locale.

Notes:
Pour l'accès pensez à `print` par exemple, l'utiliser n'en fait pas une locale.
Une variable ne peut *presque* jamais ne pas contenir de valeur, et on ne peut pas la "déclarer".

----

## Immuables vs modifiables

Certains types sont modifiables, d'autres, non.

Notes: On dit qu'elles sont immuables (*immutable* en anglais).

Attention, les variables sont toujours ... variables, nous n'avons pas
de constantes.

----

## Les types modifiables

Parmis les types modifiables on trouve :

Les listes, les dictionnaires, les ensembles, …

*On peut ajouter a une liste, modifier la valeur pour une clé d'un
dictionnaire, ou vider un ensemble par exemple.*

----

## les types immuables

Parmis les types immuables on trouve :

Les chaînes de caractères, les *n*-uplets, les entiers, les booléens, …

*On ne peut pas dire que maintenant 10 vaut 12, ni que faux est vrai.*


Notes:

Pour les chaînes c'est discutable, mais avoir des chaînes immuables
est confortable (clef de dictionnaires par exemple, ou la garantie
qu'un appel à une fonction avec une chaîne en paramètre ne va pas la
modifier).

----

## La vérité

En Python, ce qui est vide est faux, 0 est faux. Le reste est vrai :

```python
>>> bool("Non vide")
True
>>> bool([])  # Une liste vide
False
>>> bool(0.0)
False
```

Notes:
Attention à la sémantique : `if foo` est différent de `if foo is True`.

Leur rappeler que c'est pylint qui leur dira quand utiliser `is`, leur
dire quand même : pour `True`, `False`, et `None`.

---

# Fonctions (suite)

Créer ses propres fonctions

----

## Syntaxe

```python
def la_fonction(ses_paramètres):
    """Une courte description.
    """
    # Le corps de la fonction
```

Notes:

Passer du temps sur la syntaxe et le vocabulaire
 - fonction
 - paramètre, argument
 - `return`


----

## Paramètres

Une fonction prend des paramètres et renvoie une valeur.

```python
def ones_in_binary(value):
    as_binary = bin(value)
    return as_binary.count("1")
```
----

## Arguments

On peut donc lui donner des arguments :
```python
>>> print(ones_in_binary(42))
3
```
