# Python

Jour 3


# Le packaging


## Le packaging

Restez dans les standards : `pyproject.toml`, `setup.cfg`.


## pyproject.toml et setup.cfg

- https://github.com/JulienPalard/oeis
- https://setuptools.readthedocs.io/


## pip

```bash
(test) $ pip install -e .
```


## pytest

```bash
(test) $ mkdir tests/
(test) $ pip install pytest
(test) $ editor tests/test_dice.py
```

Notes: C'est l'occasion de parler de assert.


## hypothesis

```python
from hypothesis import given
from hypothesis.strategies import integers

@given(integers(min_value=2,
                max_value=1000))
def test_fib(i):
    assert fib(i) == fib(i-1) + fib(i-2)
```


## pdb

```
breakpoint()
```


## PYTHONDEVMODE=y

Et `./configure --with-pydebug`.

Notes: Voir mon bashrc :] Surtout "viable" depuis la 3.8.



# Les modules utiles

- argparse
- re
- csv (quand on a pas Pandas)
- subprocess


# La communauté

> Come for the language, stay for the community

— Brett Cannon



## Les PyCons

La PyConFr (tous les ans, sauf cette année) ! Les meetups locaux hors période de pandémie !
