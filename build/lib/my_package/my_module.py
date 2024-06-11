def hello_world():
    print("Hello, world!")

from astropy.io import fits

def print_fits_info():
    fits_image_filename = fits.util.get_testdata_filepath('masterflat_sdssr_18_03_2024.fits')

    hdul = fits.open(fits_image_filename)

    hdul.info()

    hdul.close()
