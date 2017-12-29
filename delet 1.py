# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:20:29 2017

@author: bio608
"""

import re, os
#input_file = input("Enter the path of your HLA.txt sequence file (ex.C:Users\Desttop\input_file.txt):")
#with open (input_file, "r+") as f:
input_file_4 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\1KLU.txt"
input_file_5 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\3C5J.txt"
input_file_6 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\4X5W.txt"
input_file_7 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\testfile.txt"


with open(input_file_4, 'rt') as f:
    file = open("testfile.txt", "w")
    seq1 = list()
    seq2 = list()
    #select_c = "C|PDBID"
    
    for line1 in f.readlines():
        seq1.append(line1)
    seq1 = ''.join(str(e) for e in seq1)
    for line3 in seq1.split(">"):
        seq2.append(line3)

with open(input_file_5, 'rt') as f:
    file = open("testfile.txt", "a")
    seq3 = list()
    seq4 = list()
    #select_c = "C|PDBID"
    
    for line1 in f.readlines():
        seq3.append(line1)
    seq3 = ''.join(str(e) for e in seq3)
    for line3 in seq3.split(">"):
        seq4.append(line3)

with open(input_file_6, 'rt') as f:
    file = open("testfile.txt", "a")
    seq5 = list()
    seq6 = list()
    #select_c = "C|PDBID"
    
    for line1 in f.readlines():
        seq5.append(line1)
    seq5 = ''.join(str(e) for e in seq5)
    for line3 in seq5.split(">"):
        seq6.append(line3)

#1KLU_c_chain = seq2[3]
#3C5J_c_chain = seq4[3]
#4X5W_c_chain = seq6[3]
#file.write(seqoutput)
#file.close()

print (seq2[3])

