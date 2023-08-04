#!/usr/bin/env python3

import sys

# dict={}
for line in sys.stdin:
    if line[0]!='#':
        try:
            node1,node2=line.strip().split()
            node1=node1.strip()
            node2=node2.strip()
        except:
            continue
        print(node1,node2,sep=',')
