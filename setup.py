from setuptools import setup, find_packages

print find_packages()
packages = find_packages()
setup(
    version = "0.1",
    name = "django-host-settings",
    packages = packages,
    author = "Elijah Rutschman",
    author_email = "elijah@sandersnewmedia.com",
    description = "A small Django app for managing local settings files for multiple hosts",
    url = "https://github.com/sandersnewmedia/django-host-settings",
    include_package_data = True,
    zip_safe = False
)
