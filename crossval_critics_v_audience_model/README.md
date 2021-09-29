# portfolio - Movies Analysis and Systems

Elise Schatzki-McClain

## Predicting audience reaction based on Critic opinions using k-fold cross validation to test kNN and Logistic Regression models


In this part of the project, I was wondering if one can predict what the audience’s reaction will be based on the critic’s reaction to a movie. To do this, I used rotten tomatoes data and tried to use the number of critic reviews and the critics ratings as a predictor to determine whether a majority of the audience reviewed the film positively.

### Performing 20 fold Cross Validation and Choosing a Model

To do this tested two different sklearn models, kNN and Logistic Regression. The process in the specifics of how this was done is noted in the jupyter notebook in this directory. First, I split the rotten tomatoes data into a train/test dataset and a validation dataset. The train/test dataset would be used for performing cross validation and choosing a model and the validation set would be checking if the chosen model performs well on new data.

I performed 20-fold cross validation on both the kNN and the Logistic Regression model.  To do this the test/train dataset was split into 20 groups and was interchanged with each other in a testing and training process twenties times. Through this, there are 20 mean squared errors calculated for the 20 models fitted with different data, and the average of these errors shows how well the model fits the given data overall. For both kNN and Logistic Regression, the errors were approximately 0.24. However, the error was slightly higher for the Logistic Regression, so I chose the kNN model to continue my analysis.

The kNN model has the n_neighbors predictor which can change how the function creates the model and fits the data to the model. To see if there is any variability in the accuracy of the model’s predictions depending on the n_neighbors values, I fit all the test/train data to the kNN model, and I tested and graphed the mean square errors for a range of n_neighbors values. In the end, the best n_neighbors value seemed to be around 20.

### Conclusion

With this information, I fit all the test/train dataset to the kNN model with n_neighbors = 20. Then I tested the accuracy of the model by introducing the validation set and using the model to predict the data from the validation set. Here, the mean square error was approximately 0.22. After calculating the predictions, around 22% of the validation set was predicted inaccurately by the kNN model. This just shows that although critics reviews and opinions might help predict audience opinions for some movies, for other movies, the critics opinion will be less helpful. Most of the incorrect prediction happened when the critics rated a move 30% to 70%, meaning that that audiences and critics might agree on the movies they strongly like and dislike, but not as much on movies they have less strong opinions about.

![image](https://user-images.githubusercontent.com/68246625/119213026-4b820f00-ba8a-11eb-9106-272cbeef9d14.png)


