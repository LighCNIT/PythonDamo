'''
Created on 2016-4-2

@author: gh
'''
'read File'
fname = raw_input("Enter filename:")
try:
    fobj = open(fname,'r')
except IOError,e:
    print "*** file open error:",e
else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()