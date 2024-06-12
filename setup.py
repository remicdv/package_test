from setuptools import setup, find_packages
from glob import glob

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    data_files=[("my_package",glob('./my_package/data/*'))],
    install_requires=['astropy'],  # Add dependencies if needed
)
