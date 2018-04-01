# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 11:21:41 2018

@author: Tyler
"""

import csv

#these should be constant
MATH_CUR = 0
MATH_OBJ = 1
MATH_WAR = 2
ENG_CUR = 3
ENG_OBJ = 4
ENG_WAR = 5
HST_CUR = 6
HST_OBJ = 7
HST_WAR = 8
SCI_CUR = 9
SCI_OBJ = 10
SCI_WAR = 11
LANG_CUR = 12
LANG_OBJ = 13
LANG_WAR = 14

CUR_LIST = [MATH_CUR, ENG_CUR, HST_CUR, SCI_CUR, LANG_CUR]


def has_trouble(troadd):
    tro_list = [MATH_OBJ, ENG_OBJ, HST_OBJ, SCI_OBJ, LANG_OBJ]
    trresult = []
    for i in range(len(tro_list)):
        tro_idx = tro_list[i]
        cur_idx = CUR_LIST[i]
        t = troadd[tro_idx]
        c = troadd[cur_idx]
        if c < t:
            trresult.append(c)
            trresult.append(t)
        else:
            add_con(troadd)
    print(trresult)
    return #trresult     

def has_concern(conadd):
    conresult = []
    war_list = [MATH_WAR, ENG_WAR, HST_WAR, SCI_WAR, LANG_WAR]
    for i in range(len(war_list)):
        war_idx = war_list[i]
        cur_idx = CUR_LIST[i]
        w = conadd[war_idx]
        c = conadd[cur_idx]
        if c < w:
            conresult.append(c)
            conresult.append(w)
    print(conresult)
    return #conresult
          
def add_tr(line):
    troadd = []
    for x in line[2:]:
        troadd.append(int(x))    
    has_trouble(troadd)
    
    return

def add_con(troadd):
    conadd = []
    #for x in line[2:]:
    has_concern(troadd)
    for x in troadd:
        conadd.append(int(x))    
    return

def student_name():
    """ 
    iterates through every student name, creates full name and
    inserts name into result. Then calls add functions to see
    what should be added depending on grades
    """
    with open('student_files.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        student_list = list(reader)
        result = []
        for line in student_list:
            result = line[:2]
            result = list(reversed(result))
            print("Student name:", result[0], result[1])
            add_tr(line)
        return
    
def main():

    student_name()
    
if __name__ == "__main__":     
    main()