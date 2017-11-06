# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

###read sequence and input 
import re, csv

def read_seq(fn):
    with open(fn, 'rt') as f:
         seq = list()
         for line in f.readlines():
             if not re.match('>', line):
                for base in line:
                   if not base == '\n':
                      seq.append(base)
                      #print (seq)
                        
    return seq


##print test
#file = "TP53.txt"
#seq = read_seq(file)
#print (''.join(seq), '\n')

###complementary sequence bases method 1
def complementary_seq1(seq):
    total = list()
    for base in seq:
        if base == "A":
           total.append("T")
        if base == "T":
           total.append("A")
        if base == "C":
           total.append("G")
        if base == "G":
           total.append("C")
        if base == "a":
           total.append("t")
        if base == "t":
           total.append("a")
        if base == "c":
           total.append("g")
        if base == "g":
           total.append("c")
    return total
    
##print test   
file = "TP53.txt"
seq = read_seq(file)
c_seq = complementary_seq1(seq)
print (''.join(c_seq))

###complementary sequence bases method 2
def complementary_seq2(seq):
    c_seq = list()
    c_table = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'a':'t', 't':'a', 'c':'g', 'g':'c'}
    for base in seq:
        c_seq.append(c_table[base])
    
    return c_seq
    
##print test    
#file = "TP53.txt"
#seq = read_seq(file)
#c_seq = complementary_seq1(seq)
#print (''.join(c_seq))
    
    
###translat the sequence
