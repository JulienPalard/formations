# Django Initiation

par

Julien Palard <julien@palard.fr>

https://mdk.fr

::: notes

Introduce yourself!


# Django

Django est une infrastructure d'applications web populaire et robuste.

> The web framework for perfectionists with deadlines.


## Django : qui l'utilise ?

- Instagram, Pineterest, Mozilla, Disqus, BitBucket, …

![](static/stats.png)


## Vocabulaire

Dans Django on va avoir principalement des `models`, des `vues`, des
`templates`, et des `urls`.


# Les bonnes bases : Python

On travaillera toujours dans un `venv` :

```python
python -m pip install django
```

# La théorie — Projet

Pour démarrer un projet, une commande :

```python
django-admin startproject project
```

## La théorie — App

Une fois dans le projet, pour créer une application, une commande :

```python
python manage.py startapp watch
```

::: notes

(et ajout dans `settings.py`)


## La théorie — Modèle

Un « modèle » est la description d'une table.

Ça rappelle un ORM, mais ça permet beaucoup plus de choses en Django.

::: notes

- admin
- forms
- serializers (API)
- class based views


## La théorie — Modèle

Par exemple :

```python
class Website(models.Model):
    host = models.CharField(max_length=512)
    is_up = models.BooleanField(null=True, blank=True)
    last_check = models.DateTimeField(auto_now_add=True)
```

::: notes

Prendre le temps d'expliquer les fields (leur relation avec la DB), et
les differents endroits ou Django peut reutiliser cette information
(widgets, validation, ...).


## La théorie — Première interface d'admin

En une ligne, pourquoi pas :

```python
admin.site.register(Website)
```

## La théorie — la DB

- PostgreSQL
- MySQL
- sqlite
- ...

::: notes

Leur faire croire 2 secondes qu'on va devoir s'installer et se
configurer un serveur de base de donnée :D


## La théorie — La DB

```bash
python manage.py makemigrations
python manage.py migrate
```

::: notes

On expliquera plus tard, leur dire que ça crée la DB et que le but
maintenant c'est surtout d'aller tester ça :)


## La théorie — L'interface d'administration

On a une DB, mais pas encore d'utilisateur admin dedans :

```bash
python manage.py createsuperuser
```

## La théorie — L'interface d'administration

On a terminé, on peut démarrer le serveur :

```bash
python manage.py runserver
```

# La pratique

```bash
django-admin startproject project
cd project
python manage.py startapp watch
```

::: notes

Biiien prendre le temps d'expliquer l'arborescence, de se promener,
d'y lire les commentaires.


## La pratique

Ajout de l'app `watch` dans `project/settings.py` :

```python
INSTALLED_APPS = [
    "watch",
    ...,
    ...,
]
```


## Les modèles

On va mettre celui-ci dans `watch/models.py`.

```python
class Website(models.Model):
    host = models.CharField(max_length=512)
    is_up = models.BooleanField(null=True, blank=True)
    last_check = models.DateTimeField(auto_now_add=True)
```


## Première interface d'admin

Et ça dans `watch/admin.py`.

```python
from watch.models import Website


admin.site.register(Website)
```


## Création de la DB

```bash
python manage.py makemigrations
python manage.py migrate
```

::: notes

Expliquer les deux étapes.


## Les modèles

Désambiguons `makemigrations` et `migrate` d'abord.


## L'interface d'administration

On a une DB, mais pas encore d'utilisateur admin dedans :

```bash
python manage.py createsuperuser
```

## L'interface d'administration

On a terminé, on peut essayer maintenant ?

```bash
python manage.py runserver
```
::: notes

Leur faire faire ça dans un **autre** shell.

puis les laisser jouer avec l'interface d'admin, créer quelques sites...


## L'interface d'administration

Les modèles, leurs `fields` ne servent donc pas qu'a l'ORM, cette
interface d'admin nous à demandé une ligne de code.

::: notes

Si ce n'est pas déjà fait, leur faire ajouter des `__str__`.


## Astuce

On peut passer beaucoup de temps à peaufiner l'interface d'admin,
repoussez ça après avoir livré une première version.


# Manipulation des modèles

## Mise en pratique

Créez le modèle `Check` avec les champs `is_up`, `date`, `website`, et
`message`.

::: notes

Pour le champ `website` vous aurez besoin d'un `models.ForeignKey`, RTFM.


## L'admin

Ajoutez une interface d'admin pour ce modèle, et ajoutez à la main quelques « *checks* ».

::: notes

Les faire tester ça.


# Les URLs & les vues

Changons complètement de sujet : les URLs et des vues.


## Les URLs

Dans `project/urls.py` on va se rajouter une URL pour la page d'accueil :

```python
from watch import views

urlpatterns = [
   ...
   ...
   path("", views.index, name="index"),
]
```

::: notes

C'est un `path`, un chemin, c'est le chemin vide.


## Les URLs

On aurait pu rajouter :

```python
path("about", views.about, name="about"),
path("help", views.help, name="help"),
...
```

## include

Petite parenthèse, on aurait pu mettre un `urlpatterns` dans
`watch/urls.py`, et les inclure dans `project/urls.py` en utilisant :

```python
from django.urls import include

[...]

path("", include("watch.urls")),
```

::: notes

C'est pratique pour « ancrer » un ensemble de chemin sous un autre
chemin : pour se faire une hierarchie.


## namespaces

Les espaces de nommage permettent de désambiguer les urls nommées :

`index` est le nom de la page d'accueil de l'interface d'admin de la
page d'accueil de votre application...


## namespaces

Avec les espaces de nommage, on a donc :

- `admin:index`
- `watch:index`

sans ambiguité.


## namespaces

À l'usage, dans les templates :

```html
{% url 'admin:index' %}
```

::: notes

Utilisez-en, c'est bien.


## Les vues

Dans `watch/views.py` :

```python
from django.http import HttpResponse


def index(request):
    html = "<html><body><h1>Website Watcher</h1></body></html>"
    return HttpResponse(html)
```


::: notes

C'est bien mais écrire du HTML dans du Python c'est pas élégant.


## Les vues

Mieux :

```python
from django.http import HttpResponse

def index(request):
    return render(request, "watch/index.html")
```

## Les templates

Django va chercher `watch/index.html` dans tous les dossiers de
templates, dont `watch/templates/`.


## Les templates

Donc dans `watch/templates/watch/index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8" />
    <title>Website Watch</title>
</head>
<body>
    <h1>Website Watch</h1>
</body>
</html>
```


## Les vues

Et si on ajoutais de la données provenant de la DB dans le template ?


## Les vues

```python
from django.http import HttpResponse

def index(request):
    return render(request, "watch/index.html", {"websites": Website.objects.all()})
```

::: notes

Premier apperçu de l'ORM en passant.


## Les vues

Digression :

Il existe aussi des vues basées sur des classes, pouvant s'appuyer sur
des modèles.


## Les vues

```python
class WebsiteListView(ListView):
    model = Website
```

## Les templates

```html
<body>
    <h1>Website Watch</h1>
    <ul>
    {% for website in websites %}
        <li>{{ website.host }} {% if website.is_up %}✓{% else %}✗{% endif %}</li>
    {% endfor %}
    </ul>
</body>
```


## Les templates

Ça fonctionne, mais on ne veux pas répéter l'entête HTML à chaque
page…


## Les templates — extends

En utilisant `extends`, on peut réutiliser des templates.


## La Debug Toolbar

![](https://raw.githubusercontent.com/django-debug-toolbar/django-debug-toolbar/master/example/django-debug-toolbar.png)


## La Debug Toolbar

```bash
python -m pip install django-debug-toolbar
```

L'ajouter dans `settings.py` et `urls.py`.


# L'ORM

## L'ORM

C'est l'occasion de sortir un `python manage.py shell`.

```pycon
>>> from watch.models import Website
>>> Website.objects.all()
```

Essayer `.all`, `.filter`, `.get`, `.order_by`, et les slices.


## Les *Managers*

Exposent les opérations de requête de base de donnée, c'est le `.objects`.

Ces opérations (des méthodes) renvoient des `queryset`s.

## Les *Queryset*

Introduction aux concepts Manager et Queryset, RelatedManager
Méthodes simples de requêtage en base de données


# Les tests
## Les fixtures

# Forms
## Forms fields
## Widgets
## ModelForm
## Validation

# Modèles
## Relations
## ForeignKey
## ManyToManyField
## OneToOneField
## InlineModeladmin

# Users
## Groups
## Permissions
## Authentication
How to protect views

# Static assets (day 3)
# Deployment
## gunicorn

# Bonus bonnes pratiques Python

La gestion des dépendances avec `pip-compile`.


## Bonus bonnes pratiques Python

Versionnez !!


## Bonnes pratiques

Prennez le temps de poser un `.gitignore`.


## Bonnes pratiques

On en mettra le moins possible dans le dossier du projet, on
utilisera des applications pour le reste du code.


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


## Resources

Pour Django on avait : https://ccbv.co.uk/ (Memo: « Classy Class-Based-View »).


# La configuration de Django

- `include local_settings.py`
- `django-configurations`
- `django-environ`
