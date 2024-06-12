from astropy.io import fits
from pathlib import Path
from importlib import metadata
from my_package import my_module

def list_files():
    path_f = Path(my_module.__file__)
    path = Path(path_f.parent.absolute().as_posix()+'-'+metadata.version('my_package')+'.data/data/my_package')
    for child in path.iterdir(): print(child.name)

def hello_world():
    print("Hello, world!")

def print_fits_info():
    with fits.open(os.path.abspath('./my_package/masterflat_sdssr_18_03_2024.fits')) as hdul:
        hdul.info()
