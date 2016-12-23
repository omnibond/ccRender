import io
import os
from setuptools import setup
from setuptools import find_packages

# Encoding specification for PY3
with io.open('README.md', encoding='utf-8') as fp:
    description = fp.read()

# check and tweak version number
# can change author and email if necessary
setup(
    name='ccRender',
    # version number (will change later)
    version='0.6.1.dev1',
    # used own name and email, will change later if necessary
    author='Cliffton Hicks',
    author_email='cliffton@omnibond.com',
    license='LGPL',
    url='https://github.com/omnibond/ccRender',
    description='Cloud-based Blender rendering addon',
    long_description=description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Not sure if python programing language is necessary
        # will double check to make sure user uses latest python 3 version
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.5',
    ],
    py_modules=['ccrender'],
    packages=find_packages(exclude=['samples', 'tests']),
    install_requires=['scp'],
)
