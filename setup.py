from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='snakebox',
    version='0.2.0',
    description='A super basic API wrapper for Baasbox',
    long_description=long_description,
    url='https://github.com/LeartS/snakebox',
    author='Leonardo Donelli',
    author_email='learts92@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='baasbox api wrapper',
    packages=['snakebox'],
    install_requires=['requests'],
)
