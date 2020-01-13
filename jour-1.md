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
