# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 00:23:46 2017

@author: Mikołaj
"""

import numpy as np
from astropy.io import fits
import time
def median_fits(files):
  l=len(files)
  dx=np.shape(fits.open(files[0])[0].data)[0]
  dy=np.shape(fits.open(files[0])[0].data)[1]
  #db=np.zeros(len(files),dx,dy)
  trio=(l,dx,dy)
  
  db=np.zeros(trio)
  #print(trio)
  i=0
  start=time.perf_counter()
  for file in files:
    db[i]=fits.open(file)[0].data
    i=i+1
  m=np.median(db,axis=0)
  
  memsize=l*dx*dy*8/1024
  stop=time.perf_counter()-start
  return (m,stop,memsize)    
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])