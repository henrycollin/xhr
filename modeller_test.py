# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:34:05 2017

@author: bio608
"""

##### clustal omega inout file #####

import os, re
#file = os.path.abspath("C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\1KLU.txt")
with open("C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\1KLU.pir", 'rt') as f:
    seq = list()
    line3 = str()
    for line in f:
        line2 = line.split('\n');
        seq.append(line2)
        ### list to string ###
        #line3 = ''.join(str(e) for e in seq);

print (seq[0],seq[1])
    