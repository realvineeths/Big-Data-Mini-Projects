#!/usr/bin/env python3
import sys

# store={}
file=open(sys.argv[1].strip(),"w")

prevnode=None
for line in sys.stdin:
    try:
        temp1,temp2=line.split(',')
        temp1=temp1.strip()
        temp2=temp2.strip()
    except:
        continue
    # print(temp1,temp2,sep='\t',end='')
    if prevnode==None:
        prevnode=temp1
        file.write(temp1+','+'1'+'\n')
        print(temp1,'\t[',temp2,sep='',end='')
        # print('[',temp2,end='')
    elif temp1==prevnode:
        print(', ',temp2,end='',sep='')
    else:
        print(']',sep='',end='\n')
        print(temp1,end='\t',sep='')
        print('[',temp2,end='',sep='')
        file.write(temp1+','+'1'+'\n')
        prevnode=temp1


print(']')
file.close()
