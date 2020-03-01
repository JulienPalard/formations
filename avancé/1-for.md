# Python

Notes:

En initiation, on utilise (le for par exemple),
en avancé on crée (des itérables par exemple).

- Exemples concrets et définitions abstraites
  - Pas de `class Foo`, le cerveau ne peut s'accrocher à rien.
  - Le bonheur est dans le chemin et dans la finalité
- Contenu différenciant
  - Pas de `class Foo`, tout le monde le fait déjà.
  - Détaillez toutes les étapes, même les plus petites.
  - Soyez drôle ! Donnez envie !

J'ai 5 jours, donc ~200 slides.


## « Tout est objet »

Comme en Java, #oupas

Notes:

- Sortir un interpréteur.
- Leur faire essayer de deviner ce qui pourrait ne pas être une classe.
- Démo avec:
 - un nombre entier, #obvious, c'est géré par Python
   - ouvrir une parenthèse si nécessaire, avec 6 ** 6 ** 6
 - un float, en les faisant hésiter vu qu'ils sont « gérés par le CPU »
 - une fonction
 - une classe (et une instance)
 - range !
 - module !!

OK mais pas `for`, `def`, ... ce sont des mots clefs.


## Donc, tout a des attributs…

Notes:

Exercice : avec des `set`, et `dir()`, trouver la liste des attributs
communs à une fonction, disons `max` et à un int, disons `42`,
combien y'en-a-il ? Moi 23. Combien `object` en a-il ?


## Même un int ?

```python
>>> (42).__bool__() is bool(42)
True
```

Notes:

Ouvrir une parenthèse sur la notion de vérité, ce qui est :

- Vide
- Égal à zéro
- None ou False

c'est faux, le reste, c'est vrai.


## Les noms

Notes:

Faire le schéma à deux colonnes: noms → mémoire.

En Python avancé bien insister sur le fait qu'un objet en mémoire à
une adresse.

Insister sur le fait qu'un paramètre de fonction n'est qu'un nom. On a
donc pas de « passage par valeur » chez nous.

Bien préciser qu'on ne peut pas « délier » un nom pour le faire
pointer sur rien (en ce cas on le fait pointer sur None).


## Pendant qu'on parle des noms

Leur portée dans une fonction ?

Notes:

In Python, variables that are only referenced inside a function are
implicitly global. If a variable is assigned a value anywhere within
the function’s body, it’s assumed to be a local unless explicitly
declared as global.


## UnboundLocalError

Mais qui ment dans l'histoire ?

Notes:

Personne :

On ne peut pas « délier » un nom, mais il peut très bien ne jamais
avoir été lié.

Faire un exemple dans un fichier.


# J'ai 5mn pour vous parler de `for`

Notes:

Déjà, c'est pas un objet.

Jusqu'où peut-on creuser ?


## `for` itère sur des itérables

- Itérable : Objet dont on peut obtenir les éléments un à un.
- Itérateur : Représentation d'un flux d'éléments.
- Séquence : Un itérable dont les éléments sont accessible par indice et dont on connaît la taille.
- Collection : Itérable dont on connaît la longueur.

Notes:

On peut très bien imaginer un itérateur capable d'itérer un itérable,
mais aussi une séquence, une collections, ...


## Le protocole « séquence »

Implémente `__getitem__` et `__len__`.

(voir meme `__reversed__`, `__iter__` et `__contains__`).

Notes:

Exercice, implémenter un `range()`, mais sans `stop` ni `step`.

Petite parenthèse : `range`, c'est une classe ou une fonction ?


## Le protocole « séquence »

`__getitem__` suffit pour être itérable.

Notes:

C'est l'application du duck-typing : Si ça a tout ce dont `for` à
besoin, alors ça fonctionne. `for` n'a pas besoin de connaître la
taille, donc ça fonctionne.


## Le protocole d'itération

Notes:

Itérable : Objet capable de renvoyer ses éléments un à un.
Itérateur : Objet chargé de s'occuper de l'itération d'un itérable :
se souvenir où on en est.


## Le protocole d'itération

- `iter()` : Crée un itérateur à partir d'un itérable.
- `next()` : Demande l'élément suivant à un itérateur.

Notes:

Première démo REPL sur une liste « on reste utilisateurs de Python ».


## Le protocole d'itération

`__iter__` et `__next__`

Notes:

Démo REPL sur une liste « on perçoit comment on va pouvoir
l'implémenter ».

La différence ? Petite parenthèse : `iter()` peut utiliser soit le
protocole séquence soit le protocole d'itération, et fait quelques
vérifications (que l'itérateur renvoyé soit bien un itérateur).


## Petite parenthèse

```python
>>> class Counter:
...     def __getitem__(self, i):
...         return i
...
>>> i = iter(Counter())
>>> i
<iterator object at ...>
>>> next(i)
0
>>> next(i)
1
>>> next(i)
2
```

Notes:

Via le protocole séquence, `__len__` n'est pas utilisé donc ça se
passe bien.


## Petite parenthèse

```python
>>> class B: ...
...
>>> iter(B())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'B' object is not iterable
```

Notes:

`iter()` donne une belle exception.


## Petite parenthèse

```python
>>> class C:
...     def __iter__(self): return None
...
>>> iter(C())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: iter() returned non-iterator of type 'NoneType'
```

Notes:

`iter()` valide que `__iter__` renvoie bien un itérateur.


## Digression

`iter` a aussi une version qui prend deux paramètres.

```python
from functools import partial

with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
```


## Retour sur `__iter__`

```python
    def __iter__(self):
        return self
```

Notes:

Mauvaise idée !

Réimplémentez la classe `Counter()` comme ça.


## Solution

```python
class Counter:
    def __init__(self): self.i = -1
    def __iter__(self): return self
    def __next__(self):
        self.i += 1
        return self.i
```

## Le problème

```python
>>> c = Counter()
>>> for i, j in zip(c, c):
...     print(i, j)
...     if i > 5: break
...
0 1
2 3
4 5
6 7
```


## On recommence

Notes:

Cette fois avec un itérateur dédié.


## Solution

```python
class BetterCounter:
    def __iter__(self):
        return CounterIterator()
```


## Solution

```python
class CounterIterator:
    def __init__(self):
        self.i = -1

    def __next__(self):
        self.i += 1
        return self.i
```


## Solution

```python
>>> c = BetterCounter()
>>> for i, j in zip(c, c):
...     if i > 5: break
...     print(i, j)
0 0
1 1
2 2
3 3
4 4
5 5
```

Notes:

C'est toujours faux ! Un itérateur doit AUSSI implémenter `__iter__`,
donc qui `return self`, ça permet d'utiliser aussi les itérateurs avec
for.


## Peut-on faire plus simple ?

Notes:

Oui ! Avec un générateur ! C'est le sucre syntaxique pour créer ses
itérables.

Attention, une fonction générateur renvoie un itérateur, (qu'on
appelle un générateur), pas un itérable ! Et là on est bien contents
qu'un itérateur ai un `__iter__` qui se renvoie lui même, pour pouvoir
l'utiliser dans un for !


## Mais alors

Si une fonction générateur renvoie un itérateur, et que `__iter__`
doit renvoyer un itérateur, on peut implémenter `__iter__` avec yield ?

Notes:

Oui.


## Exemple

```python
class GenCounter:
    def __iter__(self):
        i = 0
        while True:
            yield i
            i += 1
```


## Pendant qu'on parle de `yield`

Connaissez-vous `yield from` ?


## Pendant qu'on parle de `for`

Connaissez-vous le `else` du `for` ?

Notes:

Il ne s'exécute que si le `for` sort sans `break`.


## `else`

```python
>>> n = 13
>>> for i in range(2, n - 1):
...     if n % i == 0:
...         print(f"{n} is not prime")
...         break
... else:
...     print(f"{n} is prime")
13 is prime
```

Notes:

Typiquement utile lors des recherches, la sémantique :
 - Trouvé, plus besoin de chercher, break.
 - else: pas trouvé.

Fonctionne aussi sur le while.

Ah j'ai utilisé une f-string.


## Literal String Interpolation

```python
>>> f"{42:08b}"
'00101010'
```

Notes:

Attention aux ':' et '!' dans l'expression, bien que ce soit accepté
si c'est entre guillemet, crochets, parenthèses, ... sinon toute
expression Python est autorisée (comme avec .format, mais avec .format
c'est plus évident).


## Literal String Interpolation

```python
>>> f"{(lambda x: x.upper())('hello'):^11}"
'   HELLO   '
```

Notes:

Attention à rester lisible, mais ici le `:` de la lambda est entre
parenthèses, donc c'est bon.

En parlant de parenthèse, fermons une parenthèse.


## On parlais d'itérables

Si on parlais d'unpacking ?

Notes:

Pour se remémorer ces choses, cherchez les PEPs, typiquement la 448, la 3132, ...

- Parler de `deep unpacking`.
- Parler de `head, *rest`, ...


## Ça peut rappeler `*args` et `**kwargs`

Notes:

Démo si nécessaire.
