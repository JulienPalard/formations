# Le terminal et le shell

## Le vocabulaire

Expliquer le vocabulaire : shell, terminal, émulateur de terminal,
tout en autaurisant les abus de langages (si un élève parle de
terminal au lieu de shell ou vice-versa, aucun souci, on le fait
tous).

Pour le rôle du terminal, donner en exemple :

=> https://mdk.fr/blog/how-apt-does-its-fancy-progress-bar.html

Pour le rôle du shell, donner en exemple l'auto-complétion de bash.

Expliquer le vocabulaire *commande*, *programme*, *argument* :

C'est très flou, pour un débutant, que lorsqu'il tape `ls /`, `ls` est
un programme, `/` et un argument, je pense que dans les yeux du
débutant ce sont « deux trucs qui vont bien ensemble ». Pour
approfondir un peu plus on peut doucement discerner builtin et
programme.


## La philosophie Unix

### Write programs that do one thing and do it well.

Environ 3000 programmes différents dans mon dossier `/bin` sur une
Debian, heureusement leur utilisation suit une loi de Ziph :

    $ history | awk '{print $2}' | sort | uniq -c | sort -gr
    1088 git
    634 fg
    317 cd
    293 emacs
    239 ls
    201 python
    119 ssh
    113 flake8
    104 curl
    ...

L'idée ici est de réutiliser le code au maximum, un exemple typique :
la recherche dans un fichier.

Dans un contexte unix, un seul outil sert à chercher du texte dans un fichier : `grep`.

Dans les autres contextes, chaque programme ré-implémente à sa manière
le code nécessaire à la recherche de texte dans un fichier :

- Firefox
- Microsoft Word
- Chromium
- Thunderbird
- Microsoft Excel
- Libreoffice
- SublimeText
- Visual Studio Code

C'est de nombreuses heures de perdues, à réimplémenter inlassablement
la même fonctionalité.


### Write programs to work together.

Pour pouvoir réutiliser un programme il faut qu'il s'interface
correctement avec les autres :

- Un programme doit s'exprimer dans un dialecte compréhensible pour un autre.
- Un programme doit comprendre facilement le dialecte d'un autre.


### Write programs to handle text streams, because that is a universal interface.

Parler de l'omniprésence du texte brut (de Markdown à HTTP/1.1 en
passant par les fichiers source), en opposition aux formats binaires
(sortis d'éditeurs comme Word, ...).  (Je ne veux plus voir des
débutants ouvrir Microsoft Word pour taper leurs premières lignes de
code.)

Digrésser sur Markdown et reStructuredText, mentionner groff.


### Everything is a file.

Un disque dur est un fichier, une clef USB est un fichier, ma batterie
est un fichier, ma souris est un fichier...


### Philosophie UNIX

C'est le moment de commencer les démos et explications des commandes
élémentaires qui sont l'implémentation de la philosophie UNIX :

- pwd
- cd
- ls
- cp, mv
- rm (leur rappeler qu'il n'y a pas de « corbeille »)
- mkdir (et rmdir)
- less (leur apprendre à *q*uitter ! Rien n'est pas une évidence.)
- man (`man intro`, `man man`, `man ls`, `man cp`, ...)
- l'historique (`history`, pavé directionnel, ctrl-r, ça suffit pour le moment)
- grep
- find

Pour faire des exemples, on peut par exemple utiliser
[fr.openfoodfacts.org.products.csv](https://www.data.gouv.fr/fr/datasets/open-food-facts-produits-alimentaires-ingredients-nutrition-labels/#resource-164c9e57-32a7-4f5b-8891-26af10f91072).

```bash
$ wc -l fr.openfoodfacts.org.products.csv
1486053 fr.openfoodfacts.org.products.csv

$ file fr.openfoodfacts.org.products.csv
fr.openfoodfacts.org.products.csv: UTF-8 Unicode text, with very long lines

$ less fr.openfoodfacts.org.products.csv

$ head fr.openfoodfacts.org.products.csv
...

# Les noms des colonnes
$ head -n 1 fr.openfoodfacts.org.products.csv | tr '\t' '\n'

$ grep --color E431 fr.openfoodfacts.org.products.csv
...

$ grep --color E431 fr.openfoodfacts.org.products.csv  | wc -l
5

$ grep --color E100 fr.openfoodfacts.org.products.csv  | wc -l
5733

$ grep -oE 'E[0-9]{3}' fr.openfoodfacts.org.products.csv  |  sort | uniq -c | sort -gr | head
 167170 E322
 132029 E330
  79081 E500
  54024 E160
  50842 E415
  47528 E471
  44851 E450
  39896 E150
  39629 E202
  38945 E412

# Les marques les plus / les moins représentée
$ cut -f14 fr.openfoodfacts.org.products.csv | sort | uniq -c | sort -gr | head
 660855
  13160 Carrefour
  10902 Auchan

...
```

Ou faire quelques exemples simples, par exemple sur un fichier README
afficher les titres:

    grep '^#' README.md


## ssh

SSH: Parler de clefs, conseiller ED25519

```
eval $(ssh-agent -s)
ssh-add
```

Aborder les clefs physiques + Fido U2F


## sed, c'est bien



## dig, et comment fonctionne le DNS

```
# récupérer la zone root (et oui, il faut connaître un serveur root
# pour trouver un serveur root... les résolveurs DNS les connaissent
# en fait plus ou moins "tous", ils ne changent pas tous les matins.)
$ dig @198.41.0.4 . NS +norec

# Disons qu'on veut trouver la machine qui s'appelle `cr.yp.to` :
# Demander à un serveur root, c'est le seul qu'on connaît :
dig @192.5.5.241 cr.yp.to +norec
# Il nous donne une réponse contenant les NS de `to.`, ainsi que leurs IPs.

# On demande donc à un de ces NS la même question :
dig @216.74.32.101 cr.yp.to +norec
# Qui nous répond avec la liste des NS pour yp.to, ainsi que leurs IPs.

# On demande donc à un de ces NS la même question :
dig @131.193.32.108 cr.yp.to +norec
# Qui nous donne (enfin !) une réponse A (IPv4)

# Si quelqu'un demande pourquoi le NS de yp.to. à un nom à
# ralonge, c'est que c'est du CurveDNS (...de la crypto).
```

Parler des enregistrements TXT rapidement pendant qu'on y est.

Aussi du cache, pour démonter des préjugés comme "il faut forcément
attendre un temps fou après avoir configuré un enregistrement".

Parler des DNS menteurs, et de Google Chrome qui flood les racines en
tentant de détecter les DNS menteurs.


## curl, wget

Parler de HTTP/1.1, si possible leur faire une démo à la main, avec
l'IP récupérée précédement de cr.yp.to :

```
$ netcat 131.193.32.108 80
GET / HTTP/1.1
Host: cr.yp.to

```
```
HTTP/1.1 200 OK
```

Digrésser sur la sémantique HTTP.


## vim, emacs, nano

Donner en passant les raccourcis de base de bash et d'emacs :

- `ctrl-a` (début de ligne)
- `ctrl-e` (fin de ligne)
- `ctrl-z` (suspend, parler de `fg`, `bg`, `jobs`)
 - `ctrl-k` (kill-line)


## git

Clarifier rapidement git vs guthub : j'aime dire « git est à github ce
qu'un jpg est à dropbox » pour leur faire comprendre que git n'est
*pas* Github.

- Qu'est-ce qu'un commit, comment sont-ils rangés.
- Qu'est-ce qu'un remote, qu'est-ce qu'un clone, (et qu'est-ce qu'un fork ?).
- Qu'est-ce qu'une branche, qu'est-ce qu'un merge, qu'est-ce qu'un rebase.
- git bisect
- git grep


## apt install, pip install, ...

Peut être sans trop comparer avec une install sur Windows (chercher
sur Google, tomber sur un site louche, télécharger un malware), mais
tout de même, montrer la puissance de la chose :

    apt install vlc
    vlc cybersdf/

Parler du côté extrêmemnent controllé des paquets des distribs, en
opposition au côté extrêmement yolo des paquets des langages (npm,
pip, le typo squatting, supply-chain attacks, ...).


## rsync

On ne parle plus de `scp`, `scp` c'est finit, RIP.

Aborder rsnapshot si possible, digresser sur l'importance des
sauvegardes.


## L'encodage

Mettre en opposition "glyphe" (sur un coin de nappe en papier) et
"bits" (sur un disque ou par du cuivre), pour vite ammener au côté
nécessaire d'encoder d'un côté et de décoder de l'autre (pour le
transport, le stockage, ...).

Digresser sur le binaire, l'hexadécimal, leur rappeler les méthodes de
conversion au moins jusqu'a l'octet.

Digresser rapidement sur la logique booléenne :

  - 0 and x ?
  - 1 or x ?
  - not(a or b) == ?
  - (not a) or (not b)


Parler d'encodage de caractères, peut être en partant d'ASCII (pas
avant, ce n'est pas utile et ils ne retiendront pas tout), Unicode,
UTF-8, UTF-16, UTF-32, BE, LE, le BOM.

Quelques démos s'imposeront avec `iconv` et peut être Python.


# TODO

- Le système de fichiers
  - Les droits
  - Les montages
- Petit historique
- Les window-managers
- Sweet sweet thinks like youtube-dl
- crons / crontabs
- débugger (journalctl, /var/log)
- https://www.lopezferrando.com/30-interesting-shell-commands/
