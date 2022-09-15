# TODO

Lors de la présentation des fonctions natives dans un REPL, il y a une
ambiguité (`print` vs `return`):

    >>> int("42")
    42
    >>> print("42")
    42

On pourrait passer par une variable peut-être :

    >>> quarante_deux = int("42")
    >>> quarante_deux
    42

    >>> result = print("42")
    42
    >>> print(result)
    None
