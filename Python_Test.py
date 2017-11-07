# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##### read sequence and input #####
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

##### complementary sequence bases method 1 #####
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
#file = "TP53.txt"
#seq = read_seq(file)
#c_seq = complementary_seq1(seq)
#print (''.join(c_seq))

##### complementary sequence bases method 2 #####
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
    
##### reverse sequence method 1 #####
##print test    
#file = "TP53.txt"
#seq = read_seq(file)
#c_seq = complementary_seq1(seq)
#rev_seq = reverse_seq(c_seq)
#print (''.join(rev_seq))
#print (c_seq[::-1])
    
##### reverse sequence method 2 #####
def reverse_seq2(c_seq):
    r = []
    for c in c_seq:
        r.insert(0, c)
    return r
##print test    
#file = "TP53.txt"
#seq = read_seq(file)
#c_seq = complementary_seq1(seq)
#reverse_seq = reverse_seq2(c_seq)
#print(''.join(reverse_seq))

##### reverse sequence method 3 #####
def reverse_seq3(c_seq):
    c_seq.reverse()
    
    return c_seq
##print test
#file = "TP53.txt"
#seq = read_seq(file)
#c_seq = complementary_seq1(seq)
#reverse_seq = reverse_seq3(c_seq)
#print(''.join(reverse_seq3))

##### read T_table #####
def read_t_table(fn):
    with open("T_table", "r") as f:
        t_table = dict()
        for words in csv.reader(f, delimiter = "\t"):
            t_table[words[0]] = {"one":words[1], "three":words[2]}
    return t_table
##print test
#print (''.join(read_t_table))

##### translat the sequence 3 aa in a group  #####
def translation_seq(seq):
    codons_total = list ()
    codons = [seq[i:i+3] for i in range(0, len(seq), 3)]
    codons_total += codons
    return codons_total
    #print (len(codons), "\t")
    #print (seq)
file = "TP53.txt"
seq = read_seq(file)
protein_seq = translation_seq(seq)
print (protein_seq)


    #protein_codon = list ()
    #for base in codons:
    #    protein_codon.append([t_table[base] for base in codons])
    #return 