from codecs import open
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()


setup(
  name='fplib',
  version='1.0.0',
  description='Functional programming goodies for Python 3.6+',
  long_description=long_description,
  author='Pablo Pedemonte',
  author_email='ppedemon@ar.ibm.com',
  url='http://github.ibm.com/ppedemon/fplib',
  license='Apache-2.0',
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  packages=find_packages()
)
