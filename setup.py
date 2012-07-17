from setuptools import setup, find_packages

setup(
    name = "slider",
    version = "0.0.1",
    url = "https://github.com/h3/django-slider",
    license = "BSD",
    description = "A django application to create and manage an image slider ",
    author = 'Maxime haineault',
    packages = find_packages(),
    package_dir = {'': '.'},
    install_requires = [
        'easy-thumbnails',    
    ],
)
