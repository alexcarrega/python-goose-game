import os
from setuptools import setup

def read(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
   name = "python-goose-game",
   author = "Alex Carrega",
   author_email = "contact@alexcarrega.com",
   description = "The Goose Game Kata",
   license = "MIT",
   keywords = "game goose python",
   url = "http://www.github.com/alexcarrega/python-goose-game",
   long_description=read('../README.md'),
   classifiers = [
      "Development Status :: 5 - Production/Stable",
      "Topic :: Games",
      "License :: OSI Approved :: MIT License",
   ],
   version = '1.0.0',
   install_requires=['colorful', 'cmd2']
)
