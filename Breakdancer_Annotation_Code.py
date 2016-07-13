############################################
#CHANGE THE SHEBANG#

#!usr/bin/python
#coding: utf-8
import numpy as np
import re

#create empty dictionnaries with the chromosomes as keys 
chros =  ["chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chr8", "chr9", "chr10", "chr11", "chr12", "chr13", "chr14", 
          "chr15", "chr16", "chr17", "chr18", "chr19", "chr20", "chr21", "chr22", "chrX", "chrY"]

#dictionnary for Duplicate regions and Repeat Regions
dupdic = {key:[] for key in chros}
repdic = {key:[] for key in chros}

#Open the segment duplicate file and safe all the duplication positions in the dup dict
for line in open("SegDupsTest.txt", 'r'):
    line = re.split('\t|:|-| ', line.replace('\n', ''))
    for i in range(len(line)):
        if line[i] in dupdic:
            dupdic[line[i]].append((line[i+1], line[i+2]))
            i = i+2

#open the Simple repeat file and safe the repeat positions in the repeat dic
for line in open("SimpleRepeats_parsed.txt", 'r'):
    line = re.split('\t', line)
    if line[0] in repdic:
        repdic[line[0]].append((line[1], line[2]))

#Open output file
f = open('breakdancer_annotated.txt', 'w')
l = open('truelines.txt', 'w')

##############################################
#CHANGE THE NAME OF BREAKDANCER OUTPUT
#write all the lines to a file and annotated them if the positions lay in a duplicated segment
for line in open('breakdancer.ctx', 'r'):
    if not line.startswith('#') and 'chrM' not in line: #not loop through comment lines
        linel = np.array(line.split('\t'))
        if int(linel[8]) >= 75: #check whether wuality score is greater than 75
            linel = np.delete(linel[:9], (2,5,6,7,8), 0)
            #lines has now 4 columns: chr1 pos1 chr2 pos2
            if any(lower <= linel[1] <= upper for (lower, upper) in dupdic[linel[0]]) or any(lower <= linel[3] <= upper for (lower, upper) in dupdic[linel[2]]):
                f.write(str.join('\t', (line.strip('\n'), 'SegDup\n')))  
            elif any(lower <= linel[1] <= upper for (lower, upper) in repdic[linel[0]]) or any(lower <= linel[3] <= upper for (lower, upper) in repdic[linel[2]]):
                f.write(str.join('\t', (line.strip('\n'), 'Repeat\n')))  
            else:
                f.write(line)
                l.write(line)

f.close()
l.close()



