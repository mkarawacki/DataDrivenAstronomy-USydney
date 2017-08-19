# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:52:05 2017

@author: Mikołaj
"""

import numpy as np
def query(file):
  data=np.loadtxt(str(file),delimiter=',',usecols=(0,2))
  return data[data[:,1] > 1.0]


# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print (result)