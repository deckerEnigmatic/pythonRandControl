#!/root/scripts/plant/plant_env/bin/python
# 2021 - Enigaticdevices.com
# written for Python3

import subprocess
import json
import urllib.request
import time
from time import strftime 
from time import sleep

def getRandom(l,h):
	#print(l)
	#print(h)
	restEndpoint = "http://192.168.1.133:5000/rangeInt/"+l+"/"+h
	getnum = json.load(urllib.request.urlopen(restEndpoint))
	output = getnum[0]["value"]
	return output


def logWrite(rand_select,exper):
	dtime = strftime("%m-%d-%Y %H:%M:%S")
	logfile.write(dtime+" rand_select="+str(rand_select)+" exper_num="+str(exper_num)+"\n")
	
## of positions
low_range = '1'
high_range = '4'

exper_num = 9 

## slow script speed
sleep_factor = 5 

## open log

loghandle = '/root/scripts/plant/control.log' 
logfile = open(loghandle, "a")


count = 0
while count < 1:

	x=int(getRandom(low_range,high_range))
	print(x)
	logWrite(x,exper_num)
	sleep(sleep_factor)
