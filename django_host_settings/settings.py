
from django_host_settings import get_local_settings_module

LOCAL_SETTINGS_MODULE = get_local_settings_module()

try:
    # import the configuration settings file
    config_module = __import__('config.%s' % LOCAL_SETTINGS_MODULE, globals(), locals(), 'foo')

    # Load the config settings properties into the local scope.
    for setting in dir(config_module):
        if setting == setting.upper():
            locals()[setting] = getattr(config_module, setting)
except ImportError:
    pass
