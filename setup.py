import io
import os
from setuptools import setup
from setuptools import find_packages

# Encoding specification for PY3
with io.open('README.rst', encoding='utf-8') as fp:
    description = fp.read()

# check and tweak version number
# can change author and email if necessary
setup(
    name='ccRender',
    # version number (will change later)
    version='0.10.0.a2',
    # used own name and email, will change later if necessary
    author='Cliffton Hicks',
    author_email='cliffton@omnibond.com',
    license='LGPL',
    url='https://github.com/omnibond/ccRender',
    description='Cloud-based Blender rendering addon',
    long_description=description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Due to version of python Blender uses,
        # only the current Python version is supported.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    py_modules=['ccrender'],
    packages=find_packages(exclude=['samples', 'tests']),
    install_requires=['scp', 'pyperclip'],
)
