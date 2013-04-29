from __future__ import print_function

from glob import glob

try:
    from setuptools import setup
except ImportError:
    print("Falling back to distutils. Functionality may be limited.")
    from distutils.core import setup

requires = [ 'lxml', 'requests', 'cssselect' ]
long_description = open('README.rst').read() + "\n\n" + open("ChangeLog").read()

config = {
    'name'            : 'startupnorth-jobs-notifiaction',
    'description'     : 'Scrape jobs.startupnorth.ca and create a nice text-base email.',
    'long_description': long_description,
    'author'          : 'Brandon Sandrowicz',
    'author_email'    : 'brandon@sandrowicz.org',
    'url'             : 'https://github.com/bsandrow/startupnorth-jobs',
    'version'         : '0.1',
    'scripts'         : glob('bin/*'),
    'install_requires': requires,
    'license'         : open('LICENSE').read(),
}

setup(**config)
