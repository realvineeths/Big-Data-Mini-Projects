#!/usr/bin/env python3

import sys
import json

given_dst = float(sys.argv[1])**2
given_lat = float(sys.argv[2])
given_lng = float(sys.argv[3])
for line in sys.stdin:
    line = line.strip()
    data = json.loads(line)
    start_lat = data["lat"]
    start_lng = data["lon"]
    #if (start_lat != start_lat) or (start_lng != start_lng):
        #continue
    distance = (given_lat - start_lat)**2 + (given_lng - start_lng)**2
    #print(distance)
    if distance <= given_dst:
        #jload = post_request(start_lat, start_lng)
        #print(data)
        print(data["timestamp"], data["humidity"], data["temperature"],sep='%')
