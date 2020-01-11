# Les types

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
On associe une valeur à une clé.

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
'Tu tum pak Tu tum pak'
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
>>> {"a", "b"} | {"a", "x", "y"}
{'a', 'x', 'y', 'b'}
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

# Les instructions
----
## if

```python
>>> if 1 in {2, 3, 5, 7, 11}
...     print("1 serait-il premier ?"}
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

# Les fonctions
----

## Fonctions natives

```python
>>> print("zero")
zero
```

----

## Fonctions natives

```python
>>> exit()
$
```

----

## Fonctions natives

```python
>>> help(list)
>>> d = {}
>>> help(d)
```

----

## Fonctions natives

```python
>>> len([1, 2, 3])
3
```

----

## Fonctions natives

```python
>>> for i in range(5):
...     print(i)
0
1
2
3
4
```

----

## Fonctions natives

```python
>>> for i in range(10, 15):
...     print(i)
10
11
12
13
14
```

----

## Fonctions natives

docs.python.org/3/library/functions.html
