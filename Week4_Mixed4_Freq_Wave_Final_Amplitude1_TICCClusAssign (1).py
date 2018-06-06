# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:58:58 2018

@author: Vignesh
"""
import time
import pandas as pd
import numpy as np
from TICC_solver import TICC
import csv
 
window_size = 1
number_of_clusters= 4
lambda_parameter=0.05
beta=100    
maxIters=1000


if __name__ == '__main__':
    start_time = time.time()    
    fname = "Week4_Mixed[4]_Freq_Wave_Final_Frequency1.csv"
    # s = (np.size(fname))
    # i = 0
    # bic = 0
    #print(fname)
    #ticc = TICC(window_size, number_of_clusters, lambda_parameter, beta, maxIters, threshold=2e-5, write_out_file=False, prefix_string="output_folder/", num_proc=1)
    #(cluster_assignment, cluster_MRFs, bic) = ticc.fit(input_file=fname)
    #print(type(cluster_assignment))
    #print(fname)


    fname2 = "firstfreqdata.csv"
    
    # a,b,c,d,clus_assign = [],[],[],[],[]
    # ctr = 0
    with open(fname) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            a.append(row[0:])
            b.append(row[2:])
            c.append(row[3:])
            d.append(row[4:])
            
    #Converting the string or dataframe into a numpy array inorder to store in dataframe.
    a = np.array(list(a))
    b = np.array(list(b))
    c = np.array(list(c))
    d = np.array(list(d))
    
    #print(a)
    
    j = 0
    
    #s3 = np.size(cluster_assignment)
    k = 0
    #clus_assign = np.zeros(s1)
    #If the window size varies a lot, this section assigns cluster number according to window size
    '''
    for i in range(0,s1):
        clus_assign[i] = cluster_assignment[k]
        ctr+=1
        if(ctr == window_size):
            k+=1
            ctr = 0
    '''
    #Creating dataframe containing the series along with the cluster assignment for every datapoint and converting it into csv format.
    #df = pd.DataFrame({'Sensor 1:':a,'Sensor 2':b,'Sensor 3':c,'Sensor 4':d, 'Cluster Assignment':clus_assign })
    #print("Printing Dataframe! ")
    #print(df.iloc[:])
    
    #df.to_csv('Week4_Mixed[n=4]_Freq_Wave_Final_Amplitude1_1_WithClustAssign.csv', sep = ',')
    e =  int(time.time() - start_time)
    #print("Program over in: ",e, " seconds! i.e.", (e/60)," minutes!")
    