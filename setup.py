#!usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="welding",
    version="0.0.1",
    description="Welding professional inference.",
    url="https://github.com/Swall0w/welding_inference",
    install_requires=['numpy', 'chainer', 'scikit-image', 'imageio'],
    license=license,
    packages=find_packages(exclude=('tests')),
    test_suite='tests',
    entry_points="""
    [console_scripts]
    pig = pig.pig:main
    """,
    )
