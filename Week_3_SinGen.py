# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:26:04 2018

@author: Vignesh
Week#3.1: Creating a sine wave of different frequency.  
Week#3.2: Visualizing the cluster arrangement
"""
import numpy as np
import math
from matplotlib import pyplot
import csv 
import pandas as pd
import sys
from TICC_solver import TICC
import time
'''

n = 400
x1 = np.linspace(0,n*(np.pi/180),100)
x2 = np.linspace(0,2*n*(np.pi/180),100)
print(x1)
fig, (ax1,ax2,ax3) = pyplot.subplots(3,1)
ax1.plot(np.sin(x1))
ax2.plot(np.sin(x2))
#y = np.sin(x1)
#pyplot.plot(y)

x = np.zeros(1000)
for i in range(0,1000):
    if(i<360):
        x[i] = np.sin(i*3*(np.pi/180)) + 1
    elif((i>360) & (i<720)):
        x[i] = np.sin(i*8*(np.pi/180)) + 1
    else:
        x[i] = (np.sin(i*5*(np.pi/180))) + 1
ax3.plot(x)

#np.savetxt('Week3_Mixed_Freq_Wave.csv', x, delimiter=',')
np.savetxt("Week3_Mixed_Freq_Wave.csv",np.transpose([x,x]),delimiter = ',')
'''
window_size = 20
number_of_clusters= 3
lambda_parameter=0.09
beta=0
maxIters=100


if __name__ == '__main__':
    start_time = time.time()    
    fname = "Week3_Mixed_Freq_Wave.csv"
    s = (np.size(fname))
    x = np.zeros(s)
    i = 0
    bic = 0
    #print(fname)
    ticc = TICC(window_size, number_of_clusters, lambda_parameter, beta, maxIters, threshold=2e-5, write_out_file=False, prefix_string="output_folder/", num_proc=1)
    (cluster_assignment, cluster_MRFs, bic) = ticc.fit(input_file=fname)
    #print(type(cluster_assignment))
    #print(fname)
    
    x,y,z,x1,y1,clus_assign = [],[],[],[],[],[]
    ctr = 0
    with open('Week3_Mixed_Freq_Wave.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x.append(row[0])
            y.append(row[1])
    
    
    x = np.array(list(x))
    y = np.array(list(y))
    
    s1 = np.size(x)
    s2 = np.size(y)
    j = 0
    
    s3 = np.size(cluster_assignment)
    '''for i in range(0,100):
        x1[i] = x[j] 
        j+=10
    print(x1)
   '''
    k = 0
    clus_assign = np.zeros(s1)
    for i in range(0,s1):
        clus_assign[i] = cluster_assignment[k]
        ctr+=1
        if(ctr == window_size):
            k+=1
            ctr = 0
    df = pd.DataFrame({'Sensor 1:':x,'Sensor 2':y,'Cluster Assignment':clus_assign })
    #print("Printing Dataframe! ")
    #print(df.iloc[:])
    
    #np.savetxt("Week3_Mixed_Freq_Wave_df_[Window = 10, Cluster=3, Lambda=0.09, Beta = 0].csv",np.transpose([x,y,cluster_assignment]),delimiter = ',')
    #
    #df = pd.read_csv(fname, converters= {int})
    
    #print(list)
    #print(csvfile)
    #print(row)
    #l = map(float, l)
    #print(x)
    #print(y)
    #print(list)
    '''    
 
       ''' 
        
       
    df.to_csv(', sep = ',')
    #print(l1)
    #print(l2)
    #ax1.plot(l1)
    #ax2.plot(l2)
    #print(np.size(x))
    
    e =  int(time.time() - start_time)
    print(e)
    