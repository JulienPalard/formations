# L'encodage

## Les octets d'abord

```python
>>> bytes([0x01, 0x02]) == b"\x01\x02"
True
```

Notes:

Notez qu'en hexadecimal, deux symboles permet de représenter
exactement 8 bits, donc exactement un octet.


## ASCII

Notes:

1960, 7 bits ("a word", qu'on a traduit "un octet"), [0; 127]

Seul la moitié des octets sont donc de l'ASCII valide.

Exercice: Utiliser `range()` et `bytes([i])` pour afficher la table ascii.


## Latin-1

Notes:

1985, 8 bits, [0; 255]

Couvre environ 32 langues.

Quasi complet pour le francais, il manque juste le Œ, le œ (le
francais qui s'en est occupé n'était pas linguiste.)


Exercice: Utiliser `range()` et `bytes([i])` pour afficher la table latin-1.


## Unicode

Notes:

~1990, d'abord sur 16 bits, aujourd'hui c'est juste une base de donnée.

Couvre environ 150 langues (environ toutes).

Calque latin1 de 0 à 255, même C0 (controles bien définis) et C1 (controles
ignorés, de 0x80 à 0x9F).


## encoder, décoder

- `str.encode` → `bytes`
- `bytes.decode` → `str`
