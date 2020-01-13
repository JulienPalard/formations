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
