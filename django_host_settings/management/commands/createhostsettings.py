from django.core.management.base import BaseCommand, CommandError
from django_host_settings import get_local_settings_module
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Creates a host settings file'

    def handle(self, *args, **options):
        module_name = get_local_settings_module()
        module_path = os.path.join(settings.PROJECT_ROOT, 'config',
                                   '%s.py' % module_name)
        if os.path.exists(module_path):
            raise CommandError('%s already exists, nothing to do' % module_path)
        try:
            with open(module_path, 'w+b') as f:
                f.write('DEBUG = True\n')
        except Exception as e:
            raise CommandError('Error writing to %s: %s' % (module_path, str(e)))

        self.stdout.write('Wrote local settings to %s\n' % module_path)
