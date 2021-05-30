# DRF Initiation

par

Julien Palard <julien@palard.fr>

https://mdk.fr

::: notes

Introduce yourself!

# Les bonnes bases : Python

`*args, **kwargs`


## Les bonnes bases : Python

La MRO.


## Les bonnes bases : Python

On travaille dans un venv.


## Les bonnes bases : Python

La gestion des dépendances avec `pip-compile`.


## Pratique

Rédiger un script, en ligne de commande, permettant de tester si un
site internet est en bonne santé :

```bash
$ python checkurl.py mdk.fr
Redirection HTTPS: OK
Status: OK (200)
Response time: OK (0.125s < 1s)
Certificate: OK (expires in 68 days)
HSTS: OK (max-age=63072000; always)
```

::: notes

versionnez !


## Les bonnes bases : Django

```bash
python -m pip install Django
django-admin startproject demo
cd demo
./manage.py migrate
```

::: notes

Leur faire faire le tour du propriétaire.


## Vocabulaire

Dans Django on va avoir des `models`, des `vues`, et des `urls`.

::: notes

Peut être aussi des templates, et l'admin.


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


## Bonnes pratiques

On versionne et on prend le temps de poser un `.gitignore`.


## Bonnes pratiques

On en mettra le moins possible dans le dossier du projet, on
utilisera des applications pour le reste du code.


## Bonnes pratiques

Une bonne gestion des dépendances avec `pip-tools`.


## Bonnes pratiques

On surcharge l'objet `User`, même si on pense ne pas en avoir besoin :

```python
class User(django.contrib.auth.models.AbstractUser):
    ...
```

et :

```python
AUTH_USER_MODEL = ...
```

## Les URLs

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]
```

## Les vues

```python
def index(request):
    return HttpResponse("Hello world")
```

## Pratique

Faire une page d'accueil pour votre Django.


## Les modèles

Désambiguons `makemigrations` et `migrate` d'abord.


## Les modèles

Personalisez le modèle `User` :

```python
class User(django.contrib.auth.models.AbstractUser):
    ...
```

## Les modèles

Créez un modèle `Domain` :

```python
class Domain(models.Model):
    domain = models.CharField(max_length=253)
    is_up = models.BooleanField(null=True, blank=True)
```

## L'admin

Indiquez l'existance du modèle domaine à l'admin :

```python
admin.site.register(Domain)
```

## Testez

## Les bonnes bases : DRF

```bash
python -m pip install djangorestframework
 # Ajouter l'app rest_framework
```


##  vocabulaire

Dans DRF on va avoir des `serializers`, des `routers`, des `views` et des `permissions`.


## Le routage de Django

La requête parcourre les `urlpatterns` du projet, c'est donc à lui
d'inclure les `urlpatterns` des différentes applications.


## Resources

Pour Django on avait : https://ccbv.co.uk/ (Memo: « Classy Class-Based-View »).

Pour DRF on a : https://www.cdrf.co/ (Memo: « Classy DRF »).


## Les media types

Pour représenter des données on utilise un *media type* il existe
plusieurs écoles :

- Tout est liste (`Collection+JSON`, ...).
- Tout est article (`atom+xml`, ...).
- Snowflakes (`application/json`).

(On ne parle donc pas de RPC, on parle de **représentation**).


## Les media types

Certains *media type* sont plus « tout terrain » que d'autres :

- `JSON-LD`, avec Hydra : le plus générique.
- `HAL` : Pour la lecture seule.
- `application/problem+json`
- `application/json-patch+json`
- `application/json-home`
- ...

::: notes

Pensez au web actuel : il mélange text/html, application/javascript, text/css, ...


# Mais qu'est-ce que REST ?

C'est un ensemble de contraintes :

- Client-Serveur
- Sans état
- Une URI identifie une resource
- Les resources sont manipulées via leurs représentations
- ...

::: notes

Pensez au web actuel pour chaque contrainte : ça marche.


## Client-Serveur

✓


## Sans état

Attention à l'interprétation : on ne parle pas d'un site statique pour autant.

Le serveur a un état, et cet état est amené à changer (un `PUT`, un
`POST`, un `DELETE` vont typiquement changer quelque chose).


## Sans état

Quand on dit « *stateless* » on pense au niveau d'une requête :

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

::: notes

Si le serveur a oublié la première requête quand elle arrive, pas de souci.

Si les deux requêtes sont gérées par des serveurs différents, pas de souci.


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

::: notes

Faire une parenthèse sur les etags, `If-Match`, `If-None-Match`.


## Messages auto-descriptifs

Toutes les informations nécessaires à l'interprétation du message
doivent être dans le message.

Je n'ai rien contre un lien vers la doc.


## HATEOAS

C'est celui qui fait peur.

TL;DR: data + interactions

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
      "@id": "/cart/",
      "@type": "hydra/CreateResourceOperation",
      "method": "POST",
      "expects": {"@id": "/products/123"}
    }
}
```

::: notes

Ce n'est pas vraiment du JSON-LD+Hydra, mais ça loge das la slide...

## HATEOAS

> support on building Hypermedia APIs with REST framework is planned for a future version.


## En parlant de sémantique HTTP

TL;DR

## GET / HEAD / OPTIONS

- `safe`
- `idempotent`

## PUT

- `idempotent`

## DELETE

- `idempotent`

## POST

# La configuration de Django

## Trois solutions

- `include local_settings.py`
- `django-configurations`
- `django-environ`

# Et si on revenait à DRF !?

## Les serialiseurs

Leur rôle est de transformer un objet Python en un objet Python
facilement sérialisable (en JSON typiquement).

Il va donc, par exemple transformer objet datetime en chaîne, puisque
JSON ne spécifie pas de représentation pour les dates.

::: notes

Et vice versa.


## Les URLs

Pour commencer : aucune différence avec Django.


## Les vues

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello(request):
    return Response({"Hello": "world."})
```
