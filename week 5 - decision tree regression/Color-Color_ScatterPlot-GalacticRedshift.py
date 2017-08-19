# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:43:31 2017

@author: Mikołaj
"""

import numpy as np
from matplotlib import pyplot as plt

# Complete the following to make the plot
if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')
    
    # Define our colour indexes u-g and r-i
    ug=data['u']-data['g']
    ri = data['r']-data['i']
    # Make a redshift array
    z=data['redshift']
    # Create the plot with plt.scatter and plt.colorbar
    sc=plt.scatter(ug,ri,s=2,lw=0,c=z,vmin=0, cmap=cmap)
    plt.colorbar(sc)
    # Define your axis labels and plot title
    plt.ylabel('Colour index r-i')
    plt.xlabel('Colour index u-g')
    plt.title('Redshift (colour) u-g versus r-i')
    
    # Set any axis limits
    plt.xlim((-0.5,2.5))
    plt.ylim((-0.5,1))
    plt.show()