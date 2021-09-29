# portfolio - Movies Analysis and Systems

Elise Schatzki-McClain

## Recommendations Systems with Boosting for Audience Size and Bechdel Test Passing


From part 1 of this project (meanshifting_vs_kmeans), we have determined that people have stronger opinions or a wider range of opinions on movies that are less popular. From part 2 of this project (crossval_critics_v_audience_model) we have learned that the critics’ opinions do not always correlate with the audience’s opinions. Using this information, I created a movie recommendation system for audience members based on solely audience data. This data was from MovieLens audience member ratings and did not include any critics ratings in the data.

Each column in the data represented a movie and each row represented an audience member. The ratings were done on a scale of 1 to 5, and all movies that an audience member had not yet seen and rated were automatically 2.5. This is because 2.5 represents a neutral opinion on a scale of 1 to 5.

The recommendation system was made through reducing the dimension of audience ratings data for each movie using SVD and then pushing the data back into its originally space, showing scores for movies that each particular audience member had not yet seen. These scores are different because other audience member with similar or dissimilar tastes have affected these scores for an individual audience member.

However, this system has flaws because some movies get seen more than other movies, but are not necessarily rated higher than other movies. Some movies become very popular or unpopular in a dimension reduction recommendation system based on external factors, even though these trends may not actually be reflected in an audience’s opinions. Therefore, I chose to create multiple recommendation systems; one that is typical, one that tries to artificially boosts movies that have a smaller audience, one that artificially boosts movies that pass the Bechdel test, and one that artificially boost movies that have a small audience and pass the Bechdel test. 

## Test Audience Member's Recommendations between the 4 Systems

To test if this artificial boosting really even affected the actual recommended movies at all, I did a test trial and took one random sample to investigate and compare the different recommendation systems. This audience member’s recommendations from the various systems are listed below. What is interesting about these systems is that although some of the recommendations between the systems differ, a lot of the same movies show up in the recommendations, despite them not be artificially boosted by the systems. An example of this is 300, is recommended in 3 of the 4 systems despite it having a large audience and not passing the Bechdel test. This just shows that although you can try to influence and equalize movie recommendation systems, the system will still recommend movies that it would have recommended otherwise anyways. The current dimension reduction recommendation system leans strongly towards recommending movies with larger audiences due to the fact that the more ratings a movie gets, the more likely those high ratings could be passed on to others in the system, making them more likely movie recommendations for the system.


## Random Audience Member's Recommendations:

### This audience member already likes:

Lost in Translation

True Romance

Seven Samurai

### The Normal System:

Cat on a Hot Tin Roof

Meet Joe Black

The Crime of Padre Amaro

The Hours

300

### The Audience Boosting System:

Cat on a Hot Tin Roof

The Crime of Padre Amaro

The Hours

The Terminal

Poltergeist

300

### The Bechdel Boosting System:

Cat on a Hot Tin Roof

The Killing

Dangerous Liaisons

300

### The Audience and Bechdel Boosting System:

Cat on a Hot Tin Roof

The Killing

Man of Marble

Harry Potter and the Chamber of Secrets

Dangerous Liaisons

