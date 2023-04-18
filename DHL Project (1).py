#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


data = pd.read_csv(r"C:\Users\DELL\Desktop\BackOrders.csv")


# In[6]:


data.isnull()


# In[7]:


data.isnull().sum()


# In[8]:


remove=['lead_time']
data.drop(remove,inplace=True,axis=1)


# In[9]:


data.duplicated()


# In[ ]:




