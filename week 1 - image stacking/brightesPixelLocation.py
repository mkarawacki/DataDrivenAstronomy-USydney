# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:08:24 2017

@author: Mikołaj
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
def load_fits(filename):
  hdu=fits.open(filename)
  data=hdu[0].data
  return np.unravel_index(data.argmax(), data.shape)



if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image2.fits')
  print(bright)

  # You can also confirm your result visually:
  #from astropy.io import fits
  #

  #hdulist = fits.open('image1.fits')
  #data = hdulist[0].data

  # Plot the 2D image data
  #plt.imshow(data.T, cmap=plt.cm.viridis)
  #plt.colorbar()
  #plt.show()