#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='crowsource',
      version='1.0',
      description='PSF Photometry',
      author='Eddie Schlafly',
      author_email='eschlafly@gmail.com',
      url='https://github.com/dnidever/crowdsource',
#      scripts=['bin/dopfit','bin/dopjointfit','bin/doppler'],
      requires=['numpy','astropy','scipy'],
#      include_package_data=True,
)
