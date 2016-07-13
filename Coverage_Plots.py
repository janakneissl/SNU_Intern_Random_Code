
# coding: utf-8

# In[22]:

import numpy as np
import pylab as plt
import math
get_ipython().magic('matplotlib inline')


# In[23]:

coverage = np.loadtxt("coverageTWE69.csv", delimiter = ',')
coverage= coverage[np.all(coverage != 0, axis = 1)]


# In[24]:

pat_to_mot = np.log2(coverage[:,0]/coverage[:,1])
pat_to_fat = np.log2(coverage[:,0]/coverage[:,2])
fat_to_mot = np.log2(coverage[:,2]/coverage[:,1])


# In[83]:

f, (ax1,ax2,ax3) = plt.subplots(3, sharey = True, sharex = True, figsize=(25,13))

ax1.plot(pat_to_mot, 'r.', label ='Patient / Mother')
ax1.legend(fontsize = 18)
ax2.plot(pat_to_fat, 'b.',label ='Patient / Father')
ax2.legend(fontsize = 18)
ax3.plot(fat_to_mot, 'g.',label ='Father / Mother')
ax3.legend(fontsize = 18)
f.subplots_adjust(hspace = 0)
plt.axis('tight')

f.text(0.9,0.06, 'Positions tested for Sequencing Coverage', ha = 'right', va='center')
f.text(0.08, 0.5, 'Log-Ratio of Coverage', ha='center', va ='center', rotation='vertical')
plt.rcParams.update({'font.size': 22})
f.suptitle("Copy Number Variation in Family TWE-69", fontsize = 28)

plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible = False)


# In[ ]:



