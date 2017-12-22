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
input_file_4 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\1KLU.txt"
input_file_5 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\3C5J.txt"
input_file_6 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\4X5W.txt"
input_file_7 = "C:\\Users\\bio608\\Documents\\GitHub\\xhr\\template_and_target_file\\SLA_IPD0006002"

with open(input_file_1, 'rt') as f:
    file = open("tamplate_imformation.pir","w")
    file2 = open("sequence_imformation.pir","w")
    seq = list()
    line4 = str()
    line5 = str()
    
    for line in f:
        line2 = line.split('\n');
        seq.append(line2)

tamp_imfor = (seq[0]+['\n']+seq[1]+['\n']+seq[7]+['\n']+seq[8]+['\n'])
tamp_seq_imfor = (seq[2]+['\n']+seq[3]+['\n']+seq[4]+['\n']+seq[9]+['\n']+seq[10]+['\n']+seq[11]+['\n'])
line4 = ''.join(str(e) for e in tamp_imfor)
line5 = ''.join(str(e) for e in tamp_seq_imfor)
file.write(line4)
file.close()
file2.write(line5)
file2.close()

with open(input_file_2, 'rt') as f:
    file = open("tamplate_imformation.pir","a")
    file2 = open("sequence_imformation.pir","a")
    seq = list()
    clu_input = str()
    line4 = str()
    line5 = str()
    
    for line in f:
        line2 = line.split('\n')
        seq.append(line2)
        
clu_imfor = (seq[0]+['\n']+seq[1]+['\n']+seq[7]+['\n']+seq[8]+['\n'])
tamp_seq_imfor = (seq[2]+['\n']+seq[3]+['\n']+seq[4]+['\n']+seq[9]+['\n']+seq[10]+['\n']+seq[11]+['\n'])
line4 = ''.join(str(e) for e in clu_imfor)
line5 = ''.join(str(e) for e in tamp_seq_imfor)
file.write(line4)
file.close()
file2.write(line5)
file2.close()

with open(input_file_3, 'rt') as f:
    file = open("tamplate_imformation.pir","a")
    file2 = open("sequence_imformation.pir","a")
    seq = list()
    clu_input = str()
    line4 = str()
    line5 = str()
    
    for line in f:
        line2 = line.split('\n')
        seq.append(line2)
        
clu_imfor = (seq[0]+['\n']+seq[1]+['\n']+seq[7]+['\n']+seq[8]+['\n'])
tamp_seq_imfor = (seq[2]+['\n']+seq[3]+['\n']+seq[4]+['\n']+seq[9]+['\n']+seq[10]+['\n']+seq[11]+['\n'])
line4 = ''.join(str(e) for e in clu_imfor)
line5 = ''.join(str(e) for e in tamp_seq_imfor)
file.write(line4)
file.close()
file2.write(line5)
file2.close()


def clustal_input_file_pir_plus_pir():
    with open ("tamplate_imformation.pir", "rt") as f:
        modeller_input_file_A_chain = open ("modeller_input_file_A_chain.txt", "w")
        modeller_input_file_B_chain = open ("modeller_input_file_B_chain.txt", "w")
        g = open ("sequence_imformation.pir", "rt")
        h = ''.join(str(e) for e in g)
        seq1 = list()
        seq2 = list()
        seq3 = str()
        for line in f:
            seq1.append(line)
        for line in h.split("*"):
            line = line.strip("\n")
            seq2.append(line)
    string1 = (seq1[0],seq2[0],"\n",seq1[4],seq2[2],"\n",seq1[8],seq2[4],"\n")
    string2 = (seq1[2],seq2[1],"\n",seq1[6],seq2[3],"\n",seq1[10],seq2[5],"\n")
    file_prepare_A_chain = ''.join(str(e) for e in string1)
    file_prepare_B_chain = ''.join(str(e) for e in string2)
    modeller_input_file_A_chain.write(file_prepare_A_chain)
    modeller_input_file_A_chain.close
    modeller_input_file_B_chain.write(file_prepare_B_chain)
    modeller_input_file_B_chain.close
        
        