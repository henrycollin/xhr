# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re, csv
def read_seq(fn):
    fn = input("Please enter your sequence.")
    with open (fn, 'rt') as f:
        seq = list()
        for line in f.readlines():
            if not re.match('>', line):
                for base in line:
                    if not base == '\n':
                        seq.append(base)
                        
                        
    return seq

print ("seq")


