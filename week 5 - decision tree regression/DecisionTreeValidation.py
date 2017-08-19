# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 22:43:45 2017

@author: Mikołaj
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor

# paste your get_features_targets function here
def get_features_targets(data):
  # complete this function
  features=np.zeros((data.shape[0],4))
  features[:, 0] = data['u'] - data['g']
  features[:, 1] = data['g'] - data['r']
  features[:, 2] = data['r'] - data['i']
  features[:, 3] = data['i'] - data['z']
  targets=data['redshift']
  #pass
  return features,targets

# paste your median_diff function here
def median_diff(predicted, actual):
  #pass
  return np.median(abs(predicted-actual))

# write a function that splits the data into training and testing subsets
# trains the model and returns the prediction accuracy with median_diff
def validate_model(model, features, targets):
  # split the data into training and testing features and predictions
  N = len(features)
  Ntrain=int(3*N/4)
  train_features = features[:Ntrain]
  train_targets = targets[:Ntrain]
  test_features = features[Ntrain:]
  test_targets = targets[Ntrain:]
  # train the model
  dtr=DecisionTreeRegressor()
  dtr.fit(train_features,train_targets)
  # initialize model
  #dtr = DecisionTreeRegressor()
  # train the model
  predictions=dtr.predict(test_features)
  # get the predicted_redshifts
  
  # use median_diff function to calculate the accuracy
  return median_diff(test_targets, predictions)


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model
  dtr = DecisionTreeRegressor()
  #print(int(3*len(features)/4))
  # validate the model and print the med_diff
  diff = validate_model(dtr, features, targets)
  print('Median difference: {:f}'.format(diff))