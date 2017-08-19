import numpy as np
def median_bins(array,bins):
  array=np.asarray(array,float)
  binarray=np.zeros(bins)
  l=len(array)
  mean=np.mean(array)
  sigma=np.std(array)
  binwidth=2*sigma/bins
  minval=mean-sigma
  maxval=mean+sigma
  for i in range(0,len(binarray)-1):
    binarray[i]=np.size(np.where(((minval+i*binwidth <= array) & (array < minval+(i+1)*binwidth))))
    #print(i,minval+i*binwidth,minval+(i+1)*binwidth,binarray[i])
    #binarray[len(binarray)-1]=np.size(np.where((( minval> array))))
  histo=np.histogram(array,bins=bins,range=(minval,maxval))
  tab=histo[1]
  return (mean,sigma,np.count_nonzero((minval > array)),binarray)

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
  if N%2==1:
      k=(N+1)//2
      suma=below
      for i in range(0,bins):
          suma+=binarray[i]
          if(suma >= k):
              return (i+0.5)*binwidth+minval
  
  if N%2==0 :
      k=N//2
      suma=below
      for i in range(0,bins):
          suma+=binarray[i]
          if(suma>=k):
              return (i+2)*binwidth/2+minval
  



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