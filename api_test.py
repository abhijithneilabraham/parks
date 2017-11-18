#!/usr/bin/python
import requests
import json
area = "United Kingdom"

headers = {"Referer": "https://wayncheng.github.io/jobba/",'Origin': 'https://wayncheng.github.io', "X-Requested-With*": "XMLHttpRequest"}	
keywordList = ["speaker", "interpreter", "singer", "food tester", "Design Thinker"]
for text in keywordList:
	# url = "https://cors-anywhere.herokuapp.com/http://service.dice.com/api/rest/jobsearch/v1/simple.json?text="+text+"&city="+area
	url = "https://duunitori.fi/api/v1/5d3fc27dec93f5e5105e3443edfc421bb57c3603/jobentries?search="+text+"&format=json&city="+area
	# url = "https://cors-anywhere.herokuapp.com/http://service.dice.com/api/rest/jobsearch/v1/simple.json?text="+text+"&city="+area
	
	r = requests.get(url,headers=headers	)
	print r.text
	# tempJson = json.loads(r.text)
	# print tempJson

	pass
