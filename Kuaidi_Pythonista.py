# -*- coding:utf-8 -*-
import sys, json, urllib.request, urllib.error, urllib.parse, time, datetime, os, clipboard
import appex, ui

def blanker(a, b): print (a + " " + b)

def netTry(tryurl):
	try: response = urllib.request.urlopen(tryurl)
	except urllib.error.URLError: return "False"
	else: return response.read()

def autocomp(readid):
	aTry = netTry("https://www.kuaidi100.com/autonumber/autoComNum?text=" + readid)
	if aTry != "False":
		countp = aTry.count(b"comCode")
		if countp >= 2: return json.loads(aTry)["auto"][0]["comCode"]
		else: return "unknown"
	else: return "custom_network"

def home(readid):
	global retA, retB; retA = retB = ""
	comp = "auto"; statText = "在途"
	if comp == "auto": comp = autocomp(readid)
	if comp != "unknown":
		urlb = "https://www.kuaidi100.com/query?type=" + comp + "&postid=" + readid
		tryb = netTry(urlb)
		if tryb != "False":
			ansj = json.loads(tryb)
			comtext = {'yuantong': '圆通', 'yunda': '韵达', 
						'shunfeng': '顺丰', 'shentong': '申通', 
						'zhongtong': '中通', 'jd': '京东', 'ems': '邮政 EMS'}
			if ansj["status"] == "200":
				result = ansj["data"]
				realComp = comtext.get(ansj["com"], "其他") + "快递"
				fTime = result[0]["time"]
				fContent = result[0]["context"].replace(" 【", "【").replace("】 ", "】").replace(" （", "（").replace(" ）", ")")
				fContent = fContent.replace("( ", "(").replace(" )", ")").replace("【", "").replace("】", "").replace('"(点击查询电话)"', "")
				signCount = fContent.count("签收") + fContent.count("感谢") + fContent.count("代收") + fContent.count("取件")
				sendCount = fContent.count("派送") + fContent.count("派件") + fContent.count("准备") + fContent.count("正在")
				if signCount > 0 and (signCount - sendCount) > 0: statText = "[签收]";
				end = "更新于 " + fTime + "\n" + fContent
				retA = realComp + " " + readid; retB = end 
			else:
				blanker(readid, "returned code " + ansj["status"])
				if ansj["status"] == "400": 
					return ("[" + readid + " is currently using comp code '" + comp + "'.]")
		else: 
			return (readid, "failed connect")
	else:
		return (readid, "without company")
		
global retA, retB; retA = retB = ""
frm = ui.View(frame=(0,0,200,100), flex="h")

home(clipboard.get())
