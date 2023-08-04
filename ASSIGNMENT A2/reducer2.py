#!/usr/bin/env python3

import sys

rank = lambda x: 0.34 + 0.57* x
# def rank(x):
#     return 0.34 + 0.57* x


prev_node = None

for line in sys.stdin:
    line = line.strip()

    source,contribution = line.split("\t")
    source = source.strip()
    contribution = float(contribution.strip())

    if prev_node is None:
        prev_pagerank = rank(contribution)
        prev_node = source


    elif prev_node == source:
        prev_pagerank += 0.57 * contribution

    else:
        print("{},{:.2f}".format(prev_node, prev_pagerank))
        prev_node = source
        prev_pagerank = rank(contribution)

print("{},{:.2f}".format(prev_node, prev_pagerank))