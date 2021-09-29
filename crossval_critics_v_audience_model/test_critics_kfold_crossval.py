import pytest
import pandas as pd
import numpy as np
import critics_kfold_crossval


#import relevant data which is rotten tomatoes movie dataset

rotten = pd.read_csv("rotten_tomatoes_movies_Mark.csv", sep=',')
rotten['audience_status'] = rotten['audience_status'].replace(['Spilled'], 0)
rotten['audience_status'] = rotten['audience_status'].replace(['Upright'], 1)
rotten_pd = rotten.loc[:, ['tomatometer_rating', 'tomatometer_count', 'audience_status']] 
rotten_np = rotten_pd.to_numpy()
rotten_np = rotten_np.astype(int)

#tests for splitting_valid_testrain function

def test_splitting_valid_testrain_length():
	expected = 2
	assert len(critics_kfold_crossval.splitting_valid_testrain(rotten_np)) == expected

def test_splitting_valid_testrain_shape0():
	expected = (1604, 3)
	assert critics_kfold_crossval.splitting_valid_testrain(rotten_np)[0].shape == expected

def test_splitting_valid_testrain_shape1():
	expected = (14443, 3)
	assert critics_kfold_crossval.splitting_valid_testrain(rotten_np)[1].shape == expected

def test_splitting_valid_testrain_type():
    hello = ["hello"]
    expected = type(hello)
    assert type(critics_kfold_crossval.splitting_valid_testrain(rotten_np)) == expected

def test_splitting_valid_testrain_type0():
    expected = type(rotten_np[1,1])
    test = critics_kfold_crossval.splitting_valid_testrain(rotten_np)[0]
    assert type(test[0,0]) == expected

# test for knn crossval function

def test_knn_crossval_type():
	expected = type(rotten['audience_rating'][1])
	assert type(critics_kfold_crossval.kNN_crossval_k_fold(rotten_np, 20, 70)) == expected


# test for logreg crossval function

def test_logreg_crossval_type():
	expected = type(rotten['audience_rating'][1])
	assert type(critics_kfold_crossval.logreg_crossval_k_fold(rotten_np, 20)) == expected