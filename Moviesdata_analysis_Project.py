#!/usr/bin/env python
# coding: utf-8

# In[1]:


###Importing Required Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[2]:


###importing data 
df=pd.read_csv("Movies_data.csv",engine='python')


# In[3]:


###check the data
df.head()


# In[4]:


## Display summary of the DataFrame
df.info()


# In[5]:


###check the null values
df.isna().sum()


# In[6]:


###separte the null values as a dataframe
null_df= df[df.isnull().any(axis=1)]


# In[7]:


null_df


# In[8]:


###Drop the null values 
df=df.dropna()


# In[9]:


###check the null values
df.isna().sum()


# In[10]:


df.shape


# In[11]:


###check the data type of columns
df.dtypes


# In[12]:


###Convert the column from object to int
df.loc[:, "Vote_Count"] = df["Vote_Count"].astype(int)


# In[13]:


###Convert the column from object to float
df.loc[:, "Vote_Average"] = df["Vote_Average"].astype(float)


# In[14]:


###describe the dataframe
df.describe()


# In[15]:


###Convert the column from object to datatime
df["Release_Date"]=pd.to_datetime(df["Release_Date"])


# In[16]:


print(df["Release_Date"].dtype)


# In[17]:


df.head(5)


# In[18]:


###Extracts the year from the "Release_Date" column 
df["Release_Date"]=df["Release_Date"].dt.year


# In[19]:


df.head(5)


# In[20]:


### make alist of unneccesory columns
col_d=["Overview","Original_Language","Poster_Url"]


# In[21]:


### drop the unneccesory columns
df.drop(col_d,axis=1,inplace=True)


# In[22]:


df.head(5)


# In[23]:


#Returns the count of unique values in the "Vote_Average" column
df["Vote_Average"].value_counts()


# In[24]:


### statistics summary 
df["Vote_Average"].describe()


# In[25]:


### Define labels for categorizing the "Vote_Average"
label=["Not Popular","Below Average","Average","Popular"]


# In[26]:


### Function to categorize a column 
def categorize_fun(df,col,label):
    edges=[df["Vote_Average"].describe()['min'],
           df["Vote_Average"].describe()["25%"],
           df["Vote_Average"].describe()["50%"],
           df["Vote_Average"].describe()["75%"],
           df["Vote_Average"].describe()["max"]]
    df[col]=pd.cut(df[col],edges,labels=label,duplicates='drop')
    return df


# In[27]:


categorize_fun(df,'Vote_Average',label)


# In[28]:


###Returns the count of unique values in the "Vote_Average" column, showing how many times each vote average occurs
df["Vote_Average"].value_counts()


# In[29]:


###drop null values
df.dropna(inplace=True)


# In[30]:


###check null values
df.isna().sum()


# In[31]:


df.head()


# In[32]:


# Splits the "Genre" column values by comma and space (", "), converting them into a list of genres for each row
df["Genre"]=df["Genre"].str.split(", ")


# In[33]:


###Explode "Genre" column and reset index
df=df.explode("Genre").reset_index(drop=True)


# In[34]:


df


# In[35]:


###check the data types
df.dtypes


# In[36]:


###Convert "Genre" to categorical type
df["Genre"]=df["Genre"].astype("category")


# In[37]:


df.dtypes


# In[38]:


###check the unique values
df.nunique()


# In[39]:


df.head(5)


# In[40]:


df["Genre"].describe()


# In[41]:


###Count occurrences of each genre
df["Genre"].value_counts()


# In[42]:


###Create count plot for "Genre"
sns.set_style('darkgrid')
sns.catplot(y="Genre",data=df,kind='count',order=df["Genre"].value_counts().index)
plt.title("Exploring Genre Distribution")
plt.show()


# In[43]:


df.head()


# In[44]:


###visualizing vote_average column
sns.histplot(df['Vote_Average'], bins=10)
plt.xlabel('Vote Average')
plt.ylabel('Count')
plt.title("'Distribution of Vote Average'")
plt.show()


# In[45]:


###Group the DataFrame by the 'Genre' column and calculate the sum of 'Vote_Count' for each genre
genre_vote_counts = df.groupby('Genre')['Vote_Count'].sum().reset_index()


# In[46]:


genre_vote_counts 


# In[47]:


###checking max popularity in dataset
df[df["Popularity"]==df["Popularity"].max()]


# In[48]:


###checking min popularity in dataset
df[df["Popularity"]==df["Popularity"].min()]


# In[49]:


### Histogram 
plt.hist(x='Release_Date',data=df);
plt.xlabel("Year")
plt.ylabel("Movies Count")
plt.title("Movies Count by Year")
plt.show()


# Q1: What is the most frequent genre in the dataset?
#     Drama genre is the most frequent genre in our dataset and has appeared more than  14% 
#     of the times among 19 other genres.
# 
# Q2: What genres has highest votes ?
#     The genre "Action" has the highest votes with votecount 4868675.
# 
# Q3: What movie got the highest popularity ? what's its genre ?
#     Spider-Man No Way Home has the highest popularity rate in our dataset and it has genres of Action,
#     Adventure and Sience Fiction.
# 
# Q3: What movie got the lowest popularity ? what's its genre ?
#     'The united states', 'thread' has the highest lowest rate in our dataset and it has genres
#     of 'music' , 'drama' , 'war', 'Science Fiction' and 'history'.
# 
# Q4: Which year has the most filmmed movies?
#     year 2020 has the highest filmming rate in our dataset.
