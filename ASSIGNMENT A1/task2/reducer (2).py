#!/usr/bin/env python3

import sys

time_dict={}
for line in sys.stdin:
	line = line.strip()
	lis = line.split("%")
	if len(lis)!=3:
		continue
	timestamp=lis[0]
	humidity=lis[1]
	temperature=lis[2]
	if humidity=='nan' or temperature=='nan':
		continue	
	humid=float(humidity)
	temp=float(temperature)
	if 48.0<humid<54.0 and 20<temp<24:
		if timestamp not in time_dict:
			time_dict[timestamp]=0
		time_dict[timestamp]+=1
for i in time_dict:
	print(i+' '+str(time_dict[i]))
