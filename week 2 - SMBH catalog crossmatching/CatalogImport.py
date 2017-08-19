# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 08:59:05 2017

@author: Mikołaj
"""

import numpy as np
def hms2dec(h,m,s):
  return 15*(h+m/60 + s/3600)
def dms2dec(d,m,s):
  sign=1
  if(d<0):
    dec= abs(d)+m/60 + s/3600
    return -1.0*dec
  else:
    dec=(d+m/60+s/3600)
    return dec

def import_bss():  
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  lista=[]
  for i in range(0,len(cat)):
    RA=hms2dec(cat[i,0],cat[i,1],cat[i,2])
    Dec=dms2dec(cat[i,3],cat[i,4],cat[i,5])
    lista.append((i+1,RA,Dec))
  return lista  
def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  lista=[]
  for i in range(0,len(cat)):
    lista.append((i+1,cat[i][0],cat[i][1]))
  return lista


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)