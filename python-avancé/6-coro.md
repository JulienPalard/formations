# async / await

Une coroutine est une fonction dont l'exécution peut être suspendue.


## Callback Hell

```
function pong_handler(client)
{
    client.on('data', function (data)
    {
        client.on('data_written', function ()
        {
            client.close()
        });
        client.write(data)
        client.flush()
    });
}
```


## Avec des coroutines

```python
async def pong_handler():
    client.write(await client.read())
    await client.flush()
    client.close()
```

## Les coroutines

 - generator-based coroutines
 - native coroutines


## Generator-based coroutines

```pytho
import types


@types.coroutine
def get_then_print(url):
    ...
```


## Native coroutines

```python
async def get_then_print(url):
    ...
```


## Coroutines

Une `coroutine`, renvoie un objet `coroutine` :

```
>>> async def tum():
...     print("tum")
...
>>> tum()
<coroutine object tum at 0x7fa294538468>
```


## Coroutines

```
>>> async def tum():
...     print("tum")
...
>>> a_coroutine_object = tum()
>>> a_coroutine_object.send(None)
tum
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  StopIteration
```

Notes:

qu'on peut manipuler.

As you can see, calling `tum()` did not execute the `print("tum")`,
but calling `.send(None)` did (see PEP 342).

L'appel de .send est fait par la main loop (asyncio.run).


## Récupérer un résultat

Le résultat d'une coroutine est stocké dans l'exception `StopIteration`.

Notes:

Dans l'attribut `value`.


## await


```
async def two():
    return 2

async def four():
    return await two() + await two()

coro = four()
coro.send(None)
```

Notes:

Ça donne `StopIteration: 4`, de manière complètement synchrone.


## Suspendre une coroutine.

Ce n'est pas possible dans une coroutine.

Notes:

Bon, à part `await asyncio.sleep(0)`, ou toute attente vers un
awaitable qui se suspend sans rien faire.


## Future-like object

Un `future-like object` est un object implémentant `__await__`, qui a
le droit de `yield`. L'expression du yield traversera toute la stack
d'`await` jusqu'au `send(None)`.


## Awaitables

Les [awaitables](https://www.python.org/dev/peps/pep-0492/#await-expression)
sont des objets pouvant être « attendus » via un `await`.

Notes:

Typiquement `coroutine` ou un objet implémentant `__await__`.


## Gérer ses coroutines

```python
async def two():
    return 2

async def four():
    return await two() + await two()

def coro_manager(coro):
    try:
        coro.send(None)
    except StopIteration as stop:
        return stop.value

print(coro_manager(four()))
```


## Gérer ses coroutines


```python
class Awaitable:
    def __await__(self):
        yield

async def wont_terminate_here():
    await Awaitable()
    print("Terminated")
    return 42

print(coro_manager(wont_terminate_here()))
```

## Gérer ses coroutines


```python
def frenetic_coro_manager(coro):
    try:
        while True:
            coro.send(None)
    except StopIteration as stop:
        return stop.value
```


## Gérer ses coroutines

```python
import random


def frenetic_coros_manager(*coros):
    coros = list(coros)
    while coros:
        coro = random.choice(coros)
        try:
            coro.send(None)
        except StopIteration as stop:
            coros.remove(coro)
```


## Gérer ses coroutines

```python
async def tum():
    for _ in range(10):  # ou : while True:
        await Awaitable()
        print("Tum")

async def pak():
    for _ in range(10):  # ou : while True:
        await Awaitable()
        print("Pak")

frenetic_coros_manager(tum(), pak())
```
