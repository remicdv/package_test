from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    data_files=[("my_package",["./my_package/masterflat_sdssr_18_03_2024.fits"])],
    install_requires=['astropy'],  # Add dependencies if needed
)
