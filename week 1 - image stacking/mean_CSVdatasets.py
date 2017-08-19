import numpy as np
def mean_datasets(filenames):
    data1st=np.loadtxt(filenames[0],delimiter=',')
    data=np.zeros(np.shape(data1st))
    for file in filenames:
      data=data+np.loadtxt(file,delimiter=',')
    return np.round(data/len(filenames),1)