# Django tabbed admin2

Fork of old Django tabbed admin
https://github.com/omji/django-tabbed-admin

*******
Install
*******

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

From PyPi

```bash
pip install django_tabbed_admin2
```
From Github

.. code-block::  shell-session

    https://github.com/omji/django-tabbed-admin#egg=tabbed_admin


# setup


Simply add the app in your installed apps list in settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'django_tabbed_admin2'
        ...
    )

Django-tabbed-admin by default requires Jquery UI tabs plugin in order to work. It is packaged with the static files required to make it funcitonnal, however, they are not activated by default to avoid a conflict with other libraries.

In order to activate the Jquery UI statics, add the following line to the project settings:

.. code-block::  python

    TABBED_ADMIN_USE_JQUERY_UI = True


# Configure admin tabs

In order to add tabs to a model admin, it should inherit from tabbed_admin.TabbedModelAdmin and contain a tabs attribute.
The tab attribute configuration tries to remain similar to the fieldsets and inlines setup logic.

Basically, a tuple can be created for each tab exactely the same way as for fieldsets, except that inlines can be added anywhere in between.

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

Then each tuple have to be passed to a *tabs* attribute prefixed by the verbose name to display within the tab:

```  python
tabs = [
    ('Overview', tab_overview),
    ('Albums', tab_album)
]
```


A full example would give:

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

# Configure tabs dynamically


Be warned that the tabs will completely reset the fieldsets and inlines attributes in order to avoid conflicts during the form saving. Both attributes are overwritten with the entries passed to the tabs attribute. For the same reasons, it is highly recommanded not to overwrite get_fieldsets or get_inlines.

You can pass and modify the tabs dynamically the same way you would do for fieldsets or inlines.

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

# Change the jquery ui


You can change the jquery ui css and js by either overriding the media in the
admin class

```python

    class Media:
        css = {
            'all': ('css/jquery-ui.theme.min.css',)
        }
```

or by changing the the following settings,

`TABBED_ADMIN_JQUERY_UI_CSS` and `TABBED_ADMIN_JQUERY_UI_JS`

```python

    TABBED_ADMIN_JQUERY_UI_CSS = 'static/css/my-custom-jquery-ui.css'
    TABBED_ADMIN_JQUERY_UI_JS = 'static/js/my-custom-jquery-ui.js'
```

# Contribution


Please feel free to contribute. Any help and advices are much appreciated.
You will find an example application to run and develop the library easily.


# LINKS

Development:
    https://github.com/4Sigma/django-tabbed-admin

Package:


