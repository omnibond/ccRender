import io
import os
from setuptools import setup

# Encoding specification for PY3
with io.open('README.md', encoding='utf-8') as fp:
    description = fp.read()

# check and tweak version number
# can change author and email if necessary
setup(
    name = 'ccRender',
    version = '0.6.1.dev1',
    author = 'Cliffton Hicks',
    author_email = 'cliffton@omnibond.com',
    license = 'LGPL',
    url = 'https://github.com/omnibond/ccRender',
    description = 'Cloud-based Blender rendering addon',
    long_description = description,
    classifiers = [
        'Development Status :: 3 - Alpha',
        # 'Programming Language :: Python :: 3.5',
    ],
    install_requires = ['scp'],
)
