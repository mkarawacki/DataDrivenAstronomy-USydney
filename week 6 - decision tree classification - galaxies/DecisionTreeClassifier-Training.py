# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:07:37 2017

@author: Mikołaj
"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier


# copy your splitdata_train_test function here
def splitdata_train_test(data, fraction_training):
  N=len(data)
  tr=int(N*fraction_training)
  training=data[:tr]
  testing=data[tr:]
  return training,testing

# copy your generate_features_targets function here
def generate_features_targets(data):
  # complete the function by calculating the concentrations

  targets = data['class']

  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']

  # fill the remaining 3 columns with concentrations in the u, r and z filters
  # concentration in u filter
  features[:, 10] = data['petroR50_u'] / data['petroR90_u']
  # concentration in r filter
  features[:, 11] = data['petroR50_r'] / data['petroR90_r']
  # concentration in z filter
  features[:, 12] = data['petroR50_z'] / data['petroR90_z']

  return features, targets


# complete this function by splitting the data set and training a decision tree classifier
def dtc_predict_actual(data):
  # split the data into training and testing sets using a training fraction of 0.7
  fraction_training = 0.7
  # split the data using your function
  #shuffling data for randomness
  np.random.seed(0)
  np.random.shuffle(data)
  training, testing = splitdata_train_test(data, fraction_training)
  # generate the feature and targets for the training and test sets
  # i.e. train_features, train_targets, test_features, test_targets
  features, targets = generate_features_targets(data)
  Ntrain=int(len(data)*0.7)
  train_features = features[:Ntrain]
  train_targets = targets[:Ntrain]
  test_features = features[Ntrain:]
  test_targets = targets[Ntrain:]

  # instantiate a decision tree classifier
  dtc = DecisionTreeClassifier()
  # train the classifier with the train_features and train_targets
  dtc.fit(train_features,train_targets)
  # get predictions for the test_features
  predictions_test=dtc.predict(test_features)
  # return the predictions and the test_targets
  return predictions_test,test_targets


if __name__ == '__main__':
  data = np.load('galaxy_catalogue.npy')
    
  predicted_class, actual_class = dtc_predict_actual(data)

  # Print some of the initial results
  print("Some initial results...\n   predicted,  actual")
  for i in range(10):
    print("{}. {}, {}".format(i, predicted_class[i], actual_class[i]))