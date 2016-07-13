
# coding: utf-8

# In[1]:

import numpy as np
import pylab as plt
get_ipython().magic('matplotlib inline')
import matplotlib.ticker as mticker


# In[2]:

#read in the coverage file for reads mapped to chr5 with mate reads in chr8
#save the position and the coverage in an array
chr58 = [] 
for line in open('depth5n8.txt','r'):
    l = line.split()[1:]
    chr58.append(l)
chr58 = np.array(chr58, dtype = int)


# In[3]:

#exclude positions with a coverage of 0 
chr58 = chr58[chr58[:,1] != 0]


# In[4]:

#read in the depth file for reads from chr5 with a mate in any other chr
chr5o = [] 
for line in open('depth5no.txt','r'):
    l = line.split()[1:]
    chr5o.append(l)
chr5o = np.array(chr5o, dtype = int)


# In[5]:

#find the unique positions occuring in chr58
pos = set(np.unique(chr58[:,0]))


# In[6]:

#exclude all the positions from chr5o that aren't occuring in chr58
chr5oN = []
for i,x in enumerate(chr5o):
    if chr5o[i,0] in pos:
        chr5oN.append(x)
chr5oN = np.array(chr5oN)


# In[7]:

print(len(chr5oN), len(chr58))


# In[8]:

#exclude all the positions with a coverage under 15
chr58 = chr58[chr5oN[:,1]>15]
chr5oN = chr5oN[chr5oN[:,1]>15]


# In[9]:

#calculate percentage of reads mapped to chr8
perc =chr58[:,1]/chr5oN[:,1]


# In[10]:

plt.figure(1, figsize=(10, 4))
plt.bar(chr5oN[:,0], perc)
plt.xlabel("Position on Chr5")
plt.title("Proportion of Reads with mate in Chr8")
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)


# In[ ]:



