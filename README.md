[django-host-settings](http://github.com/sandersnewmedia/django-host-settings)
================================================================================

Overview
--------
django-host-settings is a small Django app which lets you easily manage settings for your development machines & servers.

Installation
------------

    $ git clone git://github.com/sandersnewmedia/django-host-settings.git
    $ cd django-host-settings
    $ python setup.py install

Usage
-----
In your settings.py:

    INSTALLED_APPS = (
        ...
        'django_host_settings'
    )

Then run these commands:

    $ python manage.py createhostsettings
    $ echo "\n\nfrom django_host_settings.settings import *" > settings.py

You can now override any settings in your own settings file, created in the config/ directory.
