# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:20:09 2018

@author: bio608
"""
import os

Tamplate_txt_file = ("C:\\Users\\bio608\\Desktop\\Modeller_input_convertor\\Template_txt")
DATA_DIR = Tamplate_txt_file
Template_file_data_txt = []

for filename in os.listdir(DATA_DIR):
    print ("Loading: %s" % filename)
    Template_loadFile = open(os.path.join(DATA_DIR, filename), 'rt')
    Template_file_data_txt.append(Template_loadFile.read())
    Template_loadFile.close()

#def read_Template_seq():
    seq1 = list()
    for items in Template_file_data_txt:
        item = ''.join(str(e) for e in items)
    for items in item.split(">"):
        seq1.append(items)
    
    #tamp_imfor = (seq1[0],['\n'],seq1[1],['\n'],seq1[7],['\n'],seq1[8],['\n'])
    #tamp_seq_imfor = (seq1[2],['\n'],seq1[3],['\n'],seq1[4],['\n'],seq1[9],['\n'],seq1[10],['\n'],seq1[11],['\n'])
    #line4 = ''.join(str(e) for e in tamp_imfor)
    #line5 = ''.join(str(e) for e in tamp_seq_imfor)
    
    print (seq1[5])
            