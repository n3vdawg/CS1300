# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:44:26 2018

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
    not_trouble = []
    print("\t Trouble Courses")
    if troadd[0] < troadd[1]:
        print("\t \t Current Math Grade:", troadd[0], "Objective Math Grade:", troadd[1])
    else:
        not_trouble.append(troadd[0])
        not_trouble.append(troadd[1])
    if troadd[3] < troadd[4]:
        print("\t \t Current English Grade:", troadd[3], "Objective English Grade:", troadd[4])
    else:
        not_trouble.append(troadd[3])
        not_trouble.append(troadd[4])
    if troadd[6] < troadd[7]:
        print("\t \t Current History Grade:", troadd[6], "Objective History Grade:", troadd[7])
    else:
        not_trouble.append(troadd[6])
        not_trouble.append(troadd[7])
    if troadd[9] < troadd[10]:
        print("\t \t Current Science Grade:", troadd[9], "Objective Science Grade:", troadd[10])
    else:
        not_trouble.append(troadd[9])
        not_trouble.append(troadd[10])   
    if troadd[12] < troadd[13]:
        print("\t \t Current Language Grade:", troadd[12], "Objective Language Grade:", troadd[13])
    else:
        not_trouble.append(troadd[12])
        not_trouble.append(troadd[13])
    
    has_concern(not_trouble)
    
    return    

def has_concern(conadd):
    
    
    """print("\t Trouble Courses")
    if conadd[0] < conadd[1]:
        print("\t \t Current Math Grade:", conadd[0], "Objective Math Grade:", conadd[1])
    else:
        not_trouble.append(conadd[0])
        not_trouble.append(conadd[1])
    if conadd[3] < conadd[4]:
        print("\t \t Current English Grade:", conadd[3], "Objective English Grade:", conadd[4])
    else:
        not_trouble.append(conadd[3])
        not_trouble.append(conadd[4])
    if conadd[6] < conadd[7]:
        print("\t \t Current History Grade:", conadd[6], "Objective History Grade:", conadd[7])
    else:
        not_trouble.append(conadd[6])
        not_trouble.append(conadd[7])
    if conadd[9] < conadd[10]:
        print("\t \t Current Science Grade:", conadd[9], "Objective Science Grade:", conadd[10])
    else:
        not_trouble.append(conadd[9])
        not_trouble.append(conadd[10])   
    if conadd[12] < conadd[13]:
        print("\t \t Current Language Grade:", troadd[12], "Objective Language Grade:", troadd[13])
    else:
        not_trouble.append(troadd[12])
        not_trouble.append(troadd[13])"""
    return
          
def add_tr(line):
    troadd = []
    for x in line[2:]:
        troadd.append(int(x))    
    has_trouble(troadd)
    
    return

def add_con(line):
    conadd = []
    for x in line[2:]:
        conadd.append(int(x))
    has_concern(conadd)
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
            add_con(line)
            add_tr(line)
        return
    
def main():

    student_name()
    
if __name__ == "__main__":     
    main()