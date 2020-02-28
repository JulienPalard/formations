# À ranger

## Virgule flottante

```python
>>> 0.1 + 0.2
0.30000000000000004
```

https://0.30000000000000004.com


## Chaînes de caractères

```python
>>> """Anne Elk's Theory est "mieux"."""
'Anne Elk\'s Theory est "mieux".'
```

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


# A refare

Ajouter les nombres imaginaires en avancé.

Jour 1 virer le try, le bouger jour 2.
