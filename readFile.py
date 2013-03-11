'''
Created on 2013-1-30

@author: wang_xm
'''

fileName = raw_input("input file name:")
fobj = open(fileName,'r')
for line in fobj:
    print line
    
