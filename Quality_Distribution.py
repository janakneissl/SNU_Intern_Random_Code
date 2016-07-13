
# coding: utf-8

# In[1]:

import numpy as np
import pylab as plt
get_ipython().magic('matplotlib inline')


# In[16]:

dic = {}
for line in open('mapQ.txt'):
    currentq = int(line)
    if currentq not in dic:
        dic[currentq]=1
    else:
        dic[currentq]+=1


# In[17]:

dic


# In[18]:

plt.bar(dic.keys(), dic.values())


# In[24]:

dic2 = {}
for line in open('chr5n8.txt'):
    currentq = int(line)
    if currentq not in dic2:
        dic2[currentq]=1
    else:
        dic2[currentq]+=1


# In[25]:

plt.bar(dic2.keys(), dic2.values())


# In[26]:

dic2


# In[ ]:



