# Django Tabbed Admin2

This is a fork of the old Django tabbed admin, available at [omji/django-tabbed-admin](https://github.com/omji/django-tabbed-admin).

## Installation

It is strongly recommended to install this theme from Git using PIP in your project's virtual environment.

### From PyPi

```bash
pip install django_tabbed_admin2
```

### From GitHub

```shell-session
https://github.com/omji/django-tabbed-admin#egg=tabbed_admin
```

## Setup

Simply add the app to your list of installed apps in `settings.py`.

```python
INSTALLED_APPS = (
    ...
    'django_tabbed_admin2',
    ...
)
```

Django-tabbed-admin, by default, requires the Jquery UI tabs plugin to work. It is packaged with the static files required for functionality, but they are not activated by default to avoid conflicts with other libraries.

To activate the Jquery UI statics, add the following line to the project settings:

```python
TABBED_ADMIN_USE_JQUERY_UI = True
```

## Configure Admin Tabs

To add tabs to a model admin, it should inherit from `tabbed_admin.TabbedModelAdmin` and contain a `tabs` attribute. The `tabs` attribute configuration is similar to the `fieldsets` and `inlines` setup logic.

A tuple can be created for each tab in the same way as for `fieldsets`, except that `inlines` can be added anywhere in between.

```python
tab_overview = (
    (None, {
        'fields': ('name', 'bio', 'style')
    }),
    MusicianInline,
    ('Contact', {
        'fields': ('agent', 'phone', 'email')
    })
)
```

Then each tuple has to be passed to a `tabs` attribute prefixed by the verbose name to display within the tab:

```python
tabs = [
    ('Overview', tab_overview),
    ('Albums', tab_album)
]
```

A full example would be:

```python
from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from .models import Band, Musician, Album

class MusicianInline(admin.StackedInline):
    model = Musician
    extra = 1

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1

@admin.register(Band)
class BandAdmin(TabbedModelAdmin):
    model = Band

    tab_overview = (
        (None, {
            'fields': ('name', 'bio', 'style')
        }),
        MusicianInline,
        ('Contact', {
            'fields': ('agent', 'phone', 'email')
        })
    )
    tab_album = (
        AlbumInline,
    )
    tabs = [
        ('Overview', tab_overview),
        ('Albums', tab_album)
    ]
```

## Configure Tabs Dynamically

Be warned that the tabs will completely reset the `fieldsets` and `inlines` attributes to avoid conflicts during form saving. Both attributes are overwritten with the entries passed to the `tabs` attribute. For the same reasons, it is highly recommended not to overwrite `get_fieldsets` or `get_inlines`.

You can pass and modify the tabs dynamically the same way you would do for `fieldsets` or `inlines`.

```python
def get_tabs(self, request, obj=None):
    tabs = self.tabs
    if obj is not None:
        tab_overview = self.tab_overview + ('Social', {
            'fields': ('website', 'twitter', 'facebook')
        })
        tab_ressources = self.tab_ressources + (InterviewInline, )
        tabs = [
            ('Overview', tab_overview),
            ('Ressources', tab_ressources)
        ]
    self.tabs = tabs
    return super(BandAdmin, self).get_tabs(request, obj)
```

## Change the Jquery UI

You can change the Jquery UI CSS and JS by either overriding the media in the admin class:

```python
class Media:
    css = {
        'all': ('css/jquery-ui.theme.min.css',)
    }
```

or by changing the following settings, `TABBED_ADMIN_JQUERY_UI_CSS` and `TABBED_ADMIN_JQUERY_UI_JS`:

```python
TABBED_ADMIN_JQUERY_UI_CSS = 'static/css/my-custom-jquery-ui.css'
TABBED_ADMIN_JQUERY_UI_JS = 'static/js/my-custom-jquery-ui.js'
```

## Contribution

Please feel free to contribute. Any help and advice are much appreciated. You will find an example application to run and develop the library easily.

## Links

- Development: [https://github.com/4Sigma/django-tabbed-admin](https://github.com/4Sigma/django-tabbed-admin)
