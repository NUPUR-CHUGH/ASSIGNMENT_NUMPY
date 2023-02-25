#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ASSIGNMENT


# In[ ]:


#PROBLEM 1


# In[ ]:


Prepare aarray of all zeros(3 rows and 4 columns)


# In[2]:


import numpy as np


# In[3]:


zeros_array=np.zeros((3,4))
print(zeros_array)


# In[ ]:


#PROBLEM2


# In[ ]:


1.Create two arrays (numbers between 10-20),First array shape=(2,3,5),Second array shape=(1,3,5)


# In[4]:


array1=np.random.randint(10,21,size=(2,3,5))
print("Array 1:\n",array1)
array2=np.random.randint(10,21,size=(1,3,5))
print("Aeeay 2:\n",array2)


# In[ ]:


2.Now mutiply them


# In[5]:


mult_array=np.multiply(array1,array2)
print("Multipliedarray:\n",mult_array)


# In[ ]:


3.Find the min Axis=1 wise


# In[6]:


min_array=np.amin(mult_array,axis=1)
print("Minimum array along axis 1:\n",min_array)


# In[ ]:


4.Find the sum Axis=0 Wise


# In[7]:


sum_array=np.sum(mult_array , axis=0)
print("Sum array alongaxis 0:\n",sum_array)


# In[ ]:




