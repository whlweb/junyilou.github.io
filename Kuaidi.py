# -*- coding:utf-8 -*-
from __future__ import division
import os, sys, json, urllib2, datetime, fileinput
arg = 0
apikey = "2fb76bff2aa440eb" # Expired API key 7c97c766f5dccc09
for m in sys.argv[1:]: arg = arg + 1
if arg > 0 :
    parts = ["http://api.jisuapi.com/express/query?appkey=", apikey, "&type=auto&number=", sys.argv[1]]
else:
	exi = os.path.isfile("packages.txt")
	forloop = 1
	if not exi:
		fb = open("packages.txt", 'w')
		fb.close()
		exi = 1
	order = list(range(10))
	print
	for line in fileinput.input("packages.txt"):
		order[forloop] = int(line)
		forloop = forloop + 1
		pass
	if order[1] == 1 or order[1] == "":
		input("没有保存的运单, 将打开文本文档, 输入后按任意键继续...")
		print
		os.system("open ~/packages.txt")
		exit(0)
	if order[1] != "":
		print "已保存以下运单:"
		for j in range(1, forloop):
			print "[", j, "]", order[j]
		print "输入要查询的单号编号，输入0打开单号存储文件", 
		odinput = input()
		if not odinput:
			os.system("open ~/packages.txt")
			exit(0)
	parts = ["http://api.jisuapi.com/express/query?appkey=", apikey, "&type=auto&number=", str(order[odinput])]
url = ''.join(parts)
responce = urllib2.urlopen(url)
anst = responce.read()
ansj = json.loads(anst)
if ansj["status"] == "0":
	maxnum = anst.count("time")
	result = ansj["result"]["list"]
	newesttime = datetime.datetime.strptime(result[0]["time"], '%Y-%m-%d %H:%M:%S')
	lasttime = datetime.datetime.strptime(result[maxnum-1]["time"], '%Y-%m-%d %H:%M:%S')
	deliverystatus = ansj["result"]["deliverystatus"]
	deliverytitle = ["在途中", "派件中", "已签收", "派送失败"]
	if deliverystatus != "3":
		deltat = round((((datetime.datetime.now() - lasttime).seconds)/60/60)+24*((datetime.datetime.now() - lasttime).days), 1)
	else:
		deltat = round((((newesttime - lasttime).seconds)/60/60)+24*((newesttime - lasttime).days), 1)
	if deltat > 24:
		deltat = round(deltat / 24, 1)
		print "\n快递单号:", ansj["result"]["number"], " 公司代号:", ansj["result"]["type"], "用时约", deltat, "天 状态:", deliverytitle[int(deliverystatus)-1]
	else:
		print "\n快递单号:", ansj["result"]["number"], " 公司代号:", ansj["result"]["type"], "用时约", deltat, "小时 状态:", deliverytitle[int(deliverystatus)-1]
	for i in range(0, maxnum):
		print result[i]["time"], result[i]["status"]
else:
	print
	if ansj["status"] == "101": print "查询失败，Appkey为空"
	if ansj["status"] == "102": print "查询失败，Appkey过期"
	if ansj["status"] == "103": print "查询失败，Appkey权限错误"
	if ansj["status"] == "104": print "查询失败，请求超过此数限制"
	if ansj["status"] == "105": print "查询失败，IP地址被禁止"
	if ansj["status"] == "106": print "查询失败，IP地址超过请求限制"
	if ansj["status"] == "107": print "查询失败，API接口正在维护"
	if ansj["status"] == "108": print "查询失败，API接口已经停用"
	if ansj["status"] == "201": print "查询失败，快递单号为空"
	if ansj["status"] == "202": print "查询失败，快递公司为空"
	if ansj["status"] == "203": print "查询失败，快递公司不存在"
	if ansj["status"] == "204": print "查询失败，自动识别快递公司失败"
	if ansj["status"] == "205": print "查询失败，暂未更新物流信息"
print