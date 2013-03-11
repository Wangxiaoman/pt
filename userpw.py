#!/usr/bin/python
#-*-coding:utf-8-*-

'''
Created on 2013-2-25

@author: wang_xm
'''

db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = "name tabken,try another"
            continue
        else:
            break
    pwd = raw_input('password:')
    db[name] = pwd
 
def olduser():
    name = raw_input('login:')
    pwd = raw_input('password:')
    password = db[name]
    if pwd == password:
        print 'welcom back',name
    else:
        print 'login incorrect~'
        
Methods = {'n':newuser,'e':olduser}        

def showMenu():
    prompt = '''
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice:'''
    while True:
        try:
            choice = raw_input(prompt).strip().lower()
        except (EOFError,KeyboardInterrupt):
            choice='q'
        print 'your choice is ',choice
        if choice not in 'neq':
            print 'invalid option, try again~'
        else:
            if choice == 'q':
                break
            Methods[choice]();


if __name__ == '__main__':
    showMenu();