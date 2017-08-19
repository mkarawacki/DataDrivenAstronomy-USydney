# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:24:24 2017

@author: Mikołaj
"""

import numpy as np
import math
from operator import itemgetter
import collections
#from operator import itemgetter
def hms2dec(h,m,s):
  return 15*(h+m/60 + s/3600)
def dms2dec(d,m,s):
  if(d<0):
    dec= abs(d)+m/60 + s/3600
    return -1.0*dec
  else:
    dec=(d+m/60+s/3600)
    return dec

def import_bss():  
  cat1 = np.loadtxt('bss.dat', usecols=range(1, 7))
  lista=[]
  for i in range(0,len(cat1)):
    RA=hms2dec(cat1[i,0],cat1[i,1],cat1[i,2])
    Dec=dms2dec(cat1[i,3],cat1[i,4],cat1[i,5])
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

def import_super():
  cat2 = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  lista2=[]
  for i in range(0,len(cat2)):
    lista2.append((i+1,cat2[i][0],cat2[i][1]))
  return lista2

def crossmatch(bss,supercat,maxdist):
  matches=np.zeros(len(bss),dtype=('i4,i4,f10'))
  nomatches=[]
  
  for i in range(0,len(bss)):
    mdist=np.inf
    
    dist=np.inf*np.ones(len(supercat))
    for j in range (0,len(supercat)):
      dist[j]=angular_dist(bss[i][1],bss[i][2],supercat[j][1],supercat[j][2])
      
      if (dist[j]<maxdist):
          if(dist[j]<mdist):
           mdist=dist[j]
          k=np.argmin(dist)     
          matches[i]=(bss[i][0],supercat[k][0],dist[k])     
    #print [x for x, y in collections.Counter(matches[:][0]).items() if y > 1
     
  #items present in bss but not in matches  
  nomatches=[x[0] for x in bss if (x[0] not in [y[0] for y in matches])]
  matches_l=list(matches)
  matches_l=[x for x in matches_l if x[0]>0 ]
  matches_l=[tuple(i) for i in matches_l]
  return matches_l,nomatches

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40.0/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  
 # print(dist)
  #print(type(dist))
  #print(len(dist))
  print(type(matches[0]))
  print(len(matches))
  print(no_matches[:3])
  print(len(no_matches))
  # Second example in the question
  #max_dist = 5.0/3600
  #matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  #print(matches[:3])
  #print(len(matches))
  #print(no_matches[:3])
  #print(len(no_matches))