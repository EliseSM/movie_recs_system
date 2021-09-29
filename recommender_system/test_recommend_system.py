import pytest
import pandas as pd
import numpy as np
import recommend_system


#importing relevant rating and movies datasets and adjusting their size to speed up processing

movies_pd = pd.read_csv("merged_movie_data.csv", sep = ",")
movies_np = movies_pd.to_numpy()

ratings_pd = pd.read_csv("wrangled_ratings_data.csv", sep = ",")
ratings_np = ratings_pd.to_numpy()

smaller_ratings_data = ratings_np[:600,:3000]




#tests for normal recommendation system

def test_movie_rec_system_length():
	expected = 2
	assert len(recommend_system.movie_rec_system(smaller_ratings_data, 30, 10)) == expected

def test_movie_rec_system_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system(smaller_ratings_data, 30, 10)) == expected

def test_movie_rec_system_1_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system(smaller_ratings_data, 30, 10)[1][1]) == expected

def test_movie_rec_system_1_length():
    expected = len(smaller_ratings_data[:,0])
    assert len(recommend_system.movie_rec_system(smaller_ratings_data, 30, 10)[1]) == expected

def test_movie_rec_system_1_1_type():
    expected = type(2)
    assert type(recommend_system.movie_rec_system(smaller_ratings_data, 30, 10)[1][1][1]) == expected

def test_movie_rec_system_1_1_length():
    expected = 10
    assert len(recommend_system.movie_rec_system(smaller_ratings_data, 30, 10)[1][1]) == expected

#tests for audience recommendation system

def test_movie_rec_system_audience_length():
	expected = 2
	assert len(recommend_system.movie_rec_system_audience(smaller_ratings_data, movies_np, 30, 10, 0.2)) == expected

def test_movie_rec_system_audience_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system_audience(smaller_ratings_data, movies_np, 30, 10, 0.2)) == expected

def test_movie_rec_system_audience_1_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system_audience(smaller_ratings_data, movies_np, 30, 10, 0.2)[1][1]) == expected

def test_movie_rec_system_audience_1_length():
    expected = len(smaller_ratings_data[:,0])
    assert len(recommend_system.movie_rec_system_audience(smaller_ratings_data, movies_np, 30, 10, 0.2)[1]) == expected

def test_movie_rec_system_audience_1_1_type():
    expected = type(2)
    assert type(recommend_system.movie_rec_system_audience(smaller_ratings_data, movies_np, 30, 10, 0.2)[1][1][1]) == expected

def test_movie_rec_system_audience_1_1_length():
    expected = 10
    assert len(recommend_system.movie_rec_system_audience(smaller_ratings_data, movies_np, 30, 10, 0.2)[1][1]) == expected


#tests for bechdel recommendation system

def test_movie_rec_system_bechdel_length():
	expected = 2
	assert len(recommend_system.movie_rec_system_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2)) == expected

def test_movie_rec_system_bechdel_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2)) == expected

def test_movie_rec_system_bechdel_1_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2)[1][1]) == expected

def test_movie_rec_system_bechdel_1_length():
    expected = len(smaller_ratings_data[:,0])
    assert len(recommend_system.movie_rec_system_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2)[1]) == expected

def test_movie_rec_system_bechdel_1_1_type():
    expected = type(2)
    assert type(recommend_system.movie_rec_system_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2)[1][1][1]) == expected

def test_movie_rec_system_bechdel_1_1_length():
    expected = 10
    assert len(recommend_system.movie_rec_system_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2)[1][1]) == expected


#tests for both audience and bechdel recommendations system

def test_movie_rec_system_audience_bechdel_length():
	expected = 2
	assert len(recommend_system.movie_rec_system_audience_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2, 0.2)) == expected

def test_movie_rec_system_audience_bechdel_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system_audience_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2, 0.2)) == expected

def test_movie_rec_system_audience_bechdel_1_type():
    expected = type(["hello"])
    assert type(recommend_system.movie_rec_system_audience_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2, 0.2)[1][1]) == expected

def test_movie_rec_system_audience_bechdel_1_length():
    expected = len(smaller_ratings_data[:,0])
    assert len(recommend_system.movie_rec_system_audience_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2, 0.2)[1]) == expected

def test_movie_rec_system_audience_bechdel_1_1_type():
    expected = type(2)
    assert type(recommend_system.movie_rec_system_audience_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2, 0.2)[1][1][1]) == expected

def test_movie_rec_system_audience_bechdel_1_1_length():
    expected = 10
    assert len(recommend_system.movie_rec_system_audience_bechdel(smaller_ratings_data, movies_np, 30, 10, 0.2, 0.2)[1][1]) == expected
