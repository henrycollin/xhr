# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:34:05 2017

@author: bio608
"""

##### clustal omega inout file #####

import os, re
#file = os.path.abspath("C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\1KLU.txt")
input_file_1 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\1KLU.pir"
input_file_2 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\3C5J.pir"
input_file_3 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\4X5W.pir"

with open(input_file_1, 'rt') as f:
    file = open("tamplate_imformation.pir","w")
    seq = list()
    clu_input = str()
    line4 = str()
    
    for line in f:
        line2 = line.split('\n');
        seq.append(line2)

clu_imfor = (seq[0]+['\n']+seq[1]+['\n']+seq[7]+['\n']+seq[8]+['\n'])
line4 = ''.join(str(e) for e in clu_imfor)
#print (line4)
file.write(line4)
file.close()

with open(input_file_2, 'rt') as f:
    file = open("tamplate_imformation.pir","a")
    seq = list()
    clu_input = str()
    line5 = str()
    
    for line in f:
        line2 = line.split('\n')
        seq.append(line2)
        
clu_imfor = (seq[0]+['\n']+seq[1]+['\n']+seq[7]+['\n']+seq[8]+['\n'])
line4 = ''.join(str(e) for e in clu_imfor)
file.write(line4)
file.close()

with open(input_file_3, 'rt') as f:
    file = open("tamplate_imformation.pir","a")
    seq = list()
    clu_input = str()
    line5 = str()
    
    for line in f:
        line2 = line.split('\n')
        seq.append(line2)
        
clu_imfor = (seq[0]+['\n']+seq[1]+['\n']+seq[7]+['\n']+seq[8]+['\n'])
line4 = ''.join(str(e) for e in clu_imfor)
file.write(line4)
file.close()

