# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:54:17 2017

@author: Mikołaj
"""

import numpy as np
import numpy.lib.recfunctions as rfn
def query(file1,file2):
  stars=np.loadtxt(str(file1),delimiter=',',usecols=(0,2),dtype=[('kepler_id', int), ('st_radius', float)])
  planets=np.loadtxt(str(file2),delimiter=',',usecols=(0,5),dtype=[('kepler_id', int), ('pl_radius', float)])
  #a=np.array(data[data[:,1] > 1.0])
  #b=np.argsort(a)
  #print(a[b])
  #return a[np.argsort(a[:, 1])]
  lista=[]
  for s in range(0,len(stars)):
    for p in range (0,len(planets)):
      if stars[s][0]==planets[p][0] and stars[s][1]>1.0:
        lista.append(planets[p][1]/stars[s][1])
  #print (stars)
  #print(planets)
  #join=np.array(rfn.join_by('kepler_id', stars, planets, jointype='inner', usemask=False))
  #print (join,len(join))
  a=np.array(lista)
  #a=np.array(a[a[:,0] > 1.0])
  a=a[np.argsort(a)]
  #print(a)
  return a.reshape(len(a),1)
# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')