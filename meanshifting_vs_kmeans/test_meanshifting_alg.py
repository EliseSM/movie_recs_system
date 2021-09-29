import pytest
import pandas as pd
import numpy as np
import meanshifting_alg


#importing relevant data

rotten = pd.read_csv("rotten_tomatoes_movies_Mark.csv", sep=',')

rotten_norm = meanshifting_alg.data_process_scaling(rotten)


#tests for data processing function

def test_data_process_shape():
    expected = (16381, 2)
    assert meanshifting_alg.data_process_scaling(rotten).shape == expected


def test_data_process_type():
    expected = type(rotten["audience_rating"][1])
    np =  meanshifting_alg.data_process_scaling(rotten)
    assert type(np[1,1]) == expected

def test_data_process_max():
    expected = 1
    data =  meanshifting_alg.data_process_scaling(rotten)
    assert np.max(data[:,0]) <= expected



#tests for meanshifting function


def test_meanshifting_length():
    expected = 2
    assert len(meanshifting_alg.meanshifting(rotten_norm, 0.2, False, 0)) == expected


def test_meanshifting_0_shape():
    expected = (2,)
    assert meanshifting_alg.meanshifting(rotten_norm, 0.2, False, 0)[0].shape == expected


def test_meanshifting_0_type():
    expected = type(rotten_norm)
    assert type(meanshifting_alg.meanshifting(rotten_norm, 0.2, False, 0)[0]) == expected


def test_meanshifting_1_type():
    expected = type(rotten_norm)
    assert type(meanshifting_alg.meanshifting(rotten_norm, 0.2, False, 0)[1]) == expected





#tests for mean shifting clustering function


def test_clustering_type():
    expected = type(rotten_norm)
    assert type(meanshifting_alg.meanshifting_clustering(rotten_norm, 0.2, False, 0, 10)[0]) == expected


def test_clustering_0_shape():
    expected = (2,)
    assert meanshifting_alg.meanshifting_clustering(rotten_norm, 0.2, False, 0, 10)[0].shape == expected

