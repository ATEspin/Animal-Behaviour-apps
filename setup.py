#!/usr/bin/env python

from distutils.core import setup

setup(name='rat-apps',
      version = '0.1',
      author = 'Abel Torres-Espin, Callum Doolin',
      author_email = 'callum@resolvedinstruments.com',

      scripts = ['scripts/Xmaze.py'],

      install_requires = [
            'pyqtgraph',
            'numpy',
            'PyQt5',
            'opencv-python',
      ]

     )