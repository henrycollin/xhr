# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:20:09 2018

@author: bio608
"""
import os

Tamplate_txt_file = ("C:\\Users\\bio608\\Desktop\\Modeller_input_convertor\\Template_txt")
DATA_DIR = Tamplate_txt_file
Template_file_data_txt = []
#store_file = open ("Template__sequence_information.txt","rt")

for filename in os.listdir(DATA_DIR):
    print ("Loading: %s" % filename)
    Template_loadFile = open(os.path.join(DATA_DIR, filename), 'rt')
    Template_file_data_txt.append(Template_loadFile.read())
    Template_loadFile.close()

#def read_Template_seq():
    seq1 = list()
    seq2 = list()

    for items in Template_file_data_txt:
        item = ''.join(str(e) for e in items)
    for items in item.split(">"):
        seq2.append(items)
    seq3 = (seq2[3])
    for items in seq3.split("\n"):
        seq1.append(items)
    
    print (seq1)
    
    
            