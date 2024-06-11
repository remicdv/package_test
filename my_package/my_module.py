from astropy.io import fits
import os

def hello_world():
    print("Hello, world!")

def print_fits_info():
    with fits.open(os.path.abspath('./my_package/masterflat_sdssr_18_03_2024.fits')) as hdul:
        hdul.info()
