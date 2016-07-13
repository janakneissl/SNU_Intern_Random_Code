
# coding: utf-8

# In[3]:

import numpy as np
square = np.loadtxt("HeatMap.csv",delimiter=",", dtype=int)


# In[4]:

square


# In[6]:

for k in range(len(square)): 
    row = square[k]
    for j in range(len(row)):
        if j < k:
            square[j,k]= square[j,k]+row[j]
square


# In[9]:

np.savetxt("Triangle.csv", square,delimiter=',', fmt='%1.1i')


# In[ ]:



