# Le packaging

## Petite parenthèse

La différence entre un paquet et un module ?

Notes:

Pour Python il n'y en a pas, tout est module, pour nous, un paquet est
un dossier.  Aborder rapidement les paquets-espace-de-noms.


## Digression

`__main__` et `__main__.py`.


## venv

Notes:

Et ses alternatives : virtualenv / conda.


## pip

Notes:

Jamais `sudo`, toujours dans un `venv`.


## pyproject.toml

## pip install .

## Packager

```bash
pip install build
python -m build
```

### Publier

```bash
pip instqll twine
twine upload dist/*
```
