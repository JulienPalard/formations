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
