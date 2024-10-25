#!/usr/bin/env python3
import os
from setuptools import setup, find_packages


__version__ = None
my_directory = os.path.dirname(__file__)
exec(open(os.path.join(my_directory, 'cli_notes/version.py')).read())

console_scripts = [
    "notes = cli_notes.notes:main",
    ]


def parse_requirements(filename: str) -> list[str]:
    """
    Reads requirements.txt file into a list.
    Ignores 'FileNotFoundError's as we can be in the
    wrong directory due to multiple __init__.py files.
    """
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


setup(
    name='cli_notes',
    description="CLI Note taking package",
    author='Daniel McIntyre',
    author_email='danielmcintyre56@gmail.com',
    python_requires='>=3.10.6',
    packages=find_packages(),
    version=__version__,
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': console_scripts,
    },
)
