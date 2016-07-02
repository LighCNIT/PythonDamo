#coding:utf-8
'''
Created on 2016-7-2

@author: gh
'''
def showMaxFactor(num):
    count = num/2
    while count > 1:
        if num%count == 0:
#             print '%d 的最大公约数是: %s' %(num,count)
            break
        count -=1
    else:
        if num > 1:
            print num,'是素数'
        else:
            print num,'不是素数'

# for eachNum in range(1,100):
#     showMaxFactor(eachNum)
    
s = int(raw_input('请输入一个数字：'))
# for s in range(1,100):
showMaxFactor(s)