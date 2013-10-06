from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='dev.svetlyak.ru',
    version=version,
    description='http://dev.svetlyak.ru blog.',
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='blog site',
    author='Alexander Artemenko',
    author_email='svetlyak.40wt@gmail.com',
    url='http://github.com/svetlyak40wt/dev.svetlyak.ru',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
)

