# -*- coding: utf-8 -*-
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup
setup(name='brainfuck',
      description='Interpreter and REPL for brainfuck',
      author='Ashish Prasad (codemaniac)',
      author_email='ashish.ap.rao@gmail.com',
      version='0.1.0',
      scripts=['brainfuck'],
      install_requires=['argparse'],
      license = "BSD",
      keywords = "brainfuck interpreter REPL"
)
