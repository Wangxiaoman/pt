#!/usr/bin/python
#-*-coding:utf-8-*-
'''Created on 2013-2-20

@author: wang_xm
'''

'''
print (1)
print (1,) #ֻ��һ���Ԫ���һ��','���������


person = ['name',['saving',1000]]
hubby = person[:]
wifey = list(person)

print [id(x) for x in (person,hubby,wifey)]

print [id(x) for x in hubby]
print [id(x) for x in wifey]

hubby[0]='joe'
wifey[0]='jane'
print hubby,wifey
print [id(x) for x in hubby]
print [id(x) for x in wifey]

hubby[1][1]=200

print hubby,wifey
print person 

print "abc" in "abadsfsabcwear123"
'''

#���ʯͷ��
list = ['����','ʯͷ','��']
def rechambeau(x,y):
    if x in list and y in list:
        if list.index(x)== list.index(y):
            print 'equals'
        elif list.index(x)-list.index(y)==1 or list.index(x)-list.index(y)==-2:
            print 'win'
        else:
            print 'lose'
    
    else:
        print 'valid input'

rechambeau('����','��')    
rechambeau('����','����')

rechambeau('ʯͷ','����')
rechambeau('����','����')

rechambeau('����','ʯͷ')
rechambeau('��','����')    



