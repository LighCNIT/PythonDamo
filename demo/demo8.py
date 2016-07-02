#coding:utf-8
'''
Created on 2016-7-2
文件操作
@author: gh
'''
import os
filename = raw_input('Enter file name:')
f = open(filename,'w+')
while True:
    aLine = raw_input("Enter a line('.' to quit): ")
    if aLine != '.':
        f.write('%s%s' %(aLine,os.linesep))  #os.linesep字符串给出当前平台使用的行终止符
    else:
        break
f.close()
