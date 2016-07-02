#coding:utf-8
'''
Created on 2016-6-14
python核心编程 3-12

@author: gh
'''
import os
ls=os.linesep
def write():
        while True:
            fname=raw_input('Enter file name:')
            if os.path.exists(fname):
                print('Error %s already exists ' % fname)
            else:
                break
        all=[]
        print("\nEnter lines ('.' by itself to quit).\n")
        while True:
            entry=raw_input('>')
            if entry=='.':
                break
            else:
                all.append(entry)
        fobj=open(fname,'w')
        fobj.writelines(['%s%s' % (x,ls) for x in all])
        fobj.close()
        print('Done')
        
def read():
        while True:
                fname=raw_input('Enter filename:')        
                if not os.path.exists(fname):
                        print('sorry,%s is not exists' % fname)
                else:
                        break
        try:
                fobj=open(fname,'r')
        except IOError as e:
                print("*** file open error" ,e)
        else:
                for eachline in fobj:
                        #print (eachline),
                        return eachline
        fobj.close()  
                
i = 0
while i!='q':
    i = raw_input("'r'read,'w',write,'rw','read and write','q'quite:")
    if i=='r':
        read()
    elif i=='w':
        write()
    elif i == 'rw':
        str = read()
        print str.decode("gbk")
        str = str + "哈啊哈"
        

    