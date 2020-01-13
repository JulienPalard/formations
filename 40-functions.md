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
