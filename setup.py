#!/usr/bin/env python3
import os

from setuptools import find_packages, setup


def exec_file(path_segments):
    """Execute a single python file to get the variables defined in it"""
    result = {}
    code = read_file(path_segments)
    exec(code, result)
    return result


def read_file(path_segments):
    """Read a file from the package. Takes a list of strings to join to
    make the path"""
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *path_segments)
    with open(file_path) as f:
        return f.read()


long_description = read_file(("README.md",))


setup(
    name="signets",
    version='0.2.0',
    description="Un robot qui vous veut du bien",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.0",
        "towhee>=1.1.3",
        "pymilvus>=2.5.0",
        "numpy>=2.0.1",
     ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
