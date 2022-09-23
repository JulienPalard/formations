# The slides I use while teaching

Each directory contains a Makefile that builds the slides using
[mdtoreveal](https://pypi.org/project/mdtoreveal/).

Each directory is also uploaded to mdk.fr:

- https://mdk.fr/python-initiation
- https://mdk.fr/python-avancé
- https://mdk.fr/drf-initiation
- https://mdk.fr/django-initiation
- https://mdk.fr/python-perfs
- https://mdk.fr/git-initiation


## TODO

- http://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial
- `*` peut être vu comme de l'unpacking vers des noms qu'on ne voit pas.
- Ajouter une slide sur "jamais de \ en fin de ligne", il y a toujours
  un moyen plus lisible.
- https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html Why numbering should start at zero
- Les imports
- with statement


## Notes

Les arguments par defaut conservés peuvent service de memoizer:

    def fib(x, memo={}):
        ...

**Aucune** fonction n'est montée avant le 3, (à part des méthodes sur
les types natifs).

Souci : Jour 1 pytest nécessite Jour 2 pip...


# La suite du programme avancé


- Packaging
 - cookiecutter : docs/, tests/, README, setup.cfg, setup.py, ...

- Multiprocessing / Multithreading / Asyncio
 - IO Bound vs CPU Bound
 - Locks vs Queues

- Code quality
- import this, explicit is better
 - sémantique : les ternaires, les listes en compréhension, sont des
   expressions, elles doivent être utilisées comme des expressions,
   pas comme des instructions.
 - TDD
 - pas de print, logging FTW.
 - pas de "logging tiers", personne ne connaît, on reste sur `logging`.
 - -Xdev
 - black, ..., pass
 - pytest, doctest
 - pytest-cov
 - hypothesis
 - flake8
 - flake8-bugbear
 - tox
 - mypy
 - black
 - pdb, breakpoint()
 - EAFP, LBYL

- Performance
 - Les types natifs : Leur complexité algorithmique
 - Cython
 - pypy
 - cffi
 - cprofile / pstats

- Libs
 - re
 - argparse
 - pathlib
 - logging
 - numpy
 - jupyter

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Ce(tte) œuvre est mise à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Licence Creative Commons Attribution 4.0 International</a>.

# DRF

Side project : https://github.com/JulienPalard/drf-demos

- Revue des bases et consolidation Python et Django
- Présentation des types d'API, approfondissement de REST/HATEOAS
- Rappels autour de la sémantique HTTP
- django-rest-framework: La sérialisation
- django-rest-framework: Les différents types de vues
- django-rest-framework: Les permissions
- django-rest-framework: Les relations
- Les tests et la maintenabilité


# Objectifs pédagogiques

- Pouvoir démarrer rapidement un projet DRF.
- Savoir designer une API.
- Implémenter un service headless en utilisant DRF.


# TP

- Projet 1 : API « Horloge parlante ».
- Projet 2 : API « memcached ».
- Projet 3 : API « file system ».
- Projet 4 : API « uptime manager ».


# Formation Initiation Linux (2 jours)

Cette formation est destinée à toute personne souhaitant utiliser
Linux, pour du développement, de l'administration système, ou pour un
usage quotidien.


## Stagiaires

Maximum 5 par sessions, pour commencer, peut monter à 7.


## Pré-requis

Aucun.


## Objectifs pédagogiques

- Pouvoir utiliser une machine sous Linux au quotidien.
- Être à l'aise avec les interfaces en ligne de commande.
- Savoir installer et utiliser des logiciels.
- Manipuler des fichiers, des données.


## Plan

### Jour 1

- Présentation de l'environnement Linux.
- Maniement de l'émulateur de terminal.
- Approche des commandes classiques :
  - `man`, `cd`, `ls`, `pwd`, `mv`, `cp`, `rm`, `less`, …
- Installer, désinstaller des applications depuis le gestionnaire de paquets.


### Jour 2

- L'accès à l'extérieur avec `ssh`, `rsync`, `curl`, et gestion des sauvegardes.
- Introduction à la gestion de sources en utilisant `git`.
- Manipulation de données en utilisant `awk`, `sed`, `grep`, `find`.
- L'édition de texte depuis un terminal en utilisant `emacs`.
- Approche du système de fichier : les droits, la sécurité, `mount`.
