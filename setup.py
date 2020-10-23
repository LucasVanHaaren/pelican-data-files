from setuptools import setup, find_packages

# versioning is handled by bumpversion
__version__ = '0.0.1'

def get_file(filename):
    with open(filename) as f:
        return f.read()

setup(
    name='pelican-data-files',
    description="Pelican plugin that allows to load data from files like JSON or YAML",
    url='https://github.com/LucasVanHaaren/pelican-data-files',
    author='vhash',
    author_email='29121316+LucasVanHaaren@users.noreply.github.com',
    keywords='pelican, pelican-plugin, data',
    version=__version__,
    long_description=get_file('README.md'),
    license=get_file('LICENSE'),
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'pelican>=4.5'
    ],
    extras_require={
        'dev': [
            'bumpversion',
            'flake8',
            'black'
        ]
    }
)
