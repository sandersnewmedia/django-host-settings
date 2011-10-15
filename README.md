[django-host-settings](http://github.com/sandersnewmedia/django-host-settings)
================================================================================

Overview
--------
django-host-settings is a Django app which helps you create and load settings unique to each host running your Django project.

Installation
------------

    $ easy_install django-host-settings

or

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
    $ echo "import os" >> settings.py
    $ echo "PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))" >> settings.py
    $ echo "from django_host_settings.settings import *" >> settings.py
    
You can now override any settings in your own settings file, created in the `config/` directory of your project's root.

For instance, if your hostname is `sir-robin`, the `createhostsettings` command will create a file, `config/sir_robin.py` that you could define Django settings in, such as `DEBUG = True`.  These settings will be loaded along with, and override, the settings defined in `settings.py`.