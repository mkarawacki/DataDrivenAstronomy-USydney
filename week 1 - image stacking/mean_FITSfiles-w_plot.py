# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:18:43 2017

@author: Mikołaj
"""

# Write your mean_fits function here:
import numpy as np
from astropy.io import fits
def mean_fits(fitsfiles):
  hdulist = fits.open(fitsfiles[0])
  data = hdulist[0].data
  data=np.zeros(np.shape(data))
  for file in fitsfiles:
    hdulist=fits.open(file)
    data=data+hdulist[0].data
  
  return data/len(fitsfiles)



if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()