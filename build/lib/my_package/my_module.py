def hello_world():
    print("Hello, world!")

from astropy.io import fits

def print_fits_info():
    with fits.open('./my_package/masterflat_sdssr_18_03_2024.fits') as hdul:
        hdul.info()
