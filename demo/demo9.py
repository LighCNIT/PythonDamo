#coding:utf-8
'''
Created on 2016-7-2
文件操作
@author: gh
'''
import os 
from tempfile import tempdir

# temDir = 'd:\\temp'
for temDir in ('d:\\temp'):
    if os.path.isdir(temDir):   #指定路径是否存在且为一个目录
        break
    else:
        print 'no temp directory avaiable'
        tempdir = ''
        
if temDir:
    os.chdir(temDir)  #创建目录
    cwd = os.getcwd() #返回当前目录
    print '*** current temporary directory'
    print cwd
    
    print 'creating example directory:'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working directory:'
    print cwd
    print '*** original directory listing:'
    print os.listdir(cwd) #列出指定目录的文件
    print '*** creating test file...'
    fobj = open('test','w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print '*** updated directory listing:'
    print os.listdir(cwd)
    
    print "*** renaming 'test' to 'filetest.txt'"
    os.rename('test', 'filetest.txt')
    print '*** updated directory listing:'
    print os.listdir(cwd)
    
    path = os.path.join(cwd,os.listdir(cwd)[0])
    print '*** full file pathname'
    print path 
    print '*** (pathname,basename) =='
    print os.path.split(path)  #返回[dirname(),basename()]元组
    print '*** (filename,extension) =='
    print os.path.splitext(os.path.basename(path)) #去掉目录路径，返回文件名
    
    print '*** displaying file contents: '
    fobj = open(path)
    for eachLine in fobj:
        print eachLine,
    fobj.close()
    
    print '*** deleting test file'
    os.remove(path)#删除文件
    print '*** updated directory listing: '
    print os.listdir(cwd)
    os.chdir(os.pardir)
    print '*** deleting test directory'
    os.rmdir('example')  #删除路径
    print '*** DONE'