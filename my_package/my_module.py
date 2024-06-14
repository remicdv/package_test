from astropy.io import fits
from pathlib import Path
from importlib import metadata
from my_package import my_module

base_url_data = Path(Path(my_module.__file__).parent.absolute().as_posix()+'-'+metadata.version('my_package')+'.data/data/my_package')

def list_files():
    return [file.name for file in base_url_data.iterdir()]

def get_file(filename):
    file_url = base_url_data / filename
    with fits.open(file_url.absolute().as_posix()) as hdul:
        hdul.info()

def hello_world():
    print("Hello, world!")

def print_fits_info():
    with fits.open(os.path.abspath('./my_package/masterflat_sdssr_18_03_2024.fits')) as hdul:
        hdul.info()
