# Les instructions

----

## if

```python
>>> if 1 in {2, 3, 5, 7, 11}:
...     print("1 serait-il premier ?")
...
>>>
```

Notes:

Parler de l'indentation !

Notez le `...`, on a du appyer un coup en « entrée » pour fermer ce bloc.

1 était premier, avant, mais ça casse le théorème « Every possible
whole number can be written as a _unique_ product of primes ».

----

## for

```python
>>> d = {"zero": 0, "un": 1, "deux": 2}
>>> for number in d:
...     print(number)
...
zero
un
deux
>>>
```

----

## for

```python
>>> d = {"zero": 0, "un": 1, "deux": 2}
>>> for number, value in d.items():
...     print(number, value)
...
zero 0
un 1
deux 2
>>>
```

---

## for

```python
>>> for i in range(5):
...     print(i)
0
1
2
3
4
```
