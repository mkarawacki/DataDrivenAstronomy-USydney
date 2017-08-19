import numpy as np
import matplotlib.pyplot as plt
def median_bins(array,bins):
  array=np.asarray(array,float)
  binarray=np.zeros(bins)
  biny=np.zeros(bins)
  N=len(array)
  mean=np.mean(array)
  sigma=np.std(array)
  
  binwidth=2*sigma/bins
  #print('binwidth ',binwidth)
  minval=mean-sigma
  maxval=mean+sigma
  #print('minval',minval)
  #print('maxval',maxval)
  
  binno=0
  below=0
  for i in range(0,N):
    if(array[i]<minval):
      below+=1
    if(array[i]<maxval):
      binno=(int)((array[i]-minval)/binwidth)
      binarray[binno]+=1
  
  histo=np.histogram(array,bins=bins,range=(minval,maxval))
  #print('below ',below)
  #print('Binarray: ', binarray)
  #print('ilosc wartosci mniejszych niz minval ',np.count_nonzero((minval > array)))
  #plt.plot(histo[0])
  #plt.show()
  if N!=2:
   return (mean,sigma,below,np.asarray(histo[0],float))
  else:
      return (mean,sigma,below,binarray)
def median_approx(array,bins):
  suma=0  
  result=median_bins(array,bins)
  mean=result[0]
  sigma=result[1]
  below=result[2]
  binarray=result[3]
  binwidth=2*sigma/bins
  minval=mean-sigma
  maxval=mean+sigma
  N=len(array)
  suma=below
  if N%2==1:
   k=(N+1)/2
   
   for i in range(0,bins):
      suma+=binarray[i]
      if(suma >= k):
           return (i+0.5)*binwidth+minval
        
# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
  
  print(median_bins([0,1],5))
  
  print(median_approx([0,1],5))