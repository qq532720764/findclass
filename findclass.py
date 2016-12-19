#-*- coding:utf-8 -*-

import json
import re
import copy
import os
import time

def capture_class(path):
    with open(path,'r') as f:
        str = f.read()
    f.close()
    #print str
    list1 = re.split(r';',str)
    #print len(list1)
    #print list1
    list2 = []
    for i in range(0,len(list1)):
        if re.search(r'(?<=class_).+?(?=\.)',list1[i]):
            classname = re.search(r'(?<=class_).+?(?=\.)',list1[i]).group()
            if classname not in list2:
                list2.append(classname)
    print len(list2)
    #print list2
    return list2

def match(path,classname):
    with open(path,'r') as f:
        str = f.read()
    f.close()
    list = re.findall(classname,str)
    if len(list) > 0:
        result = 1
    else:
        result = 0
    return result

def filter(path,list_class):
    list_file = os.listdir(path)
    list_result = list_file[:]
    for i in range(0,len(list_file)):
        path_file = path+'/'+list_file[i]
        analyzeresult = 0
        for classname in list_class:
            analyzeresult = match(path_file,classname)
            if analyzeresult == 1:
                break
        if analyzeresult == 1:
            analyzeresult = 0
            list_result.remove(list_file[i])
    return list_result

path1 = '/Users/yuan/Desktop/345.txt'
path2 = '/Users/yuan/Desktop/m_file'
list_class = capture_class(path1)
list_result = filter(path2,list_class)
print list_result
