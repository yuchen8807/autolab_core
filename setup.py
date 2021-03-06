"""
Setup of core python codebase
Author: Jeff Mahler
"""
from setuptools import setup

requirements = [
    'numpy',
    'scipy',
    'matplotlib',
    'pyyaml',
    'multiprocess',
    'setproctitle',
    'joblib'
]

setup(name='autolab_core',
      version='0.1.0',
      description='AutoLab core utilites code',
      author='Jeff Mahler',
      author_email='jmahler@berkeley.edu',
      package_dir = {'': '.'},
      packages=['autolab_core'],
      install_requires=requirements,
      test_suite='test'
     )

