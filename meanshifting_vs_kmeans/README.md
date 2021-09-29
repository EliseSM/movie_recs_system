# portfolio - Movies Analysis and Systems

Elise Schatzki-McClain

## A Time Analysis of sklearn’s Kmeans, sklearn’s MeanShift, and my own implementation of Meanshifting with Rotten Tomatoes’s audience ratings data

In this part, I am wondering if movies with larger audiences have different ratings than movies with smaller audiences. In other words, does the size of the audience dictate the quality of the movie? To do this I used Rotten Tomatoes data to determine the relationship between audience size and audience rating. Rotten Tomatoes is a movie database that collects information on movie’s, specifically lots of information on the audiences of movies. In this project, I am looking at the relationship between audience_rating and audience_count (size of audience) using clustering algorithms that function very differently; sklearn’s kmeans, sklearn’s MeanShift, and my implementation of meanshifting.

### sklearn Kmeans

The sklearn kmeans algorithm is an unsupervised algorithm. Since the data when graphed appears to have two distinct groups, the algorithm was set to look for two clusters of data. This algorithm found two clusters of data, one group of movies with a very high audience count and higher audience rating, and one group of movies with a low audience count and a large range of audience ratings. This algorithm took 0.15257048606872559 seconds to run. Here the center point for the cluster of movies with a large audience was approximately 5 points higher, and had a much smaller range in ratings.

### sklearn Meanshift

The sklearn MeanShift algorithm is one that determines the number of clusters in a dataset, which means it takes much longer to process because it is in addition to finding the clusters and the cluster centers, it is finding the correct number of clusters. When running this algorithm on the audience_rating and audience_count data, it found the same two clusters and very similar cluster center points. The algorithm also pointed that the cluster for the movies with larger audiences had a center for rating than the other cluster did. However, because of the extra processing that had to happen within the algorithm, it took much longer than the kmeans algorithm, and it took 636.8672199249268 seconds to run.

### My implementation of MeanShift

My implementation for MeanShift was adjusted so that it would only do the shifting a set number of times, which allowed one to manually adjusted how much or little processing would happen to create a guess on the number of clusters, the datapoints for each cluster, and the cluster centers. Like the sklearn MeanShift, this algorithm determines how many clusters are in the data set within the algorithm. When iterations were set to 10, this algorithm had a runtime of 22.3972 seconds. This implememntation was not as fast as the kmeans algorithm, but was definitely faster than the sklearn Mean Shift algorithm, likely because of the ability to manually set the number of meanshifting iterations, which would control the amount of processing and also the processing time of the algorithm. Ultimately, the most computationally time expensive line in the algorithm was calculating the distances between points, to determine whether they were inside or outside of the shifting window.

### Results

Ultimately, what has been discovered is that in clustering algorithms, it is very important to be able to control the amount of processing that is done, particularly when the algorithm to does more than just clustering, but also determines how many clusters to make. The algorithm being able to do this also decreases the processing speed of the algorithm significantly.

In terms of what we learned about audience size and audience ratings for movies, we learned that there are two main groups; one that includes all the movies with a small audience and one that includes all the movies with a large audience. The movies with a large audience have a small range of audience ratings and the rating center around 65%. The movies with a small audience have a large range of audience ratings, ranging from almost 0% to 100%, but the audience rating center around 60%. In short, movies that have been seen by more people tend to have higher ratings, but also rarely get very high ratings above 90%.

![image](https://user-images.githubusercontent.com/68246625/119213224-8fc1df00-ba8b-11eb-9e51-4fe9db60d766.png)


