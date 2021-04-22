# DRF Initiation


par

Julien Palard <julien@palard.fr>

https://mdk.fr

::: notes

Introduce yourself!


## Les bonnes bases

On travaille dans un venv.

```bash
python -m pip install djangorestframework
django-admin startproject drfdemo
cd drfdemo
# Ajouter l'app rest_framework
./manage.py migrate
```


## Debug toolbar

```bash
python -m pip install django-debug-toolbar
```

L'ajouter dans `settings.py` et `urls.py`.


## Un compte administrateur

```bash
./manage.py createsuperuser
```

Vous devez maintenant avoir une interface d'administration qui
fonctionne, avec la Debug Toolbar à droite.


## Pause bonnes pratiques

- On versionne, on prend le temps de poser un `.gitignore`.
- On renomme l'app `app`, sinon c'est ambigu.
- On en mettra le moins possible dans `app/`, on utilisera des
  applications pour le reste du code.


## Pause vocabulaire

Dans Django on va avoir des `models`, des `urls`, et l'`admin`.

Dans DRF on va avoir des `serializers`, des `routers`, des `views` et des `permissions`.


## Pause resources

Pour Django on avait : https://ccbv.co.uk/ (Memo: « Classy Class-Based-View »)

Pour DRF on a : https://www.cdrf.co/ (Memo: « Classy DRF »)


## Les media types

Pour représenter des données il existe plusieurs écoles :

- Tout est liste (`Collection+JSON`, ...)
- Tout est article (`atom+xml`, ...)
- Tout est fonction (`RPC`)
- REST incluant HATEOAS
- Snowflakes
- ...


# Mais qu'est-ce que REST ?

C'est un ensemble de contraintes :

- Client-Serveur
- Sans état
- Coopérant avec les caches intermédiaires
- Interface uniforme
  - Une URI identifie une resource
  - Les resources sont manipulées via leurs représentations
  - Messages auto-descriptifs
  - HATEOAS


## Client-Serveur

✓


## Sans état

Attention à l'interprétation : le serveur a bien sûr un état, et cet
état est amené à changer (un `PUT`, un `POST`, un `DELETE` vont
typiquement changer quelque chose).


## Sans état

Quand on dit « *stateless* » on le dit au niveau d'une requête :

> L'interprétation d'une requête ne doit **pas** dépendre des requêtes précédentes.

C'est tout.

::: notes

Prendre l'exemple du client qui s'endort, puis qui revient 8h plus
tard pour terminer. Ou de plusieurs backends derrière un LB.


## Sans état

Donc pas de :

```text
PUT /workon/user/1
PUT /user -d '{"name": "Alan"}'
PUT /workon/user/2
PUT /user -d '{"name": "Ada"}'
```

## Sans état

Mais :

```text
PUT /users/1 -d '{"name": "Alan"}'
PUT /users/2 -d '{"name": "Ada"}'
```


## Coopération avec les caches intermédiaires

C'est surtout respecter la sémantique HTTP.

Avec HTTPS les problèmes causés par des proxy inconnus, éventuellement
ne respectant pas la sémantique HTTP ont disparu.


::: notes

Attention, certains réseaux, de fait, ne respectent pas la sémantique
HTTP : un POST pourraît être exceptionnellement rejoué, sur un réseau
mobile, lors du roaming.


## Une URI identifie une resource

> Cool URIs don't change.

REST ne nous impose pas des URL sémantiques / expressives.

Cependant les humains les apprécient, une URL bien choisie c'est comme
un nom de variable bien choisi, c'est agréable.

::: notes

La slide n'en parle pas mais bien en parler:
- Une URI == une resource.
- Une resource == une URI.


## Manipulation par la représentation

```text
GET /users/1
{"name": "Alan", "birthdate": "1912-06-23"}
PUT /users/1 -d '{"name": "Alan Turing", "birthdate": "1912-06-23"}'
```

## Messages auto-descriptifs

Toutes les informations nécessaires à l'interprétation du message
doivent être dans le message, je n'ai rien contre un lien vers la doc.


## HATEOAS

C'est celui qui fait peur.

::: notes

Prendre l'exemple d'une boutique avec le bouton "acheter" qui n'est
présent que s'il y a du stock.


## HATEOAS

Le mauvais exemple :

```json
{
    "@id": "/products/123",
    "name": "Brioche",
    "in_stock": false,
    "buy": {
      "@id": "/cart/"
      "@type": "hydra/CreateResourceOperation",
      "method": "POST",
      "expects": {"@id": "/products/123"}
    }
}
```

::: notes

Ce n'est pas vraiment du JSON-LD+Hydra, mais ça loge das la slide...