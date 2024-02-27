#!/usr/bin/env python
# coding: utf-8

# # Tweety-lyzer helps analyzing tweets from the dataset over 1.6 million tweets

# In[14]:


import pandas as pd
from textblob import TextBlob


# In[15]:


tweets_df = pd.read_csv('tweets.csv', encoding='latin-1', header=None, names=['target', 'ids', 'date', 'flag', 'user', 'text'])


# In[16]:


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score


# In[ ]:


keyword = input("Enter the keyword or phrase you want to analyze: ")

relevant_tweets = tweets_df[tweets_df['text'].str.contains(keyword, case=False)]
if len(relevant_tweets) == 0:
    print(f"No tweets found containing the keyword '{keyword}'.")
else:
    # Perform sentiment analysis
    relevant_tweets['Sentiment Score'] = relevant_tweets['text'].apply(analyze_sentiment)

    # Display sentiment analysis results
    print(f"Sentiment analysis results for tweets containing '{keyword}':")
    print(relevant_tweets[['text', 'Sentiment Score']])


# In[ ]:












# In[ ]:




