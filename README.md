# portfolio - Movies Analysis and Systems

Elise Schatzki-McClain

### Introduction:

I am computer science student who took computational machine learning in Spring 2021. From this course, I have learned a lot of skills about a variety of subjects, including but not limited to supervised learning, unsupervised learning, clustering, classification, cross validation, gradient descent, efficacy, and benchmarking. In addition to these machine learning skills, I have been developing professional programming skills throughout my education and in my work experiences, including making unit tests, using GitHub and GitHub Actions, and contributing to and participating in group programming projects and problem-solving discussions.

In this project, I demonstrate some of the skills I have learned in this class through investing movie ratings and recommendation systems. The project is split into three parts, and the first two parts build up into decisions I make in the third part which is about movie recommendation systems. This project asks important questions about how recomendations systems work and whose opinions and voices are prioritized. How does the size of an audience or a movie's popularity correlate with a movie's ratings? How does a movies popularity and audience size influence whether of not the movie is recommended or not in a recommendation system? Do critic opinions help predict the audience's opinions on movies, and should they be included in recommendation systems for audiences? There are many different internal and external factors in ratings systems and recommendation systems outside of the pure number ratings, and this project aims to investigate some of these factors and how they can potentially influence movie recommendations systems.


## Part 1 - Clustering Audience Sizes and Ratings using Kmeans and Mean Shifting

In this project I look at the different methods to cluster and find the center point (most-densely packed point) of a cluster of data. I investigate the efficacy and time efficiency of the following clustering functions; sklearn's k-means, sklearn's MeanShifting, and my adjusted meanshifting implementation. Here, I look at the time cost of having to actively find the number of clusters that appear in a dataset inside a function. In addition, I find how audience sizes can be correlated with certain ranges of movie ratings.


## Part 2 - Assessing Rotten Tomatoes Critics Opinion vs. Audience Opinion Models using Cross Validation

In this project I analyze different supervised models (kNN and logistic regression) using cross validation to analyze the accuracy of their predictions. The models use critic ratings and the number of critics who have viewed a movie to try to predict whether or not a majority of the audience will enjoy the movie. It questions whether one can predict the audience's opinions of a movie based on the critic's opinions of the movie.


## Part 3 - Boosting in Recommendations Systems for Audience Size and Bechdel Passing

In this part of the project, I make a recommendation system using SVD dimension reduction to determine which movies are predicted to have good ratings for each user based on their previous MovieLens reviews. I make multiple recommendation systems that boost different external factors within the systems to increase the likelihood of particular movies being recommended. This system aims to equalize the current dimension reduction recommendation system model, while still catering to an individual user's tastes. 



#### Resources and Data:

The Movies Dataset - Rounak Banik
https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv

Bechdel Dataset - Andrew Flowers
https://github.com/fivethirtyeight/data/blob/master/bechdel/movies.csv

rotten-tomatoes-movies-and-critics-datasets - Mark
https://www.kaggle.com/heyueyuan/rottentomatoesmoviesandcriticsdatasets?select=rotten_tomatoes_reviews.csv




