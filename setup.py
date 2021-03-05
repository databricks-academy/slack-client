import setuptools
from setuptools import find_packages

setuptools.setup(
    name="slack-client",
    version="1.0.0",
    packages=find_packages(),
    package_dir={'': 'python'}
)
