#!/usr/bin/env python3

import sys
import json
	
for row in sys.stdin:
	row = json.loads(row.strip())
	
	if row['location']>1700 and row['location']<2500 and row['sensor_id']<5000 and row['pressure']>=93500.00 and row['humidity']>=72.00 and row['temperature']>=12.00:
		print(row['timestamp'] + "\t1")
