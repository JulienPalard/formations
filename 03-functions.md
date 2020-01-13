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
