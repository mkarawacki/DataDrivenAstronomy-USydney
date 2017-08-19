# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:47:25 2017

@author: Mikołaj
"""

import numpy as np

def splitdata_train_test(data, fraction_training):
  # complete this function
  N=len(data)
  tr=int(N*fraction_training)
  training=data[:tr]
  testing=data[tr:]
  return training,testing
if __name__ == "__main__":
  data = np.load('galaxy_catalogue.npy')

  # set the fraction of data which should be in the training set
  fraction_training = 0.7

  # split the data using your function
  training, testing = splitdata_train_test(data, fraction_training)

  # print the key values
  print('Number data galaxies:', len(data))
  print('Train fraction:', fraction_training)
  print('Number of galaxies in training set:', len(training))
  print('Number of galaxies in testing set:', len(testing))