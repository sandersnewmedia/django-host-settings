from django.core.management.base import BaseCommand, CommandError
from django_host_settings import get_local_settings_module
import os

class Command(BaseCommand):
    args = ''
    help = 'Creates a host settings file'
    can_import_settings = True

    def handle(self, *args, **options):
        from django.conf import settings
        module_name = get_local_settings_module()
        module_path = os.path.abspath(os.path.join(settings.PROJECT_ROOT, '..',
                                      'config', '%s.py' % module_name))

        if os.path.exists(module_path):
            raise CommandError('%s already exists, nothing to do' % module_path)

        try:
            try:
                dirname = os.path.dirname(module_path)
                os.makedirs(dirname)
                with open(os.path.join(dirname, '__init__.py'), 'w') as f:
                    f.write('')
            except:
                pass
            with open(module_path, 'w+b') as f:
                f.write('DEBUG = True\n')
        except Exception as e:
            raise CommandError('Error writing to %s: %s' % (module_path, str(e)))

        self.stdout.write('Wrote local settings to %s\n' % module_path)
