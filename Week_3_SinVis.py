# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:06:53 2018

@author: Vignesh
Program to extract the data from the dataframe - namely cluster assignments, Sensor Value (a) and (b).
Visualize them in a plot and also draw plots indicating cluster assignments.
"""
import pandas as pd
from matplotlib import pyplot
import random
import numpy as np
from itertools import cycle

if __name__ == '__main__':
    cycol = cycle('bgrcmk')
    
        
    df = pd.read_csv('Week3_Mixed_Freq_Wave_df[Cluster=3, Lambda=0.09, Beta = 0].csv', sep=',')
    #print(df)
    x = df.iloc[:,2]
    y = df.iloc[:,1]
    s1 = np.size(y)
    print(s1)
    #print(x)
    #print(y)
    pyplot.plot(x)
    #p = plt.axvspan(0, 360, facecolor='g', alpha=0.5)
    #q = plt.axvspan(360, 720, facecolor='b', alpha=0.5)
    #r = plt.axvspan(720, 1000, facecolor='y', alpha=0.5)       
    start_p = 0
    end_p = 0
    ctr = 0
    print("Printing Unique()")
    print(y.unique())
    j= y.unique()
    s2 = np.size(j)
    #print(j[0])
    k = 0
    l = 0
    c = ['b','g','r','g']
    #print(y[0])
    pyplot.plot(x,c='w')
    for i in range(1,1001):
        if(y[i-1] == y[i]):
             end_p=i+1
        else:
             for k in range(0,s2):
                if(j[k]==y[i]):
                    p = pyplot.axvspan(start_p,end_p, facecolor=c[k], alpha=0.7)      
                    start_p=i+1              
                    end_p=i+2
        
            
                  
    
    #pyplot.plot(y)
    #fig, ax = pyplot.subplots()
    #ax.fill(y)
    
                
            