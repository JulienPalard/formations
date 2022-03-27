# Les objets

## Rappels

- Keep it simple.
- Flat is better than nested.


## `classmethod` vs `staticmethod`

## La MRO

Notes:

Simple démo REPL : `bool.__mro__`.

## `super()` !

Notes:

Et la coopération, démo avec deux classes : `TCPConnection` qui prend
`host, port, timeout`, et `HTTPConnection` qui prend url, method, ...`

Démo aussi : passer un argument de trop et voir que object() se plains.

Antisèche : https://wyz.fr/3Z8


## Le protocole « descripteur »

- `object.__get__(self, instance, owner=None)`
- `object.__set__(self, instance, value)`

Notes:

Et `__delete__` et `__set_name__`.

- instance... c'est l'instance.
- owner, c'est le type, il est toujours connu donc "devrait" toujours être donné
- Si instance n'est pas donnée, c'est qu'on accède à l'attribut sur le type.

Exercice : https://www.hackinscience.org/exercises/temperature-class


## Métaclasses

Puisqu'une classe est un objet, une métaclasse c'est le type du type.

Notes:

En initiation on dit "ça ne vous servira pas". En avancé on dit
`__init_subclass__` couvrira tous vos besoins.


## Métaclasse

- `__new__` et `__init__` d'une classe servent à personaliser l'instance.
- `__new__` et `__init__` d'une metaclasse servent à personalier une classe.

Notes:

```python
class M(type):
    def __new__(cls, *args, **kwargs):
        print(f"meta.__new__(*{args}, **{kwargs})")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print(f"meta.__init__(*{args}, **{kwargs})")
        super().__init__(*args, **kwargs)

class MyCls(metaclass=M):
    def __new__(cls, *args, **kwargs):
        print(f"cls.__new__(*{args}, **{kwargs})")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print(f"cls.__init__(*{args}, **{kwargs})")
        super().__init__(*args, **kwargs)
```

Vous pouvez aussi utiliser un décorateur pour personaliser une classe.
