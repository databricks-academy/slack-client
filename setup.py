import setuptools
from setuptools import find_packages

setuptools.setup(
    name="slack-client",
    version="1.0.2",
    packages=["slack_client"],
    package_dir={'': 'python'}
)
