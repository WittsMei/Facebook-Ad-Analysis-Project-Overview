#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 


# In[2]:


df = pd.read_csv('KAG_conversion_data.csv')
df.head()


# In[3]:


print(f'There are {df.shape[0]} rows and {df.shape[1]} columns')


# <br>
# 
# # Data Cleaning 

# <br>
# Looking for any missing values first.

# In[4]:


df.info()


# <br>
# 
# There are no null values. Let's procceed with checking if there are any error in the categorical values. We only have age and gender as categoical values. 
# 
# 
# 
# 
# 
# 
# 

# In[5]:


df.age.value_counts()


# In[6]:


df.gender.value_counts()


# In[7]:


df['gender'].replace(
    {
      'M': 'Male',
      'F': 'Female',
    }, 
    inplace=True
)


# <br>
# 
# 
# Let's double check the values in gender if they're successfully replaced:

# In[8]:


df.gender.value_counts()


# In[9]:


df.describe().T


# <br>
# 
# Take a look at 'xyz_campaign_id' as this is the assoiated id for each as campaign used.

# In[10]:


df.xyz_campaign_id.value_counts()


# In[11]:


df['xyz_campaign_id'] = df['xyz_campaign_id'].astype(str)

df['xyz_campaign_id'].replace(
    {
      '1178': 'Campaign_c',
      '936': 'Campaign_b',
      '916': 'Campaign_a',
    }, 
    inplace=True
)


# <br>
# 
# Let's double check the values in xyz_campaign_id if they're successfully replaced:

# In[12]:


df['xyz_campaign_id'].value_counts()

