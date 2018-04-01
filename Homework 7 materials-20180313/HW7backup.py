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
            trresult.append(0)
            trresult.append(0)
    #print(trresult)
    return trresult     

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
        else:
            conresult.append(0)
            conresult.append(0)
    #print(conresult)
    return conresult

def compare(concern, trouble):
    for i in range(len(concern)):
        if trouble[i] != 0:
            concern[i] = 0
    return concern
          
def add_tr(line):
    troadd = []
    for x in line[2:]:
        troadd.append(int(x))
    return has_trouble(troadd)

def add_con(line):
    conadd = []
    for x in line[2:]:
        conadd.append(int(x))
    return has_concern(conadd)

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
        grades = open('grades_report.txt', 'w')
        for line in student_list:
            result = line[:2]
            result = list(reversed(result))
            grades.write("Student name: " + result[0] + " " + result[1])
            concern_list = compare(add_con(line), add_tr(line))
            trouble_list = add_tr(line)
            grades.write("\t Concerning Courses:")
            concern_listCL = concern_list
            trouble_listCL = trouble_list
            concern_listCL = list(map(str, concern_listCL))
            trouble_listCL = list(map(str, trouble_listCL))
            for j in range(0, len(concern_list), 2):
                if concern_list[j] != 0:
                    if j == 0:
                        grades.write("\t \t Current Math Grade: " + concern_listCL[j] + " Current Math Warning: " + concern_listCL[j+1])
                    if j == 2:
                        grades.write("\t \t Current English Grade: " + concern_listCL[j] + " Current English Warning: " + concern_listCL[j+1])
                    if j == 4:
                        grades.write("\t \t Current History Grade: " + concern_listCL[j] + " Current History Warning: " + concern_listCL[j+1])
                    if j == 6:
                        grades.write("\t \t Current Science Grade: " + concern_listCL[j] + " Current Science Warning: " + concern_listCL[j+1])
                    if j == 8:
                        grades.write("\t \t Current Language Grade: " + concern_listCL[j] + " Current Language Warning: " + concern_listCL[j+1])
            
            grades.write("\t Trouble Courses:")
            for j in range(0, len(trouble_list), 2):
                if trouble_list[j] != 0:
                    if j == 0:
                        grades.write("\t \t Current Math Grade: " + trouble_listCL[j] + " Current Math Objective: " + trouble_listCL[j+1])
                    if j == 2:
                        grades.write("\t \t Current English Grade: " + trouble_listCL[j] + " Current English Objective: " + trouble_listCL[j+1])
                    if j == 4:
                        grades.write("\t \t Current History Grade: " + trouble_listCL[j] + " Current History Objective: " + trouble_listCL[j+1])
                    if j == 6:
                        grades.write("\t \t Current Science Grade: " + trouble_listCL[j] + " Current Science Objective: " + trouble_listCL[j+1])
                    if j == 8:
                        grades.write("\t \t Current Language Grade: " + trouble_listCL[j] + " Current Language Objective: " + trouble_listCL[j+1])
        grades.close()
        return
    
def main():
    
    
    student_name()
    
    
if __name__ == "__main__":     
    main()