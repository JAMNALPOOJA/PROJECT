#!/usr/bin/env python
# coding: utf-8

# # Analyzing Instagram Influencers: A Data-Driven Exploration Using Python

# #  Instagram: Shaping Minds and Perspectives
# 
#  Instagram, the brainchild of Kevin Systrom and Mike Krieger, has come a long way since its inception in 2010. Born in the heart of America's tech scene, this photo and video sharing social networking service has become a global sensation, ultimately finding a home under the Facebook Inc. umbrella. At its core, Instagram is a platform that thrives on visual storytelling. Users have the power to share their life's moments, whether mundane or extraordinary, through a captivating blend of photos and videos.
# 
#  However, Instagram's influence reaches far beyond the realm of aesthetics and leisure. It has evolved into a powerful tool for advocacy and change. Influencers, activists, and organizations have harnessed the platform's reach to influence and mobilize their followers on critical issues. By sharing compelling stories, images, and videos, they can shape public opinion and drive societal change. This capacity to sway hearts and minds on pressing matters underscores the platform's role in impacting the order of public discourse.

# # About dataset

# This file contains data on Instagram influencers, featuring 10 attributes sorted by their follower count. Here's what each attribute represents:
# 
# 1. Rank: Influencer's ranking based on their follower count.
# 2. Channel Info: Instagram username of the influencer.
# 3. Influence Score: A score calculated from mentions, importance, and popularity.
# 4. Posts: The number of posts made by the influencer.
# 5. Followers: Total number of followers the influencer has.
# 6. Avg Likes: The average likes received on the influencer's posts.
# 7. 60-Day Eng. Rate: Engagement rate over the last 60 days as a fraction of total engagements.
# 8. New Post Avg. Likes: Average likes on the influencer's new posts.
# 9. Total Likes: The total number of likes the influencer has received on their posts (in billions).
# 10. Country: The influencer's country or region of origin.

# # Import Library

# In[106]:


import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# # Uploading csv file

# In[70]:


df= pd.read_csv("top_insta_data.csv")


# # Data Pre-processing

# In[71]:


df.head()


# In[72]:


df.tail()


# In[73]:


df.shape


# In[74]:


df.columns


# In[75]:


df.dtypes


# In[76]:


df.nunique()


# In[77]:


df.describe()


# In[78]:


df.value_counts()


# In[79]:


df["country"].value_counts()


# In[80]:


df.isnull()


# In[81]:


df.isnull().sum()


# In[82]:


sns.heatmap(df.isnull())


# In[83]:


df.duplicated()


# In[84]:


df


# # Analysis

#  # Top Instagram Performers with the Largest Follower Counts

# In[123]:


top_performers = df.sort_values(by="rank")
top_performers


# In[86]:


# Inference: Top Instagram performers are Cristiano, KylieJenner, SelenaGomez, TheRock, KimKardashian.


# # Correlation between followers and rank

# In[87]:


df.dropna(inplace=True)


# In[88]:


df['followers'] = df['followers'].str.replace('m', '').astype(float)


# In[89]:


df["followers"] = pd.to_numeric(df["followers"])
df["rank"] = pd.to_numeric(df["rank"])


# In[90]:


correlation = df["followers"].corr(df['rank'])
correlation


# In[91]:


# Inference: a correlation coefficient of -0.92 between "followers" and "rank" means there is a strong negative relationship between these variables, where higher ranks are associated with lower follower counts, and lower ranks are associated with higher follower counts among Instagram influencers in your dataset.


# # Average number of followers

# In[92]:


avg_followers = df["followers"].mean()
avg_followers


# In[93]:


# Inference:This value represents the central tendency or the typical value of the "followers" variable in our dataset. Specifically, it means that, on average, Instagram influencers in our dataset have approximately 83.7.


# # Countries with the Highest Number of Performers
# 
# 
# 
# 

# In[94]:


country_counts= df["country"].value_counts()
country_counts


# In[95]:


# Inference: Countries with the highest number of performers are United States, Brazil and India.


# # Relationship between Rank and Follower Count

# In[97]:


plt.scatter(x=df["rank"], y=df["followers"], color = 'Brown')
plt.title["Rank vs Followers count"]
plt.xlable["Rank"]
plt.ylable["followers"]


# In[98]:


df.country.value_counts().plot(kind="bar")


# # Country Map

# In[104]:


df1 = df.groupby('country').size().reset_index(name='Size')
df1


# In[116]:


choropleth_map = go.Figure(
    data = {'type'        :'choropleth',
            'locations'   : df1['country'],
            'locationmode':"country names",
            'colorscale'  :'turbo',
            'z'           : df1['Size'],
            'colorbar'    : {'title':'Influencers Country'},
            'marker'      : {
                'line'    : {'color':'rgb(255,255,255)','width': 2}}},     
    layout = {'geo':{'scope':'world',} })

choropleth_map


# # INFERENCES:
# 

# In[ ]:


# 1.  Top Instagram performers are Cristiano, KylieJenner, SelenaGomez, TheRock, KimKardashian.

# 2. This value represents the central tendency or the typical value of the "followers" variable in our dataset. Specifically, it means that, on average, Instagram influencers in our dataset have approximately 83.7.

# 3. Countries with the highest number of performers are United States, Brazil and India.

#4.  Number of followers are maximum of top rank influencers.

