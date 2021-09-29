#import statements

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import MeanShift

import time
import math
from scipy.spatial import distance



def data_process_scaling(rotten):
    rotten = rotten.loc[:, ["audience_rating", "audience_count"]]
    rotten_1 = rotten.to_numpy()
    rotten_np = rotten_1[:,:].astype(int)


    #deleting all the 0s in the dataset (nas)
    to_delete = []

    for val in range(len(rotten_np[:,0])):
        if rotten_np[val,0] <= 0 or rotten_np[val,1] <= 0:
            to_delete.append(val)
    
    rotten_np = np.delete(rotten_np, to_delete, 0)

    #scaling the variables
    rating = rotten_np[:,0]
    mx = np.max(rating)
    mn = np.min(rating)


    rating_norm = (rating - mn)/(mx - mn)
    rating_norm = np.around(rating_norm, decimals = 2) 

    count = rotten_np[:,1]
    mx = np.max(count)
    mn = np.min(count)

    count_norm = (count - mn)/(mx - mn)
    count_norm = np.around(count_norm, decimals = 2) 


    rotten_norm = np.stack((rating_norm, count_norm),axis=1)

    return rotten_norm






def meanshifting(groupdata_np, r, flag, rate):
    #groupdata is all the point in a single group
    #r is the radius of the window
    
    
    #starting center
    
    
    rows = groupdata_np.shape[0]
    index = np.random.choice(rows, size=1, replace=False) 
    center = groupdata_np[index[0],:]
 
    
    
    center_np = np.zeros((2000, 2))
    center_np[0,:] = center
   
    
    #looping through the process a set number of times
    for val in range(2000):
        
        #calculating distances between center point and other points and placing them in new group
        
        close_groupx = []
        close_groupy = []
        
        
        
        #looping through num of data points
        
        for ind in range(len(groupdata_np[:,0])):
            #finding dists and sorting ones closest
           
            a = center[0] - groupdata_np[ind, 0]
            b = center[1] - groupdata_np[ind, 1]
            
          
            dist = math.sqrt((a**2) + (b**2))
          
            if dist <= r:
                close_groupx.append(groupdata_np[ind,0])
                close_groupy.append(groupdata_np[ind,1])
                
       
        close_group_mean = np.zeros(2)        
        close_group_mean[0] = np.mean(close_groupx)                       
        close_group_mean[1] = np.mean(close_groupy)
        
      
        if close_group_mean[0] == center[0] and close_group_mean[1] == center[1]:
            break
            
        center = close_group_mean
        center_np[val,:] = center
        
        
        if flag == True:
            r = r * rate
   
    return [center, center_np]

def meanshifting_clustering(groupdata_np, r, flag, rate, times):

    centers = []
    for val in range(times):
        output = meanshifting(groupdata_np, r, flag, rate)
        centers.append(output[0])
      
    #delete duplicates
   
    ind = 0
    
    while ind < (len(centers)-1):
  
        center = centers[ind]
        
        for val in centers[ind+1:]:
            if val[0] == center[0] and val[1] == center[1]:
                centers = centers[:ind] + centers[ind+1:]
                ind = ind - 1
                break
                
        ind = ind + 1
        
        
    return centers



