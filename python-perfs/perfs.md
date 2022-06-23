# Les Performances en Python

par

Julien Palard <julien@palard.fr>

https://mdk.fr


# Bien choisir sa structure de donnée

C'est bien choisir l'algorihtme qu'on va utiliser.


## Comparaison asymptotique

Les notations les plus utiisées :

```text
O(1)        Constant
O(log(n))   Logarithmique
O(n)        Linéaire
O(n log(n)) Parfois appelée « linéarithmique »
O(n²)       Quadratique
O(nᶜ)       Polynomiale
O(cⁿ)       Exponentielle
O(n!)       Factorielle
```

## Les mesures de complexité

- De temps (CPU consommé)
- D'espace (Mémoire consommée)
- Dans le meilleur des cas
- Dans le pire des cas
- Dans le cas moyen
- Amorti
- ...


## Les mesures de complexité

Il n'est pas forcément nécessaire d'apprendre par cœur toutes les complexités de chaque opération.

Pas toute suite.


## Les bases

Mais retenir par cœur la complexité de quelques structures
élémentaires permet d'éviter les « erreurs de débutants ».


## Rappel des unités de temps

- 1 milliseconde (1 ms) c'est un millième de seconde.
- 1 microseconde (1 μs) c'est un millionième de seconde.
- 1 nanoseconde (1 ns) c'est un milliardième de seconde.


## Le cas typique

```bash
$ python -m timeit -s 'container = list(range(10_000_000))' \
  '10_000_001 in container'
#!bkt -- python -m timeit -s 'container = list(range(10_000_000))' '10_000_001 in container'

$ python -m timeit -s 'container = set(range(10_000_000))' \
  '10_000_001 in container'
#!bkt -- python -m timeit -n 100 -s 'container = set(range(10_000_000))' '10_000_001 in container'
```

Pourquoi une si grande différence !?


::: notes

C'est l'heure du live coding !


# Les outils

## Les outils en ligne de commande

`time`, un outil POSIX, mais aussi une fonction native de bash :

```bash
$ time python -c 'container = set(range(10_000_000))'
#!bkt -- time -p python -c 'container = set(range(10_000_000))' 2>&1
```

Mais `time` ne teste qu'une fois, ce n'est pas fiable.

::: notes

real    0m0.719s  # C'est le temps « sur le mur »
user    0m0.521s  # Temps CPU passé « dans Python »
sys     0m0.195s  # Temps CPU passé dans le kernel


## Hyperfine

`hyperfine` teste plusieurs fois :

```text
$ hyperfine "python -c 'container = set(range(10_000_000))'"
Benchmark 1: python -c 'container = set(range(10_000_000))'
  Time (mean ± σ):     735.6 ms ±  11.2 ms
```


## Petite parenthèse

Mais attention, démarrer un processus Python n'est pas gratuit :

```python
$ hyperfine "python -c pass"
Benchmark 1: python -c pass
  Time (mean ± σ):      19.4 ms ±   0.6 ms
```

## Petite parenthèse

Et puis il peut dépendre de la version de Python, des options de compilation, ... :

```text
$ hyperfine "~/.local/bin/python3.10 -c pass"  # Avec pydebug
Benchmark 1: ~/.local/bin/python3.10 -c pass
  Time (mean ± σ):      37.6 ms ±   0.6 ms

$ hyperfine "/usr/bin/python3.10 -c pass"  # Sans pydebug
Benchmark 1: /usr/bin/python3.10 -c pass
  Time (mean ± σ):      19.1 ms ±   0.8 ms
```

::: notes

Leur parler de `--enable-optimizations` (PGO).


## timeit

Timeit c'est dans la stdlib de Python, ça s'utilise en ligne de commande ou depuis Python.


## pyperf

C'est l'équivalent d'hyperfine mais exécutant du Python plutôt qu'un programme :

```bash
$ ~/.local/bin/python3.10 -m pyperf timeit pass
.....................
Mean +- std dev: 7.33 ns +- 0.18 ns

$ /usr/bin/python3.10 -m pyperf timeit pass
.....................
Mean +- std dev: 6.10 ns +- 0.11 ns
```

::: notes

Avec hyperfine on teste combien de temps ça prend à Python **de
démarrer** puis d'exécuter `pass`, ici on teste combien de temps ça
prend d'exécuter `pass`.


## cProfile

time, timeit, hyperfine, pyperf c'est bien pour mesurer, comparer.

cProfile nous aider à trouver la fonction coupable dans un script plus gros.


## cProfile, exemple

```python
#! cat approx_phi_up_to_1.py | tail -n 13
```


## cProfile, exemple

Testons :

```python
#! cat approx_phi_test.py
```

```text
$ python approx_phi_test.py
#!bkt -- python approx_phi_test.py
```

C'est déjà lent, et pour `20` c'est interminable...


## cProfile, exemple

Sortons cProfile :

```text
$ python -m cProfile --sort cumulative approx_phi_test.py
#! bkt -- python -m cProfile --sort cumulative approx_phi_test.py | head
```

## cProfile, exemple


```bash

$ python -m pstats fib.prof
prof% stats 10
Mon Jun 13 10:12:29 2022    prof

         30903333 function calls (133 primitive calls) in 5.381 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.381    5.381 {built-in method builtins.exec}
        1    0.000    0.000    5.381    5.381 /tmp/fib.py:1(<module>)
       33    0.000    0.000    5.381    0.163 /tmp/fib.py:8(approx_phi)
30903265/65    5.381    0.000    5.381    0.083 /tmp/fib.py:3(fib)
```

## cProfile, exemple

30903265 appels à la fonction `fib` !? On a notre coupable !

## cProfile, exemple


```python
@cache
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def approx_phi(n):
    return fib(n + 1) / fib(n)

def approx_phi_up_to(n_digits):
    with localcontext() as ctx:
        ctx.prec = n_digits + 1
        for n in count():
            step1 = approx_phi(n)
            step2 = approx_phi(n + 1)
            if step1 == step2:
                return step1
```

notes :::

On est très vite limités par les floats...

## cProfile, exemple

Dépassons la limite des floats avec le module Decimal :

```python
def approx_phi(n):
    return Decimal(fib(n + 1)) / Decimal(fib(n))
```

## cProfile, exemple

Et allons plus loin :

```python
def approx_phi_up_to(n_digits):
    with localcontext() as ctx:
        ctx.prec = n_digits + 1
        for n in count():
            step1 = approx_phi(n)
            step2 = approx_phi(n + 1)
            if step1 == step2:
                return step1
```

::: notes

Jusqu'à 5000 décimales ça marche bien, mais bon ça devient lent, c'est l'heure de cProfile !

## cProfile, exemple

```text
   Ordered by: cumulative time
   List reduced from 140 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/1    0.000    0.000   15.266   15.266 {built-in method builtins.exec}
        1    0.000    0.000   15.266   15.266 /tmp/fib.py:1(<module>)
        1    0.012    0.012   15.264   15.264 /tmp/fib.py:16(approx_phi_up_to)
    28714   15.244    0.001   15.252    0.001 /tmp/fib.py:13(approx_phi)
    14359    0.008    0.000    0.008    0.000 /tmp/fib.py:7(fib)
```

`fib` n'y est pour rien, c'est `approx_phi` qui prend près de 100% du
temps, surtout parce qu'il est appelé près de 30_000 fois !


## cProfile, exemple

Divisons par 10 le nombre d'appels, on réduira mécaniquement par 10 le temps d'exécution :

```python
    [...]
    step1 = approx_phi(10 * n)
    step2 = approx_phi(10 * n + 1)
    [...]
```
## cProfile, exemple

En rajoutant du cache sur `approx_phi` et en faisant en sorte de
réutiliser un des deux appels à chaque étape, on peut certainement
encore au moins diviser par deux le temps d'exécution :

```python
    step1 = approx_phi(2 ** n)
    step2 = approx_phi(2 ** (n+1))
```

`RecursionError` !? En effet, en avançant par si grands pas, le cache
de `fib` n'est pas chaud, et il peut vite devoir descendre
profondément en récursion...

## cProfile, exemple

Il est temps de sortir une implémentation de `fib` plus robuste, basée
sur l'algorithme « matrix exponentiation » :

```
@cache
def fib(n):
    if n in (0, 1):
        return 1
    x = n // 2
    return fib(x - 1) * fib(n - x - 1) + fib(x) * fib(n - x)
```


## cProfile, exemple

```bash
$ time python fib.py
real    0m0.064s
user    0m0.060s
sys     0m0.005s
```

Mieux.

## TODO

snakeviz
scalene
vprof
https://pypi.org/project/pyflame/
...

# Cython

# Numba

# mypyc

# Pythran

# Hand crafted C
