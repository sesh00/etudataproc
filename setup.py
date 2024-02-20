from io import open
from setuptools import setup

version = '0.1.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='etudataproc',
    version=version,

    author='sesh00',
    author_email='ernestrsage@gmail.ru',

    description=(
        u'Python library for interacting with a Yandex DataProc Queue'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/sesh00/etudataproc',
    download_url='https://github.com/sesh00/etudataproc/archive/main.zip'.format(
        version
    ),

    license='MIT License, see LICENSE file',

    packages=['etudataproc'],
    install_requires=['requests'],

    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
