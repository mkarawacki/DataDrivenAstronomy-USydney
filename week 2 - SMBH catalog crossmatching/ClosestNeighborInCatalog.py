# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 09:31:05 2017

@author: Mikołaj
"""

import numpy as np
import math
from operator import itemgetter
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
def angular_dist(r1,d1,r2,d2):
  r1_rad=np.radians(r1)
  d1_rad=np.radians(d1)
  r2_rad=np.radians(r2)
  d2_rad=np.radians(d2)
  a = math.pow(np.sin(abs(d1_rad-d2_rad)/2.0),2)
  b=np.cos(d1_rad)*np.cos(d2_rad)*math.pow(np.sin(abs(r1_rad-r2_rad)/2.0),2)
  distance=2*np.arcsin(np.sqrt(a+b))
  dist_deg=np.degrees(distance)
  return dist_deg
def find_closest(cat,RA,Dec):
  l=len(cat)
  lista=[]
  for i in range(0,l):
    lista.append((cat[i][0],angular_dist(RA,Dec,cat[i][1],cat[i][2])))
  return sorted(lista,key=itemgetter(1))[0]
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))
  #find_closest(cat, 175.3, -32.5)
  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))