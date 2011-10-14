
def get_local_settings_module():
    from socket import gethostname
    import re
    non_word_re = re.compile('[^\w]')
    # get a filename-safe version of the system's hostname
    return non_word_re.sub('_', gethostname())
