# coding: utf-8

"""
    Canopy API

    Combination of generated code from Open API definitions, and useful helper functions.
"""

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

from setuptools import setup, find_packages  # noqa: H301

with open('README.md') as f:
    long_description = f.read()

NAME = "canopy-client"
VERSION = "0.0.1"

REQUIRES = [
    "numpy",
    "certifi>=2017.4.17",
    "six>=1.10",
    "python-dateutil>=2.1",
    "urllib3>=1.23",
    "pandas>=0.25.1"
]

setup(
    name=NAME,
    packages=find_packages(),
    version=VERSION,
    license='MIT',
    description="Python Client for the Canopy Simulation API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='James Thurley',
    author_email="james.thurley@canopysimulations.com",
    url="https://github.com/canopysimulations/canopy-python/",
    keywords=["Canopy API", "Canopy Simulations", "Canopy Client"],
    install_requires=REQUIRES,
    #include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
