#!/usr/bin/python
import requests
import json
from random import shuffle

def get5( ar ):
	dataList = [] 
	i = 0
	for x in ar:
		i+=1 
		dataList.append( x )
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
	if "results" in  tempJson:
		jobs.append( get5(tempJson['results']) )

	headers = {"Referer": "https://wayncheng.github.io/jobba/",'Origin': 'https://wayncheng.github.io', "X-Requested-With*": "XMLHttpRequest"}		
	url = "https://cors.now.sh/http://api.indeed.com/ads/apisearch?publisher=422492215893931&userip=1.2.3.4&useragent=Chrome&v=2&format=json&limit=50&q="+text+"&city="+area
	r = requests.get(url,headers=headers	)
	tempJson = json.loads(r.text)

	if "results" in  tempJson:
		jobs.append( get5(tempJson['results']) )

	pass

shuffle(jobs)
print jobs
