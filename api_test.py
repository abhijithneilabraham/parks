#!/usr/bin/python
import requests
import json
area = "United Kingdom"



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

keywordList = ["speaker", "interpreter", "singer", "food tester", "Design Thinker"]

for text in keywordList:
	url = "https://duunitori.fi/api/v1/5d3fc27dec93f5e5105e3443edfc421bb57c3603/jobentries?search="+text+"&format=json&city="+area
	r = requests.get(url)
	tempJson = json.loads(r.text)
	dataList1 = get5(tempJson['results'])

	headers = {"Referer": "https://wayncheng.github.io/jobba/",'Origin': 'https://wayncheng.github.io', "X-Requested-With*": "XMLHttpRequest"}		
	url = "https://cors-anywhere.herokuapp.com/http://service.dice.com/api/rest/jobsearch/v1/simple.json?text="+text+"&city="+area
	r = requests.get(url,headers=headers	)
	tempJson = json.loads(r.text)
	dataList2 = get5(tempJson['results'])
	

	print dataList1
	print " ---- "
	print dataList2
	
	break;
	pass
