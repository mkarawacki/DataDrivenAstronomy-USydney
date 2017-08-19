# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:08:40 2017

@author: Mikołaj
"""

import numpy as np
import math
def binapprox(array,bins):
    N=np.size(array)
    mean=np.mean(array)
    sigma=np.std(array)
    binarray=np.zeros(bins)
    maxval=mean+sigma
    minval=mean-sigma
    binwidth=(2*sigma)/bins
    submin=0
    binno=0
    for i in range(0,N):
        if(array[i]<minval):
            submin+=1
        elif(array[i]<maxval):
            binno=(int)((array[i]-minval)/binwidth)
            binarray[binno]+=1
    #print('N ', N)
    #print('mean ',mean)
    #print('stddev ',sigma)
    #print('maxval ',maxval)
    #print('minval ',minval)
    #print('binwidth',binwidth)
    #print('submin',submin)
    #print(binarray)
    if(bins==4):
        histo=np.histogram(array,bins=bins,range=(minval,maxval))
        binarray=np.asarray(histo[0],float) 
    count=submin
    #print('N nieparzyste')
    k=(N+1)/2
    print(k)
    stop=0
    for i in range(0,bins):
        while(count<k):
            count+=binarray[i]
            if(count>=k):
                stop=i
                break
    return (stop+0.5)*binwidth+minval
#==============================================================================
#         if(count >= k):
#             j=i
#             while(count==k):
#                 j+=1
#                 count+=binarray[j]
#                 
#             return (i+j+1)*binwidth/2 + minval
#==============================================================================
    #return (mean,sigma,submin,binarray)

data=[0,1]
data1=[1, 5, 7, 7, 3, 6, 1, 1]
bins=5
bins1=4
data2=[1, 1, 3, 2, 2, 6]
bins2=3
print(binapprox(data1,bins1))
print(binapprox(data2,bins2))
print(binapprox(data,bins))
