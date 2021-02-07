#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='loancalc',
      version='0.0.1',
      description='Python loan calculator',
      author='Dvornikov Victor',
      author_email='spacefuryphonk@gmail.com',
      url='https://github.com/lydiym/loancalc',
      packages=find_packages(),
      install_requires=[
          'dateutils==0.6.12'
      ],
      )
