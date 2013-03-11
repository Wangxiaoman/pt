#!/usr/bin/python
#-*-coding:utf-8-*-
'''
Created on 2013-2-20

@author: wang_xm
'''

stack = []

def pushit():
    stack.append(raw_input("enter the element :").strip());
    
def popit():
    if len(stack)==0:
        print '''can't pop element !'''
    else:
        print 'remove',stack.pop()
        
def view():
    print stack
    
CMDs = {'u':pushit, 'o':popit, 'v':view}

def showMenu():
    pr = '''
P(U)sh
P(O)p 
(V)iew
(Q)uit

Enter your choice:'''
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except:
                choice='q'
            
            print '\n You picked : [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option, try agian~'
            else:
                break
        
        if choice == 'q':
            break
        CMDs[choice]()
        
if __name__ == '__main__':
    showMenu()        
           
            

