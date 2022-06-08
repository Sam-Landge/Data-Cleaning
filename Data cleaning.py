#!/usr/bin/env python
# coding: utf-8

# In[79]:


#### Data cleaning ####


# In[39]:


import pandas as pd
import numpy as np


# In[40]:


people = { 
'first': ['Pet','Herry','jerry','Sherry','Lima','Tomy',np.nan,'NA',None],
'last' : ['Laa','Ham','Ban','Catey','Fa','Goot',np.nan,np.nan,'Missing'],
'email': ['lee.com','ham.com','ban.com','catey.com','Missing','goot.com',None,np.nan,'Missing'],
'age' : [ 34,44,23,88,89,'NA',None,None,'Missing']

}


# In[41]:


df = pd.DataFrame(people)


# In[42]:


df.replace('NA',np.nan, inplace=True)  # we are replacing NA by np.nan, inplace is true because we are modifying file
df.replace('Missing',np.nan,inplace=True)  # we are replacing Missing by np.nan


# In[43]:


df


# In[44]:


df.dropna()


# In[45]:


df.dropna(axis='index',how='all')


# In[46]:


df.dropna(axis='index',how='any')


# In[47]:


df.dropna(axis='columns',how='all')


# In[48]:


# we want all the email
df.dropna(axis = 'index', how = 'any',subset = ['email']) # we want all email


# In[49]:


# still we have to deal with it because it is showing Missing and NA


# In[50]:


# we want the data which has either a last name or email
df.dropna(axis = 'index', how = 'any', subset =['last','email'])


# In[51]:


# we have to replace NA and Missing from our data so we are going back and do changes to the data frame we created.


# In[53]:


# We have to check is there any na value
df.isna()


# In[54]:


df.fillna(0) # filling the missing value by 0


# In[55]:


df.dtypes


# In[58]:


df['age'].mean()


# In[60]:


df['age'].unique()


# In[ ]:




