#!/usr/bin/env python

"""The setup script"""


import pathlib

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    INSTALL_REQUIRES = f.read().strip().split("\n")

LONG_DESCRIPTION = pathlib.Path("README.md").read_text()
PYTHON_REQUIRES = ">=3.7"

description = "carbonplan python project template"

setup(
    name="carbonplan-project",
    description=description,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    maintainer="Raphael Hagen",
    maintainer_email="raphael@carbonplan.org",
    url="https://github.com/carbonplan/python-project-template",
    packages=find_packages(),
    include_package_data=True,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    license="MIT",
    keywords="carbon, data, climate",
    use_scm_version={"version_scheme": "post-release", "local_scheme": "dirty-tag"},
)
