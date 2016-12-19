#-*- coding:utf-8 -*-

import json
import re
import copy
import os

# list=[1,2,3,4,5]
# a=2
# if a not in list:
#     print 'ok'
# else:
#     print 'in'

# str1=r'aa'
# str2=r'bb'
# str3=str1+'//'+str2
# print str3

# def capture_class(path):
#     with open(path,'r') as f:
#         str = f.read()
#     f.close()
#     print str
#     llist = re.findall(r'AccountSearchResultModel',str)
#     print llist
#
# path = 'C:\\Users\\kellanyuan\\Desktop\\AccountSearchResultModel.m'
# capture_class(path)

# str=r'- (QQCondFitUserModel *) toFitUserModel {  [CYHTest _insertFunc:@"CYH.class_AccountSearchResultModel.-toFitUserModel"];'
# num=re.findall(r'AccountSearchResultModel',str)
# print num

# list1=[1,2,3]
# list2=list1[:]
# list1[0]=0
# print list1
# print list2

# path ='C:\\Users\\kellanyuan\\Desktop'
# ll=os.listdir(path+'\\'+'aaa')
# print ll

# lll = [1,2,3]
# lll.remove(lll[1])
# print lll

path = '/Users/yuan/Desktop/123.txt'
with open(path,'r') as f:
    str = f.read()
f.close()
#print str
list1 = re.split(r';',str)
print len(list1)
print list1

print '123'+'\n'+'23'