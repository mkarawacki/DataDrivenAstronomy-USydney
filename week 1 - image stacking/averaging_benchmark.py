# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 22:02:04 2017

@author: Mikołaj
"""

import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  # the time to generate the random array should not be included
  
  timing=[]
  # modify this function to time func with ntrials times using a new random array each time
  for i in range(0,ntrials):
    
    data = np.random.rand(size)
    start=time.perf_counter()
    res = func(data)
    end=time.perf_counter()-start
    timing.append(end)
  #print(len(timing))
  # return the average run time
  timing=np.asarray(timing,float)
  return np.mean(timing)

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))