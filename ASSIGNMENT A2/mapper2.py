#!/usr/bin/env python3
import json

import sys

def prod(vec1, vec2):
    
    ans = 0.0
    ans += (vec1[0] * vec2[0])
    ans += (vec1[1] * vec2[1])
    ans += (vec1[2] * vec2[2])
    ans += (vec1[3] * vec2[3])
    ans += (vec1[4] * vec2[4])
    ans += (vec1[5] * vec2[5])

    return ans


def similarity(vec1, vec2,cache):
    
    x =  prod(vec1, vec2) 
    y = x/((cache + norm_vector1(vec2)) -x)
    return y

def norm_vector1(vec):
    
    mag = 0.0
    mag+=vec[0]**2
    mag+= vec[1]**2
    mag+= vec[2]**2
    mag+= vec[3]**2
    mag+= vec[4]**2
    mag+= vec[5]**2
    return (mag)

def norm_vector2(vec):
    
    mag = 0.0
    mag+=vec[0]**2
    mag+= vec[1]**2
    mag+= vec[2]**2
    mag+= vec[3]**2
    mag+= vec[4]**2
    mag+= vec[5]**2
    return (mag)

def contribution(p, vec2, n, v, emb_vector,cache):

    vec1 = emb_vector[p]
    return similarity(vec1, vec2,cache) * (v[p] / n)

    
w_file = open(sys.argv[1], 'r') #w.txt

embed_file = open(sys.argv[2], 'r') #page_embedding.json

emb_vector = json.load(embed_file)
dict = {}

for temp in w_file:
    temp=temp.strip()
    p, rank = temp.split(',')
    print(p,0.0,sep='\t')
    dict[p] = float(rank)

for line in sys.stdin:
    p, adj_list = line.strip().split('\t')
    adj_list = eval(adj_list)

    num = float(len(adj_list))
    cache=norm_vector2(emb_vector[p])
    for q in adj_list:  
        vec2=emb_vector[str(q)]
        print(str(q), contribution(p,vec2 , num, dict, emb_vector,cache), sep='\t')


w_file.close()
embed_file.close()
