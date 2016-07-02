'''
Created on 2016-3-29

@author: gh
'''
print abs(-4);
print 'Hello Python';

def foo():
    "This is a doc string"
    return True

user = raw_input('Enter login name: ');
print 'You login is',user

print -2*4 + 3 ** 2

pystr = 'Python'
print pystr[3:]

class FooClass(object):
    """ my very first class: FooClass """
    version = 0.1
    def __init__(self,nm = 'John Doe'):
        self.name = nm
        print 'Create a class instance for', nm
    def showname(self):
        print 'Your name is ',self.name
        print 'My name is ',self.__class__.__name__
    def showver(self):
        print self.version
    def addMe2Me(self,x):
        return x + x
    
fool = FooClass()
#print fool.showname();
print fool.showver();
#print fool.addMe2Me('xyz')

import sys
sys.stdout.write('Hello World! \n')
print sys.platform

