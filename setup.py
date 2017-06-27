import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'nose2',
    'cov-core'
]

setup(
    name='validex',
    version='0.0',
    description='A simple field validation library.',
    long_description=README + '\n\n' + CHANGES,
    author='Konrad R.K. Ludwig',
    author_email='konrad.rk.ludwig@gmail.com',
    url='http://www.konradrkludwig.com/',
    packages=find_packages(),
    install_requires=requires
)
