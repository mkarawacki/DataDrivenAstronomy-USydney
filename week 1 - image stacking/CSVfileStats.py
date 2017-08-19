import numpy as np
# Write your calc_stats function here.
def calc_stats(datafile):
  ### loadtxt solution
  data=np.loadtxt(datafile,delimiter=',')
  #print(data)
  
  ### loop solution
  #data=[]
  #for line in open(datafile):
  #  data.append(line.strip().split(','))
    
  #data=np.asarray(data,float)
  
  return (np.round(np.mean(data),1),np.round(np.median(data),1))
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data2.csv')
  print(mean)