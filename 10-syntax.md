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
