# Segmenting Active Redditors Around Video Game Release Dates

## Executive Summary

The goal of this project is to segment redditors, specifically authors of comments and submissions in relation to the release date of video games. By clustering users, the end goal, is to gain insight into the structure and features of reddit users, their comments, and submissions.

Silhouette score was the primary metric in evaluating the Agglomerative Clustering model. The silhouette score for the model was 0.741.  This score along with visual and mean analysis of clusters indicates that the model has found loose clusters of users. Looking further into each cluster the most notable features for segmentation of users are `LinkKarma`, `comment_count`, `avg_is_submitter`, and `avg_comment_score`. 

It is assumed that the PushShift Database is an accurate representation of submissions posted to Reddit within the determined time periods and that the returned submissions using `q` (search term) are related to the video game. This project is limited specifically to reddit users and the model and code would require substantial changes before it can be used for other social media platforms. Additionally, the model is built on data from reddit users who posted within a specific time period about very specific topics and therefore carries with it a selection bias.

## Navigating Notebooks & Files
1. `aws_mysql.py` contains a mysql connection class that connects to a AWS RDS Database through a NAT Gateway.
2. Data Collection Jupyter Notebook
    - When run, collects data from Steam API, PushShift API, and Reddit using Praw.
    - Collecting all Comments and Authors will take a substaintial amount of time, multiple days.
3. EDA & Model Jupyter Notebook
    - Pulls data from data folder in repository and the AWS RDS Database. 
        - `submissions.csv` is too large for Git and is available here or run 'Data Collection' notebook:  
            https://www.dropbox.com/sh/8py2ks2b758eztt/AAAqFA9TbQCqmkv1ejq3ik25a?dl=0
        - place into the `data` folder
    - Data Cleaning, EDA, & Modeling
    - Results Interpretation
    
## Gathering & Combining Data

Data was gathered in the following order and reasons:
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
5. Push Comment and User data into AWS RDS Database.

## Exporatory Data Analysis

For EDA each dataset was first explored before merging all data together into the users dataset. Initial EDA encompassed exploring the distribution of various features. Although outliers were obvious within many of the distributions, it seemed that these outliers could provide useful information. Especially, as these users with very large number of comments, karma, or other features may cluster into their own group. Outliers were not removed, however, many features were not included in the model. Many boolean features had were very unbalanced and therefore dropped. Variables of interest were mostly data that could be aggregated and grouped by user/author. This aggregated data then provides additional features on which users could be clustered. These variables included, submissions and comments dataset, average score; average length of text; total count; and percentage values for multiple boolean features.

## Data Dictionary

|Feature|type|Dataset|Description|
| :--- | :--- | :--- | :--- |
|UserID|*String*|Users|Unique ID given to each user by Reddit, base 36.|
|CommentKarma|*int64*|Users|Total karma score accumulated by user from comments.|
|CreatedUTC|*int64*|Users|Created date and time of the user account in seconds.|
|VerifiedEmail|*int64*|Users|Whether the user has a verified email (boolean).|
|IsMod|*int64*|Users|Whether the user is a mod of any subreddit (boolean).|
|LinkKarma|*int64*|Users|Total karma score accumulated by user from submissions.|
|Name|*String*|Users|User name.|
|created_date|*datetime64*|Users|Date that user created their account.|
|created_hour|*int64*|Users|Hour that user account was created (1 - 24).|
|name_length|*int64*|Users|Length of username.|
|comment_count|*int64*|Comments|Number of comments posted by user.|
|avg_comment_length|*float64*|Comments|Average comment length.|
|avg_edited_comments|*float64*|Comments|Percentage of comments that were edited by user.|
|avg_is_submittter|*float64*|Comments|Percentage of comments where the user posted the submission in which they commented.|
|avg_comment_score|*float64*|Comments|Average comment score (karma).|

## Modeling

After considering and reviewing multiple clustering models. The models choosen for this dataset were Agglomerative Heirarchical Clustering and DBSCAN. These models were selected as they have methods for dealing with outliers, which were not dropped from the dataset and would deal with data that had very skewed distributions.

Data was scaled using Standard Scaler as distances are the determining factor for clusters. Then using the full dataset, as this is an unsupervised model, the following models were trained. For the Agglomerative Hierarchical Clustering Model a dendrogram was created in order to determine the number of clusters. Then the model was fit and scored with a resulting silhouette score of 0.6TODO. The DBSCAN model was fit and scored with a resulting silhouette score of TODO. Due to lack of domain knowledge the min_sample was set to a default 2 times the number of features, and the epsilon was selected by iterating through multiple epsilon values.

The Agglomerative Heirarchical Clustering Model was expected to, and did, perform better as the density of the data may not be uniform and more importantly many features are boolean and therefore better fit a heirarchical clustering model.

## Results & Conclusions

Although a silhouette score of 0.741 is not great the differences in mean between some features of the dataset indicate that there are features that can be used to segment reddit users. The most notable features are `LinkKarma`, `comment_count`, `avg_is_submitter`, and `avg_comment_score`. 

`CommentKarma` and `LinkKarma` seem to be the best separators of clusters as most clusters have very distinct mean values for these two features. On the other hand there are multiple features such as `avg_comment_score` and `comment_count` that are distinct for some clusters but for others have very similar mean values. However, these differences seem to note that there is segmentation in reddit users by how much karma they have accumulated, how much they post, and their average score per post or comment. This is unsurprising and expected, further analysis needs to be done using NLP to get a better understanding of each cluster.

## Next Steps    

Immediate next steps for this project include collecting more data and conducting NLP on comments and submissions. Collecting more data would include using variations of the video game name to search for submissions that should be included within the dataset. For example 'Sid Meier's Civilization® V', could have been refered to as 'Civilization V', 'Civ 5', or 'Civ V', among other names. Additionally, all posts from each user could be pulled during the same time period as the submissions. This would allow for a deeper analysis of reddit users such as the total comments vs comments about the video game could be compared and overall NLP of all comments the user posted, allowing for a more nuanced model.

NLP could be used to build a better picture of typical reddit users and to check the overall sentiment of users pre and post release date of a game. Further features can be engineered through looking at self focus vs other people, parts of speech usage, and overall sentiment analysis.
    
The next step, conceptually, for this project is to use clustered users, comments, and submission data split into pre and post subsets to predict video game sales based on features such as overall sentiment change pre and post launch and the percentage of users withing different clusters posting comments and submissions.

## Appendix  

### Data Science Articles  
**Clustering Models**  
1. https://www.explorium.ai/blog/clustering-when-you-should-use-it-and-avoid-it/  
2. https://datafloq.com/read/7-innovative-uses-of-clustering-algorithms/6224  
3. https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68  
4. https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80
5. https://www.analyticsvidhya.com/blog/2020/09/how-dbscan-clustering-works/
6. https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html
7. https://towardsdatascience.com/outlier-aware-clustering-beyond-k-means-76f7bf8b4899  
8. https://machinelearningmastery.com/clustering-algorithms-with-python/

**Hierarchical Clustering**
1. https://www.kdnuggets.com/2019/09/hierarchical-clustering.html  
2. https://www.analyticsvidhya.com/blog/2019/05/beginners-guide-hierarchical-clustering/  
3. https://www.sciencedirect.com/topics/computer-science/divisive-clustering  
4. https://stats.stackexchange.com/questions/195446/choosing-the-right-linkage-method-for-hierarchical-clustering  
5. https://stats.stackexchange.com/questions/195456/how-to-select-a-clustering-method-how-to-validate-a-cluster-solution-to-warran/195481#195481  

**Neural Networks**  
1. https://medium.datadriveninvestor.com/when-not-to-use-neural-networks-89fb50622429  
2. https://blog.statsbot.co/neural-networks-for-beginners-d99f2235efca  

**Next Steps**  
1. https://towardsdatascience.com/building-a-topic-modeling-pipeline-with-spacy-and-gensim-c5dc03ffc619  

### Coding References  
1. https://stackoverflow.com/questions/25559202/from-tuples-to-multiple-columns-in-pandas  
2. https://stackoverflow.com/questions/40347689/dataframe-describe-suppress-scientific-notation

