#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 

data = pd.read_csv("C:\\Users\\kuppa\\Downloads\\hap720_icd9_to_icd10.csv")

data 


# In[7]:


icd = pd.read_csv("C:\\Users\\kuppa\\Downloads\\hap720_claims_dgns_demo_dx_rnd_removed (2).csv")
icd


# In[9]:


data_icd = data.merge(icd, right_on = "diagnosis9" , left_on = "icd9" , how = "left")


# In[10]:


data_icd


# In[12]:


data_icd = data_icd [['patient_id', 'diagnosis9' , 'icd10']]


# In[13]:


data_icd


# In[14]:


data_icd['patient_id'].nunique()


# In[15]:


data_icd.drop_duplicates()


# In[16]:


data_icd.to_csv("C:/HAP720/mergedfile.csv")


# In[ ]:




