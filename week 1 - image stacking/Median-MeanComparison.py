# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 22:04:25 2017

@author: Mikołaj
"""

import numpy as np
def list_stats(vec):
  l=len(vec)
  mid=l//2
  vec.sort()
  if l%2==0:
    median = (vec[mid - 1] + vec[mid])/2
  if l%2==1 and l!=1:
    median = vec[mid]
  if l==1:
    median=vec[0]
  return (median,sum(vec)/len(vec))



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)