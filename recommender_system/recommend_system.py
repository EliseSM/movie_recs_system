import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set() 
from sklearn.cluster import KMeans 
from sklearn.neighbors import KNeighborsClassifier
from scipy.spatial import distance
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import random as sparse_random


#system without any adjustments

def movie_rec_system(df, n_components, recs_num):

    
    #this inputed data has already been well formated for this type of recommender system
    #formatting of data has happened in other document


    #already changed all null values (0) to a neutral value on a scale of 5 (2.5) already in the data wrangling process

    #pushing data into lower dimension 

    svd = TruncatedSVD(n_components = n_components, n_iter=7, random_state=42)
    df_fit = svd.fit(df)
    transformtest = svd.fit_transform(df)
    
    #pushing the data back to its orginal size from the lower dimension data

    final_ratings = svd.inverse_transform(transformtest)

    original_size = final_ratings

    output_recs = []

    #sort through ratings to see which are very positive and have not already been rated

    #all already rated movies are 0
    for x in range(len(original_size[:,1])):
        for y in range(len(original_size[1,:])):
            if (df[x,y]!=2.5):
                original_size[x,y] = 0


    #get recs_num max ratings
    
    for x in range(len(original_size[:,1])):
     
        recs = []

        for c in range(recs_num):

            max_num = max(original_size[x,:])

            for y in range(len(original_size[1,:])):
                movieid = y+1
                
                if (original_size[x,y] == max_num) and df[x,y]==2.5:
                    new_rec = []
                    original_size[x,y] = 1  
                    recs.append(movieid)
                
        output_recs.append(recs) 

    #original favs are IMDB movie ids of movies that were rated 4 or 5 by the user
    original_favs = []
    
    for user in range(len(df[:,0])):
        user_og_favs = []
        for movie in range(len(df[:,0])):
            if df[user, movie] >= 4:
                user_og_favs.append(movie+1)
    
        original_favs.append(user_og_favs)
    
    
    #both original_favs and output_recs should be length of the number of users

    finaloutput = [original_favs, output_recs]

    return finaloutput



#system with adjustments for audience count

def movie_rec_system_audience(df, info_df, n_components, recs_num, adjust):

    
    #this inputed data has already been well formated for this type of recommender system
    #formatting of data has happened in other document


    #already changed all null values (0) to a neutral value on a scale of 5 (2.5) already in the data wrangling process

    #pushing data into lower dimension

    svd = TruncatedSVD(n_components = n_components, n_iter=7, random_state=42)
    df_fit = svd.fit(df)
    transformtest = svd.fit_transform(df)
    
    #pushing the data back to its orginal size from the lower dimension data

    final_ratings = svd.inverse_transform(transformtest)

    original_size = final_ratings

    output_recs = []

    #sort through ratings to see which are very positive and have not already been rated

    #all already rated books are 0
    for x in range(len(original_size[:,1])):
        for y in range(len(original_size[1,:])):
            if (df[x,y]!=2.5):
                original_size[x,y] = 0

                
    #adjusting for audience count so highly watched movies do not dominate the recommendation
                
    for ind in range(len(info_df[:,0])):
        if info_df[ind,0] < len(original_size[0,:]):
            if info_df[ind, 1] > 20000000:
                original_size[:,ind] = original_size[:,ind] - adjust
            else:
                original_size[:,ind] = original_size[:,ind] + adjust
                
          

    #get recs_num max ratings
    
    for x in range(len(original_size[:,1])):
     
        recs = []

        for c in range(recs_num):

            max_num = max(original_size[x,:])

            for y in range(len(original_size[1,:])):
                movieid = y+1
                
                if (original_size[x,y] == max_num) and df[x,y]==2.5:
                    new_rec = []
                    original_size[x,y] = 1  
                    recs.append(movieid)
                
        output_recs.append(recs) 

    #original favs are IMDB movie ids of movies that were rated 4 or 5 by the user
    original_favs = []
    
    for user in range(len(df[:,0])):
        user_og_favs = []
        for movie in range(len(df[:,0])):
            if df[user, movie] >= 4:
                user_og_favs.append(movie+1)
    
        original_favs.append(user_og_favs)
    
    
    #both original_favs and output_recs should be length of the number of users

    finaloutput = [original_favs, output_recs]

    return finaloutput


#system with adjustments for bechdel test

def movie_rec_system_bechdel(df, info_df, n_components, recs_num, adjust):

    
    #this inputed data has already been well formated for this type of recommender system
    #formatting of data has happened in other document


    #already changed all null values (0) to a neutral value on a scale of 5 (2.5) already in the data wrangling process

    #pushing data into lower dimension

    svd = TruncatedSVD(n_components = n_components, n_iter=7, random_state=42)
    df_fit = svd.fit(df)
    transformtest = svd.fit_transform(df)
    
    #pushing the data back to its orginal size from the lower dimension data

    final_ratings = svd.inverse_transform(transformtest)

    original_size = final_ratings

    output_recs = []

    #sort through ratings to see which are very positive and have not already been rated

    #all already rated books are 0
    for x in range(len(original_size[:,1])):
        for y in range(len(original_size[1,:])):
            if (df[x,y]!=2.5):
                original_size[x,y] = 0

                
    #adjusting for audience count for bechdel test
                
    for ind in range(len(info_df[:,0])):
        if info_df[ind,0] < len(original_size[0,:]):
            if info_df[ind, 2] == 0:
                original_size[:,ind] = original_size[:,ind] - adjust
            else:
                original_size[:,ind] = original_size[:,ind] + adjust
                
          

    #get recs_num max ratings
    
    for x in range(len(original_size[:,1])):
     
        recs = []

        for c in range(recs_num):

            max_num = max(original_size[x,:])

            for y in range(len(original_size[1,:])):
                movieid = y+1
                
                if (original_size[x,y] == max_num) and df[x,y]==2.5:
                    new_rec = []
                    original_size[x,y] = 1  
                    recs.append(movieid)
                
        output_recs.append(recs) 

    #original favs are IMDB movie ids of movies that were rated 4 or 5 by the user
    original_favs = []
    
    for user in range(len(df[:,0])):
        user_og_favs = []
        for movie in range(len(df[:,0])):
            if df[user, movie] >= 4:
                user_og_favs.append(movie+1)
    
        original_favs.append(user_og_favs)
    
    
    #both original_favs and output_recs should be length of the number of users

    finaloutput = [original_favs, output_recs]

    return finaloutput


#system with adjustments for bechdel test and audience count

def movie_rec_system_audience_bechdel(df, info_df, n_components, recs_num, adjust_a, adjust_b):

    
    #this inputed data has already been well formated for this type of recommender system
    #formatting of data has happened in other document


    #already changed all null values (0) to a neutral value on a scale of 5 (2.5) already in the data wrangling process

    #pushing data into lower dimension

    svd = TruncatedSVD(n_components = n_components, n_iter=7, random_state=42)
    df_fit = svd.fit(df)
    transformtest = svd.fit_transform(df)
    
    #pushing the data back to its orginal size from the lower dimension data

    final_ratings = svd.inverse_transform(transformtest)

    original_size = final_ratings

    output_recs = []

    #sort through ratings to see which are very positive and have not already been rated

    #all already rated books are 0
    for x in range(len(original_size[:,1])):
        for y in range(len(original_size[1,:])):
            if (df[x,y]!=2.5):
                original_size[x,y] = 0

                
    #adjusting for audience count for bechdel test and audience count
                
    for ind in range(len(info_df[:,0])):
        if info_df[ind,0] < len(original_size[0,:]):
            if info_df[ind, 1] > 20000000:
                original_size[:,ind] = original_size[:,ind] - adjust_a
            else:
                original_size[:,ind] = original_size[:,ind] + adjust_a
            if info_df[ind, 2] == 0:
                original_size[:,ind] = original_size[:,ind] - adjust_b
            else:
                original_size[:,ind] = original_size[:,ind] + adjust_b
                
          

    #get recs_num max ratings
    
    for x in range(len(original_size[:,1])):
     
        recs = []

        for c in range(recs_num):

            max_num = max(original_size[x,:])

            for y in range(len(original_size[1,:])):
                movieid = y+1
                
                if (original_size[x,y] == max_num) and df[x,y]==2.5:
                    new_rec = []
                    original_size[x,y] = 1  
                    recs.append(movieid)
                
        output_recs.append(recs) 

    #original favs are IMDB movie ids of movies that were rated 4 or 5 by the user
    original_favs = []
    
    for user in range(len(df[:,0])):
        user_og_favs = []
        for movie in range(len(df[:,0])):
            if df[user, movie] >= 4:
                user_og_favs.append(movie+1)
    
        original_favs.append(user_og_favs)
    
    
    #both original_favs and output_recs should be length of the number of users

    finaloutput = [original_favs, output_recs]

    return finaloutput