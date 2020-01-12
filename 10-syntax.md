# Python 3.8

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

# Les variables

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
