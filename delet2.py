# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:38:37 2018

@author: bio608
"""

import os, sys

Tamplate_txt_file = ("C:\\Users\\bio608\\Desktop\\Modeller_input_convertor\\Template_txt")#input("Enter the path of your HLA sequences txt file (ex.C:Users\DesKtop\input_file.txt):")
Tamplate_pir_file = ("C:\\Users\\bio608\\Desktop\\Modeller_input_convertor\\Template_pir")#input("Enter the path of your HLA sequences pir file (ex.C:Users\DesKtop\input_file.pir):")
Target_txt_file = ("C:\\Users\\bio608\\Desktop\\Modeller_input_convertor\\Target_txt")#input("Enter the path of your SLA sequences txt file (ex.C:Users\DesKtop\input_file.txt):")

DATA_DIR = Tamplate_txt_file
Template_file_data_txt = []
for filename in os.listdir(DATA_DIR):
    print ("Loading: %s" % filename)
    Template_loadFile = open(os.path.join(DATA_DIR, filename), 'rt')
    Template_file_data_txt.append(Template_loadFile.read())
    Template_loadFile.close()
    
DATA_DIR = Tamplate_pir_file
Template_file_data_pir = []
for filename in os.listdir(DATA_DIR):
    print ("Loading: %s" % filename)
    Template_loadFile = open(os.path.join(DATA_DIR, filename), 'rt')
    Template_file_data_pir.append(Template_loadFile.read())
    Template_loadFile.close()

DATA_DIR = Target_txt_file
Target_file_data_txt = []
for filename in os.listdir(DATA_DIR):
    print ("Loading: %s" % filename)
    Target_loadFile = open(os.path.join(DATA_DIR, filename), 'rt')
    Target_file_data_txt.append(Target_loadFile.read())
    Target_loadFile.close()
    
def Template_file_data_txt_read_seq(Template_file_data_txt):
    Template_seq = []
    for item in Template_file_data_txt:            
        Template_seq.append(item)
    return (Template_seq)

    
output = read_seq(Template_file_data_txt)
print (output)