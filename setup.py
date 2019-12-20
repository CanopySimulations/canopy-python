# coding: utf-8

"""
    Canopy API

    Combination of generated code from Open API definitions, and useful helper functions.
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "canopy-api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
    "pandas>=0.25.1",
    "numpy"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Canopy API",
    author_email="james.thurley@canopysimulations.com",
    url="https://www.canopysimulations.com/",
    keywords=["Canopy API", "Canopy Simulations"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Combination of generated code from Open API definitions, and useful helper functions.
    """
)
