#coding:utf-8
'''
Created on 2016-6-13
Python核心编程第二章 2-11
@author: gh
'''
while True:
    s=0
    c=int(raw_input('输入值(1为求和，2为求平均值，0 退出)：'))
    if c==1:
        for i in range(5):
            n=int(input('n%d=' % (i+1)))
            s+=n
        print(s)
    if  c==2:
        for i in range(5):
            n=int(input('n%d=' % (i+1)))
            s+=n
        print(float(s/5))
        
    if c==0:
        break
