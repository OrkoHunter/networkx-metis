#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from glob import glob
import os
import sys

from setuptools import setup, Extension
from Cython.Build import cythonize

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

if sys.version_info[:2] < (2, 7):
    print('networkx-metis requires Python version 2.7 or later (%d.%d detected).' %
          sys.version_info[:2])
    sys.exit(-1)

libraries = [
    ('gklib', {'sources': glob('src/GKlib/*.c') + glob('src/GKlib/*.cc'),
               'depends': glob('src/GKlib/*.h'),
               'include_dirs': ['src/GKlib']}),
    ('metis', {'sources': glob('src/libmetis/*.c') + glob('src/libmetis/*.cc'),
               'depends': glob('src/libmetis/*.h'),
               'include_dirs': ['src/GKlib', 'src/libmetis']})]

ext_modules = cythonize([Extension('networkx.addons.metis._metis', ['*.pyx'],
                                   include_dirs=['src/GKlib', 'src/libmetis'],
                                   libraries=['metis', 'gklib'])])

install_requires = ['decorator', 'six']

if sys.version_info[:2] < (3, 4):
    install_requires.append('enum34')

if __name__ == "__main__":

    setup(
        name               = 'networkx-metis',
        version            = '1.0',
        maintainer         = 'NetworkX Developers',
        maintainer_email   = 'networkx-discuss@googlegroups.com',
        description        = 'NetworkX Addon to allow graph partitioning with METIS',
        keywords           = ['Networks', 'Graph Theory', 'Mathematics',
                              'network', 'graph', 'math', 'graph partitioning'],
        classifiers        = ['Development Status :: 5 - Production/Stable',
                              'Intended Audience :: Developers',
                              'Intended Audience :: Science/Research',
                              'License :: OSI Approved :: Apache License Version 2',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python :: 2',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3',
                              'Programming Language :: Python :: 3.2',
                              'Programming Language :: Python :: 3.3',
                              'Programming Language :: Python :: 3.4',],
        packages           = ['networkx.addons.metis', 'networkx.addons', 'networkx'],
        namespace_packages = ['networkx.addons.metis', 'networkx.addons', 'networkx'],
        libraries          = libraries,
        ext_modules        = ext_modules,
        install_requires   = install_requires
    )
