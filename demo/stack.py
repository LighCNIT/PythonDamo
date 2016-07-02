#coding:utf-8
'''
Created on 2016-6-28
简单堆栈实现
@author: gh
'''
from random import choice

stack = []
def pushit():
    stack.append(raw_input('Enter New String:').strip())
    
def popit():
    if len(stack) == 0:
        print 'Cannot pop from empty stack!'
    else:
        print 'Removed [', `stack.pop()` ,']'
        
def viewstack():
    print stack
    
CMDS = {'u':pushit,'o':popit,'v':viewstack}

def showmenu():
    pr = """
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    
    Enter choice: """
    
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except(EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'
            print '\n You picked: [%s]' %choice
            if choice not in 'uovq':
                print 'Invalid option,try again'
            else:
                break
        if choice == 'q':
            break
        CMDS[choice]()

if __name__ == '__main__':
    showmenu()
    