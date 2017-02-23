# -*- coding:utf-8 -*-
import time, urllib2, json
def pytry(tryurl):
	try: response = urllib2.urlopen(tryurl)
	except urllib2.URLError as err: 
		if hasattr(err, 'reason') or hasattr(err, 'code'): return "False"
	else: return response.read()
tier = tmer = list(range(9)); classNote = {}
tmer[0] = "0725"; tmer[1] = "0840"; tmer[2] = "0945"; tmer[3] = "1035"; tmer[4] = "1125"; tmer[5] = "1400"; tmer[6] = "1525"
while True:
	tierNow = tierNote = ""
	nTime = time.strftime("%W.%w", time.localtime()); rTime = time.strftime("%H:%M", time.localtime()); mTime = rTime.replace(":", "")
	if len(mTime) == 3: mTime = "0" + mTime
	yWeek = int(nTime.split(".")[0]); wkDay = int(nTime.split(".")[1])
	if wkDay == 1:
		tier[0] = "数学"; tier[1] = "语文"; tier[2] = "英语"; tier[5] = "物理"; tier[6] = "化学"
		if (yWeek % 2) == 0 : tier[3] = tier[4] = "信息"
		else: tier[3] = tier[4] = "音乐"
	if wkDay == 2:
		tier[0] = "物理"; tier[1] = "英语"; tier[2] = "数学"; tier[3] = "地理"; tier[4] = "化学"; tier[5] = "语文"; tier[6] = "历史"
	if wkDay == 3:
		tier[0] = "英语"; tier[1] = "化学"; tier[2] = "语文"; tier[4] = "政治"; tier[5] = "物理"
	if wkDay == 4:
		tier[0] = "化学"; tier[1] = "英语"; tier[2] = "数学"; tier[4] = "语文"; tier[5] = "乒乓"; tier[6] = "物理"
	if wkDay == 5:
		tier[0] = "英语"; tier[3] = "数学"; tier[5] = "语文"
	classNote = {"语文": "下一节课为语文", "数学": "即将王者归来", "英语": "Learning & beliving", "政治": "你的开车可能需要电脑", "物理": "接下来要上的是一节物理课", "化学": "反应条件为电脑", "乒乓": "现在尝试寻找乒乓球拍", "地理": "地理课，本节可能需要电脑", "历史": "历史课，本节可能需要电脑"}
	for l in range(0,7):
		if mTime == tmer[l]:
			tierCount = len(tier[l])
			if tierCount > 1:
				tierNow = tier[l]; noteNow = classNote.get(tierNow)
			tmer[l] = ""
	urlA = "https://free-api.heweather.com/v5/hourly?city=chongqing&key=d61e87edd43242f8ba4e161b78dfee8d"; trya = pytry(urlA)
