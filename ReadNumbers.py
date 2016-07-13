
# coding: utf-8

# In[1]:

import numpy as np
import pylab as plt
get_ipython().magic('matplotlib inline')


# In[2]:

#open output file and write header with chromosomes
with open('ChrReads.txt', 'w') as outfile:
    print('\t\tChr1\tChr2\tChr3\tChr4\tChr5\tChr6\tChr7\tChr8\tChr9\tChr10\tChr11\tChr12\tChr13\tChr14\tChr15\tChr16\tChr17\tChr18\tChr19\tChr20\tChr21\tChr22\tChr23\tChr24\tChr25\tTotal\n', 
          file=outfile)


# In[ ]:

#loop through the number of chromosomes (first round: Chr1 reads)
for i in range(1,26):
    #create an empty list to save mate chromosomes
    chrlist = []
    #open the input file and loop through each line
    for line in open('allreads.txt', 'r'):
        #remove 'chr', so chromosome is only identified by number, rename string chromosomes
        line = line.replace('chr','').replace('M','25').replace('X', '23').replace('Y', '24').replace('\n','')
        #split line into 2 chromosomes (read and mate chromosome)
        line = line.split(' ')
        #check whether current line is of the right chromosome (so in first round, chromosome 1)
        if (line[0]!= '*')&(line[1]!='*'):
            if (int(line[0])==i):
                #replace = sign at mate read to be same number as read
                if line[1] == '=':
                    line[1]= line[0]
            #save the chromosome number of the mate read in a list
                chrlist.append(int(line[1]))
    #print the current chromosome to the output
    with open('ChrReads.txt', 'a') as outfile:
        print('\nChr',i,'\t', end='', file = outfile)
        bins = np.bincount(chrlist)[1:]
        total = len(chrlist)
        for bin in bins:
            print(bin,'\t', file=outfile, end='')
        print(total, file = outfile)


# In[ ]:



