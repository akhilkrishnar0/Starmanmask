
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.widgets import EllipseSelector
from astropy.io import fits
from astropy.wcs import WCS
from astropy.table import Table

class GalaxyAnnotator:
    def __init__(self, fits_file):
        self.ellipses = []
        self.data, self.wcs = self.load_fits(fits_file)

        self.fig, self.ax = plt.subplots(subplot_kw={'projection': self.wcs})
        self.ax.imshow(self.data, origin='lower', cmap='gray',
                       vmin=np.percentile(self.data, 5),
                       vmax=np.percentile(self.data, 99))
        self.ax.set_title("Click+drag to draw ellipses. Press 'q' to save & quit")

        self.selector = EllipseSelector(self.ax, self.on_select,
                                        interactive=True, useblit=True)

        self.cid = self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        plt.show()

    def load_fits(self, filename):
        hdu = fits.open(filename)[0]
        return hdu.data, WCS(hdu.header)

    def on_select(self, eclick, erelease):
        x = (eclick.xdata + erelease.xdata) / 2
        y = (eclick.ydata + erelease.ydata) / 2
        a = abs(erelease.xdata - eclick.xdata) / 2
        b = abs(erelease.ydata - eclick.ydata) / 2

        ell = Ellipse((x, y), 2*a, 2*b, edgecolor='red',
                      facecolor='none', lw=2)
        self.ax.add_patch(ell)
        self.fig.canvas.draw()

        self.ellipses.append((x, y, a, b, 0))

    def on_key(self, event):
        if event.key == 'q':
            self.save()
            self.selector.disconnect_events()
            self.fig.canvas.mpl_disconnect(self.cid)
            plt.close(self.fig)

    def save(self):
        tbl = Table(rows=self.ellipses,
                    names=('x', 'y', 'a_pix', 'b_pix', 'theta'))
        tbl.write("galaxy_ellipses.csv", overwrite=True)
