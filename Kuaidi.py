# -*- coding:utf-8 -*-
from __future__ import division
import sys, json, urllib2
arg = 0
for m in sys.argv[1:]: arg = arg + 1
if arg < 1:
	print "需要参数"
	exit()
for dovision in range(1, arg + 1):
	url = ''.join(["http://api.jisuapi.com/express/query?appkey=2fb76bff2aa440eb&type=auto&number=", sys.argv[dovision]])
	responce = urllib2.urlopen(url)
	anst = responce.read(); ansj = json.loads(anst)
	if ansj["status"] == "0":
		maxnum = anst.count("time")
		result = ansj["result"]["list"]
		deliverystatus = ansj["result"]["deliverystatus"]
		deliverytitle = ["在途中", "派件中", "已签收", "派送失败"]
		print "\n快递单号:", ansj["result"]["number"], " 公司代号:", ansj["result"]["type"], "状态:", deliverytitle[int(deliverystatus)-1]
		for i in range(0, maxnum): print result[i]["time"], result[i]["status"]
	else:
		erstat = int(ansj["status"])
		print sys.argv[dovision], " ",
		contact = "API错误"
		if erstat > 100 and erstat < 105: print contact
		else: 
			if erstat > 200 and erstat < 204: print contact
			else: 
				print "快件错误"
	dovision += 1
print