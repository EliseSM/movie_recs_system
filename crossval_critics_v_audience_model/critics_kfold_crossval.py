import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
import statistics

import time
from scipy.spatial import distance


def splitting_valid_testrain(rotten_np):

    to_delete = []
    for val in range(len(rotten_np[:,0])):
        if rotten_np[val,0] <= 0 or rotten_np[val,1] <= 0 or rotten_np[val,2] < 0:
            to_delete.append(val)
            
    rotten_np = np.delete(rotten_np, to_delete, 0)
    
    

    valid_size = int(len(rotten_np[:,0])/10)

    valid_indexs = np.random.choice(range(len(rotten_np[:,0])), size= valid_size, replace=False) 

    #creating the validation dataset

    validation_np = np.empty([valid_size, 3])

    for ind in range(valid_size):
        #index_val = valid_indexs[ind]
        validation_np[ind,:] = rotten_np[valid_indexs[ind],:]

    #creating the train/test dataset
    length = len(rotten_np[:,0])

    testtrain_np = np.empty([length-valid_size, 3])

    count = -1
    for ind in range(len(rotten_np[:,0])):
        if ind not in valid_indexs:
            count = count+1
            testtrain_np[count,:] = rotten_np[ind,:]

    validation_np = validation_np.astype(int)        
    testtrain_np = testtrain_np.astype(int)
    
    
    output = [validation_np, testtrain_np]
    
    return output



#kNN cross val

def kNN_crossval_k_fold(data, k, n_neighbors):
   
    #splitting data into k equal pieces
    
    length = len(data[:,1])/k
    size = int(length)

    k_groups = []
  
    for x in range(k): 
        new_group = np.empty([size, 3])
        
        for num in range(size):    
            new_group[num,:] = data[x+(k*num),:]
        k_groups.append(new_group)

    # Initialize the list of errors
    test_errors = []
    
    for val in range(k):
        
        # Split data into train and test
        
        test_data = k_groups[val]
        
        for_train = []
        for num in range(k):
            if num != val:
                for_train.append(k_groups[num])
        
        for_train = tuple(for_train)     
        train_data = np.vstack(for_train)
        
        # Create and train a model
        # Create the details of the model
       
        # Set up the particulars for the knn neighbors classification
        knn = KNeighborsClassifier(n_neighbors = n_neighbors)

        # Fit the kNN model to the data
        knn_fit = knn.fit(train_data[:,[0,1]], train_data[:,2])

        # Compute the testing error and add it to the list of testing errors
      
        #predicting kNN model data
        preds = knn_fit.predict(test_data[:,:2])
        
        res_MSE = np.mean((test_data[:,2]-preds)**2)
        test_errors.append(res_MSE)
        
    # Compute the cross-val error
    cross_val = statistics.mean(test_errors)
    
    return cross_val


#logistic regression cross val


def logreg_crossval_k_fold(data, k):
   
    #splitting data into k equal pieces
    
    length = len(data[:,1])/k
    size = int(length)

    k_groups = []
  
    for x in range(k): 
        new_group = np.empty([size, 3])
        
        for num in range(size):    
            new_group[num,:] = data[x+(k*num),:]
        k_groups.append(new_group)

    # Initialize the list of errors
    test_errors = []
    
    for val in range(k):
        
        # Split data into train and test
        
        test_data = k_groups[val]
        
        for_train = []
        for num in range(k):
            if num != val:
                for_train.append(k_groups[num])
        
        for_train = tuple(for_train)     
        train_data = np.vstack(for_train)
        
        # Create and train a model
        # Create the details of the model
       
        # Set up the particulars for the logistic regression classification
        lr = LogisticRegression()

        # Fit the logistic regression model to the data
        lr_fit = lr.fit(train_data[:,[0,1]], train_data[:,2])

        # Compute the testing error and add it to the list of testing errors
      
        #predicting logistic regression model data
        preds = lr_fit.predict(test_data[:,:2])
        
        res_MSE = np.mean((test_data[:,2]-preds)**2)
        test_errors.append(res_MSE)
        
    # Compute the cross-val error
    cross_val = statistics.mean(test_errors)
    
    return cross_val


def wrong_points(data, n_neighbors):

    knn = KNeighborsClassifier(n_neighbors=n_neighbors)

    knn_fit = knn.fit(data[:,:2], data[:,2])

    preds = knn_fit.predict(data[:,:2])

    wrong_sides = []

    for ind in range(len(preds)):
        if preds[ind] == data[ind,2]:
            wrong_sides.append(0)
        else:
            wrong_sides.append(1)
  
    percentage_wrong = sum(wrong_sides)/len(wrong_sides)
    
    return percentage_wrong