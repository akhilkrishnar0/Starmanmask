
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from astropy.io import fits
from astropy.table import Table

def plot_original_and_masked(fits_file, csv_file, save_mask=False, mask_name="masked.fits"):
    hdu = fits.open(fits_file)[0]
    data = hdu.data
    header = hdu.header

    tbl = Table.read(csv_file)
    ny, nx = data.shape
    yy, xx = np.mgrid[:ny, :nx]

    mask = np.zeros((ny, nx), dtype=bool)

    for r in tbl:
        x0, y0, a, b = r['x'], r['y'], r['a_pix'], r['b_pix']
        mask |= (((xx-x0)/a)**2 + ((yy-y0)/b)**2) <= 1

    masked = data.copy()
    masked[mask] = np.nan

    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    ax[0].imshow(data, origin='lower', cmap='gray')
    ax[1].imshow(masked, origin='lower', cmap='gray')

    for r in tbl:
        ax[0].add_patch(Ellipse((r['x'], r['y']), 2*r['a_pix'], 2*r['b_pix'],
                                edgecolor='red', facecolor='none'))

    plt.show()

    if save_mask:
        fits.PrimaryHDU(masked, header=header).writeto(mask_name, overwrite=True)

    return mask
