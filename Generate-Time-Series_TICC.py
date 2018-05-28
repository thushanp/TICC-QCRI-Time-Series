# -*- coding: utf-8 -*-
"""
Created on Sun May 20 09:31:35 2018

@author: Vignesh
"""

import numpy as np
from TICC_solver import TICC
import sys

from matplotlib import pyplot
from pandas import Series 
n = 300
limit_low = 0
limit_high = 0.48

#my_data = np.sin(np.linspace(0,5*np.pi,n))**2
'''my_data = np.sin(np.linspace(0.5*np.pi,n))**2 - np.sin(np.linspace(0.8*np.pi,n))**2 + np.sin()
scaling = (limit_high - limit_low)/(max(my_data)- min(my_data))
my_data = my_data * scaling
my_data = my_data + (limit_low - min(my_data))
#num = int( my_data.shape)
x = np.arange(0,n/2)
print(my_data)
print(my_data.shape)
print(x)
print(x.shape)
pyplot.plot(x, my_data)
pyplot.show()
'''

#Alternative version.
s = (5,n)
y = np.zeros(s)
x1  = np.linspace(0,0.5*np.pi*n,n)
x2 = np.random.ranf(8000)
#print(x1)
y[0,]=y1 = float(np.sin(x1) + np.sin(x1-1+ 0.5*np.pi)**2 - np.sin(x1*2+np.pi)) #+ np.sin(np.log(x1))
y[1,]=y2 = float(np.cos(x1) + np.cos(x1-2+ 0.9*np.pi)**2 - np.cos(x1*3+np.pi)) #+ np.sin(np.log(x1))
y[2,]=y3 = float(np.sin(x1) + np.sin(x1-8+ 0.2*np.pi)**2- np.sin(x1+np.pi)) #+ np.sin(np.log(x1))
y[3,]=y4 = float(np.cos(x1) + np.cos(x1-4+ 0.6*np.pi)**2 - np.cos(x1*4+np.pi)) #+ np.sin(np.log(x1))
y[4,]=y5 = float(np.sin(x1) + np.sin(x1-9+ 0.4*np.pi)**2- np.sin(x1*6+np.pi)) #+ np.sin(np.log(x1))
y0 = np.abs(np.random.normal(0,3.14,n))
#print (y2)

yz = y1+y2+y3+y4+y5+y0
for i in range(0,5):
   pyplot.plot(y[i]+y0)
#y[1,]
#i=0
ctr = 0
x = np.zeros(n)
f,a = pyplot.subplots(3,2)
for i in range (0,n):
        x[i] = i 
    
a[0,0].plot(x,y[0]+y0)
a[0,1].plot(x,y[1]+y0)
a[1,0].plot(x,y[2]+y0)
a[1,1].plot(x,y[3]+y0)
a[2,0].plot(x,y[4]+y0)

#pyplot.plot(yz)
#print(np.size(yz))
#print(np.size(x))
#pyplot.scatter()
fig, a = pyplot.subplots(3,2)
a[0,0].scatter(x,y[0]+y0)
a[0,1].scatter(x,y[1]+y0)
a[1,0].scatter(x,y[2]+y0)
a[1,1].scatter(x,y[3]+y0)
a[2,0].scatter(x,y[4]+y0)
#pyplot.bar(x,yz)

np.savetxt("Syn_TimeSeries2.csv",np.transpose([y[0,],y[1,],y[2,],y[3,],y[4,]]),delimiter = ',')
#np.savetxt('test.csv', x, delimiter=',')
''' Time Series using Pandas,'''
if __name__ == '__main__':
    fname = "Syn_TimeSeries2.csv"
    ticc = TICC(window_size=1, number_of_clusters=2, lambda_parameter=11e-2, beta=600, maxIters=1000, threshold=2e-5,
                 write_out_file=False, prefix_string="output_folder/", num_proc=1)
    (cluster_assignment, cluster_MRFs) = ticc.fit(input_file=fname)
    
    print(cluster_assignment)
    #np.savetxt('Results2.txt', cluster_assignment, fmt='%d', delimiter=',')
    np.savetxt('Results_SynData.csv', cluster_assignment, fmt='%d', delimiter=',')
    #print(np.size(cluster_assignment))
