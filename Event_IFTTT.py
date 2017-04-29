# -*- coding:utf-8 -*-
import requests, json, sys, datetime, os, time, re
def GetMiddleStr(content, startStr, endStr):
	startIndex = content.index(startStr)
	if startIndex >= 0: startIndex += len(startStr)
	endIndex = content.index(endStr)
	return content[startIndex:endIndex]
storelist = list(range(50))
storelist = ['@qibao', '@shanghaiiapm', '@wujiaochang', '@nanjingeast', '@pudong',
			'@globalharbor', '@hongkongplaza', '@kunming', '@sanlitun', '@chinacentralmall',
			'@chaoyangjoycity', '@wangfujing', '@xidanjoycity', '@mixcchengdu', '@taikoolichengdu',
			'@tianjinjoycity', '@riverside66tianjin', '@galaxymall', '@parc66jinan', '@mixcqingdao',
			'@parccentral', '@zhujiangnewtown', '@holidayplazashenzhen', '@mixcnanning', '@nanjingist',
			'@nanjingjinmaoplace', '@wondercity', '@center66wuxi', '@mixczhengzhou', '@mixchangzhou',
			'@westlake', '@xiamenlifestylecenter', '@thaihotplaza', '@olympia66dalian', '@parkland',
			'@zhongjiejoycity', '@mixcshenyang', '@jiefangbei', '@mixcchongqing', '@paradisewalkchongqing',
			'*apmhongkong', '*cantonroad', '*causewaybay', '*festivalwalk', '*ifcmall', '*newtownplaza', '#galaxymall']
def home():
	wAns = ""; wCount = 0; endl = "\n"; rpath = os.path.expanduser('~') + "/Retail/"; nowDatetime = datetime.datetime.now()
	print nowDatetime.strftime("%Y-%m-%d %H:%M:%S") + " 开始检查:"
	for i in range(0, len(storelist)):
		if storelist[i][0] == "*": regionCode = "hk"
		if storelist[i][0] == "#": regionCode = "mo"
		if storelist[i][0] == "@": regionCode = "cn"
		storelist[i] = storelist[i].replace("*", "").replace("#", "").replace("@", "")
		print "Checking web alias '" + storelist[i] + "' in region code '" + regionCode + "'."
		html = requests.get('https://www.apple.com/' + regionCode + '/retail/' + storelist[i] + '/')
		jcount = html.text.count('@type": "Event'); noShow = False
		if jcount > 0:
			orgSource = html.text.replace("\n", "").replace("	", "")
			Mans = GetMiddleStr(orgSource, '<script type="application/ld+json">', '"price": "0"') + '"price": "0"' + '}' + '}' + ']}'
			jans = json.loads(Mans)
			gDate = jans["event"][0]["startDate"].replace("Z", "").split("T"); aDay = str(gDate[0])
			aDaytime = datetime.datetime.strptime(aDay, "%Y-%m-%d");
			ncDaytime = datetime.datetime(int(nowDatetime.strftime("%Y")), int(nowDatetime.strftime("%m")), int(nowDatetime.strftime("%d")))
			if (aDaytime - ncDaytime).days < 1: noShow = True
			wkChn = ["一", "二", "三", "四", "五", "六", "日"]; masterWkChn = ["日", "一", "二", "三", "四", "五", "六"]
			todayWeekday = int(datetime.datetime.now().strftime("%w"))
			DayWeek = list(range(7)); NextWeek = list(range(7))
			if todayWeekday != 0: #下周
				for s in range(1, todayWeekday + 1): NextWeek[s - 1] = str(datetime.datetime.now() - datetime.timedelta(days = (todayWeekday - s - 7)))
				for e in range(todayWeekday, 8): NextWeek[e - 1] = str(datetime.datetime.now() + datetime.timedelta(days = (e - todayWeekday + 7)))
			else:
				for j in range(1, 8): NextWeek[j - 1] = str(datetime.datetime.now() - datetime.timedelta(days = (todayWeekday - j)))
			if todayWeekday != 0: #本周
				for s in range(1, todayWeekday + 1): DayWeek[s - 1] = str(datetime.datetime.now() - datetime.timedelta(days = (todayWeekday - s)))
				for e in range(todayWeekday, 8): DayWeek[e - 1] = str(datetime.datetime.now() + datetime.timedelta(days = (e - todayWeekday)))
			else:
				for j in range(1, 8): DayWeek[j - 1] = str(datetime.datetime.now() - datetime.timedelta(days = (todayWeekday - j + 7)))
			for r in range(0,7):
				if NextWeek[r].count(aDay) > 0: aDay = "下周" + wkChn [r]
				if DayWeek[r].count(aDay) > 0: aDay = "本周" + wkChn [r]
			if len(aDay) > 9:
				aDay = "星期" + masterWkChn[int(datetime.datetime.strptime(str(gDate[0]), "%Y-%m-%d").strftime("%w"))]
			OriaDay = datetime.datetime.strptime(str(gDate[0]), "%Y-%m-%d").strftime("%-m 月 %-d 日")
			aTotal = str(gDate[1]); aHour = int(aTotal[0] + aTotal[1]) + 8; aTime = aTotal.replace(aTotal[0] + aTotal[1], "")
			tAns = OriaDay + " " + aDay + " " + str(aHour) + aTime
			reload(sys); sys.setdefaultencoding('utf-8')
			pAns = "零售店活动 - " + jans["address"]['name'] + " 在 " + tAns + " 将开展活动「" + jans["event"][0]["name"] + "」"
			pAns = pAns.replace("00:00", "00").replace("15:00", "00").replace("30:00", "00").replace("45:00", "00")
			idURL = re.findall(r"\d+\.?\d*", jans["event"][0]["url"])
			EventID = idURL[len(idURL) - 1]; wAns = wAns + EventID + ", "; wCount += 1
			fb = open(rpath + "Event.md"); fcb = fb.read(); fb.close()
			nCheck = fcb.count(EventID)
			if noShow == False:
				if nCheck == 0:
					os.system('curl -X POST -H "Content-Type: application/json" -d' + "'" + '{"value1":"' + pAns + '"}' 
							   + "' https://maker.ifttt.com/trigger/raw/with/key/cMgQhRp4tZBhs3B2OreX07"); print
					simonStore = ['七宝', '上海环贸 iapm', '五角场', '南京东路', '浦东', '环球港', '香港广场', '杭州万象城', '西湖']
#					for s in range(0, len(simonStore)):
#						if pAns.count(simonStore[s]) > 0:
#							AppID = "58e7a6f5a4c48aff6614b36c"; AppSecret = "6ca99600f849dbb0d9a296c29218929f"
#							finalOut = a + AppID + b + AppSecret + c + d + e + f + g + m + n + o + p; os.system(finalOut)
					# GitHub users please notice: IFTTT Key only uses for private.
					print pAns + " [推送]"
				else: print pAns + " [已经推送]"
	if wCount > 0:
		fc = open(rpath + "Event.md", "w")
		fc.write(wAns); fc.close()
while True:
	home(); print "Sleeping, interval will be 12 hrs."; time.sleep(43200) #12 hrs