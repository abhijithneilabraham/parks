#!/usr/bin/python
import requests
import json
from random import shuffle

def get5( ar ):
	dataList = [] 
	i = 0
	for x in ar:
		i+=1 
		dataList.append( results )
		if ( i == 5 ):
			break
		pass
	return dataList

area = "United Kingdom"
keywordList = ["speaker", "interpreter", "teacher", "singer", "food tester", "Design Thinker"]
jobs = []

for text in keywordList:
	url = "https://duunitori.fi/api/v1/5d3fc27dec93f5e5105e3443edfc421bb57c3603/jobentries?search="+text+"&format=json&city="+area
	r = requests.get(url)
	tempJson = json.loads(r.text)
	jobs.append( get5(tempJson['results']) )
	pass

shuffle(jobs)
print jobs
