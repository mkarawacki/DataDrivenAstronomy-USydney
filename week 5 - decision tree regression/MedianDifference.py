# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 21:15:57 2017

@author: Mikołaj
"""

import numpy as np

# write a function that calculates the median of the differences
# between our predicted and actual values
def median_diff(predicted, actual):
  #pass
  return np.median(abs(predicted-actual))

if __name__ == "__main__":
  # load testing data
  targets = np.load('targets.npy')
  predictions = np.load('predictions.npy')

  # call your function to measure the accuracy of the predictions
  diff = median_diff(predictions, targets)

  # print the median difference
  print("Median difference: {:0.3f}".format(diff))