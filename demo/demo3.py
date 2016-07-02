#coding:utf-8
'''
Created on 2016-6-26
6-11
@author: gh
'''
def int2ip():
    ints = raw_input("Input int:")
    hexs = hex(int(ints))[2:]
    print len(hexs)
    while len(hexs) < 8:
        hexs = '0'+hexs
        ip1 = int(hexs[0]+hexs[1],16)
        ip2 = int(hexs[2]+hexs[3],16)
        ip3 = int(hexs[4]+hexs[5],16)
        ip4 = int(hexs[6]+hexs[7],16)
    return '%d-%d-%d-%d' %(ip1,ip2,ip3,ip4)

print int2ip()