# Clustering Reddit Authors

## Executive Summary

The goal is this project is two part. The first goal is to cluster redditors who author comments. Then using these cluster try to gain insight into the make up of redditors per game and see if there are 

What differences are there inthe  make up different subgroups. What is the difference if any in the groups between pre and post release date.

Assumptions of this 
    




Ultimately, want to use clustered users, submissions and comments analysis to predict game sales.
Why not include the release date?

Don't want to measure the magnitude of response on Reddit vs the magnitued of game sales. More interested in the groups of clustered users, nlp analysis, and pre and post launch comparisons.
    

* predicting sales volume for games
* measuring metrics on reddit, submissions/comments
* gathering statistics on authors
* nlp if time permitting
* cluster authors through unsupervised models -> uncertain number of categories

Poor assumptions:
* praw/pushshift will have all information, will at any way be pushable to future information/results
* 

## Gathering & Combining Data

Steps:
1. Select games for analysis.
    - Recency, post 2016.
    - Games without early access so that release dates accurate represent when a game was launched.
    - Relatively successful games/well known games that should have noticable footprints on reddit.
2. Gather game data, release dates, from Steam API.
3. Use PushShift API to get all posted submissions about the game on Reddit.
    - Using `q`, search term filter set to the game name
    - Limit to 5 days pre and post release date, enough time to gauge pre and post activity
3. Use Praw to get comments from each submission.
4. Get User (Redditor) information for each comment.
5. Push Comment and User data into AWS RDS.

Steps to incorporate in the future:
- Using variations of the game name to get submissions.
- Pull more comments and submissions from each Redditor to build better features.

## Exporatory Data Analysis

The variables of interest were any features in relation to the authors as part of the goal is to cluster authors into groups,
Did not remove any outliers as they provide valuable information and 

We want to focus on pre/post

Distribution of features within submissions, comments, users
Look at how data changes with different subsets of features such as 

## Feature Engineering
 
Submission and Comment data have author columns that can be used to link submissions and comments to a specific user.

Users 
    1. additional features from self
        -
    2. features from submissions dataset
        - 
    3. features from comments dataset
        - 
    
    # sentiment analysis of all comments
    # 


## Modeling

Choosing between multiple clustering models. Listed below is the decision process for why certain models were tested and why the final model was selected.

K-Means
    Requires the number of clusters, which is not available.
    
Mean-Shift
    

DBSCAN

EM Clustering using GMM

Agglomerative Hierarchical Clustering

Neural Network
    Part of our goals for clutering is to gain insight in features and Reddit but this is difficult with a neural network.


Used DBSCAN because we want to keep outliers to look for 'whales' or strong posters/users. 

For the clustering of redditors we used the DBSCAN model as we are expecting outliers, especially for variables such as `LinkKarma` and `CommentKarma`. 

## Results & Conclusions



## Next Steps
    
NLP Analysis
    # POS pre/post
    # Self Focused vs other people (I, me, etc)
    # Parts of speech within each grouping
    # looking at total compilation of text instead of just single comments
    # causes issues when we are developing this for users/submissions that have very few comments


## Appendix A

#### Data Science Articles
https://medium.datadriveninvestor.com/when-not-to-use-neural-networks-89fb50622429
https://blog.statsbot.co/neural-networks-for-beginners-d99f2235efca

https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68
https://medium.datadriveninvestor.com/when-not-to-use-neural-networks-89fb50622429

https://www.explorium.ai/blog/clustering-when-you-should-use-it-and-avoid-it/
https://datafloq.com/read/7-innovative-uses-of-clustering-algorithms/6224
https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80

## Appendix B

#### Coding References
