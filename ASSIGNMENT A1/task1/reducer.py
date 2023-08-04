#!/usr/bin/env python3

import sys

curr_date = ""
curr_tally = 0
date = ""

for line in sys.stdin:
	line = line.strip()
	date, tally = line.split('\t', 1)
	
	try:
		tally = int(tally)
	except ValueError:
		continue
		
	if curr_date == date:
		curr_tally += tally
	else:
		if curr_date:
			print(curr_date + " " + (str)(curr_tally))
		curr_tally = tally
		curr_date = date

if curr_date == date:
    	print(curr_date + " " + (str)(curr_tally))
