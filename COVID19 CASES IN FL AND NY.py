#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


import pandas as pd


# In[3]:


os.getcwd()


# In[4]:


location = "time_series_covid19_confirmed_US-0331.csv"


# In[5]:


df = pd.read_csv(location)


# In[13]:


df.head()


# In[28]:


data=df.loc[df['Province_State'].isin(['Florida','New York'])]


# In[32]:


data_sum=data.groupby('Province_State')["3/31/20"].sum()


# In[33]:


print(data_sum)


# In[38]:


data_sum.plot(kind='bar')


# In[ ]:




