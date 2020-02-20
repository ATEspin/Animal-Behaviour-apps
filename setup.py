#!/usr/bin/env python

from distutils.core import setup

setup(name='Rat Apps',
      version = '0.4',
      author = 'Abel Torres-Espin, Callum Doolin',
      author_email = 'callum@resolvedinstruments.com',
      packages = ["ratapps"],

      entry_points = {
            'console_scripts': [
                  'Xmaze = ratapps.xmaze:main',
                  'Openfield = ratapps.openfield:main',
                  'Whitebox = ratapps.whitebox:main',
                  'SPGAnalysis = ratapps.spganalysis:main',
            ]
      },


      install_requires = [
            'pyqtgraph',
            'numpy',
            'PyQt5',
            'opencv-python-headless', 
            # headless version needed for pyinstaller to find correct
            # dlls on OSX.
      ]

     )