# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:57:49 2018

@author: bio608
"""
import os

Tamplate_pir_file = ("C:\\Users\\bio608\\Desktop\\Modeller_input_convertor\\Template_pir")
DATA_DIR = Tamplate_pir_file
Template_file_data_pir = []

for filename in os.listdir(DATA_DIR):
    print ("Loading: %s" % filename)
    Template_loadFile = open(os.path.join(DATA_DIR, filename), 'rt')
    Template_file_data_pir.append(Template_loadFile.read())
    Template_loadFile.close()

##
    a_chain_ind = list()
    b_chain_ind = list()
    seq2 = list()

    for items in Template_file_data_pir:
        item = ''.join(str(e) for e in items)
    for items in item.split(">"):
        seq2.append(items)
    a_chain = (seq2[1])
    b_chain = (seq2[2])
    for items in a_chain.split("\n"):
        a_chain_ind.append(items)
    for item in b_chain.split("\n"):
        b_chain_ind.append(items)
        
    print (a_chain_ind)