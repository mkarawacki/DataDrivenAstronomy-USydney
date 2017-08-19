# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:03:11 2017

@author: Mikołaj
"""

fluxes = [17.3, 70.1, 22.3, 16.2, 20.7, 19.3]
fluxes.sort()
mid = len(fluxes)//2
median = (fluxes[mid - 1] + fluxes[mid])/2
print(median)