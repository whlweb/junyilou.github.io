# -*- coding:utf-8 -*-
import requests, json, sys, datetime, os, time
def GetMiddleStr(content, startStr, endStr):
	startIndex = content.index(startStr)
	if startIndex>=0:
		startIndex += len(startStr)
	endIndex = content.index(endStr)
	return content[startIndex:endIndex]
storelist = list(range(50))
storelist = ['qibao', 'shanghaiiapm', 'wujiaochang', 'nanjingeast', 'pudong',
			'globalharbor', 'hongkongplaza', 'kunming', 'sanlitun', 'chinacentralmall',
			'chaoyangjoycity', 'wangfujing', 'xidanjoycity', 'mixcchengdu', 'taikoolichengdu',
			'tianjinjoycity', 'riverside66tianjin', 'galaxymall', 'parc66jinan', 'mixcqingdao',
			'parccentral', 'zhujiangnewtown', 'holidayplazashenzhen', 'mixcnanning', 'nanjingist',
			'nanjingjinmaoplace', 'wondercity', 'center66wuxi', 'mixczhengzhou', 'mixchangzhou',
			'westlake', 'xiamenlifestylecenter', 'thaihotplaza', 'olympia66dalian', 'parkland',
			'zhongjiejoycity', 'mixcshenyang', 'jiefangbei', 'mixcchongqing', 'paradisewalkchongqing']
def home():
	wAns = ""; wCount = 0; endl = "\n"; rpath = "/home/pi/Retail/"; nowDatetime = datetime.datetime.now()
	print nowDatetime.strftime("%Y-%m-%d %H:%M:%S") + " 开始检查:"
	for i in range(0, len(storelist)):
		html = requests.get('http://www.apple.com/cn/retail/' + storelist[i] + '/')
		jcount = html.text.count('@type": "Event'); noShow = False
		if jcount > 0:
			orgSource = html.text.replace("\n", "").replace("	", "")
			Mans = GetMiddleStr(orgSource, '<script type="application/ld+json">', '"price": "0"') + '"price": "0"' + '}' + '}' + ']}'
			jans = json.loads(Mans)
			gDate = jans["event"][0]["startDate"].replace("Z", "").split("T"); aDay = str(gDate[0])
			aDaytime = datetime.datetime.strptime(aDay, "%Y-%m-%d");
			ncDaytime = datetime.datetime(int(nowDatetime.strftime("%Y")), int(nowDatetime.strftime("%m")), int(nowDatetime.strftime("%d")))
			if (aDaytime - ncDaytime).days < 1: noShow = True
			wkChn = ["一", "二", "三", "四", "五", "六", "日"]
			todayWeekday = int(datetime.datetime.now().strftime("%w"))
			DayWeek = list(range(7))
			if todayWeekday != 0:
				for s in range(1, todayWeekday + 1):
					DayWeek[s - 1] = str(datetime.datetime.now() - datetime.timedelta(days = (todayWeekday - s - 7)))
				for e in range(todayWeekday, 8):
					DayWeek [e - 1] = str(datetime.datetime.now() + datetime.timedelta(days = (e - todayWeekday + 7)))
			else:
				for j in range(1, 8):
					DayWeek [j - 1] = str(datetime.datetime.now() - datetime.timedelta(days = (todayWeekday - j)))
			for r in range(0,7):
				if DayWeek[r].count(aDay) > 0: aDay = "下周" + wkChn [r]
			if len(aDay) > 9:
				OriaDay = datetime.datetime.strptime(str(gDate[0]), "%Y-%m-%d").strftime("%-m 月 %-d 日")
				aDay = OriaDay + " 星期" + wkChn[int(datetime.datetime.strptime(str(gDate[0]), "%Y-%m-%d").strftime("%w"))]
			aTotal = str(gDate[1]); aHour = int(aTotal[0] + aTotal[1]) + 8; aTime = aTotal.replace(aTotal[0] + aTotal[1], "")
			tAns = aDay + " " + str(aHour) + aTime
			reload(sys); sys.setdefaultencoding('utf-8')
			pAns = jans["address"]['name'] + "有新活动：" + jans["event"][0]["name"] + "，时间是 " + tAns
			wAns = wAns + jans["event"][0]["name"]; wCount += 1
			fb = open(rpath + "Event.md"); fcb = fb.read(); fb.close()
			nCheck = fcb.count(jans["event"][0]["name"])
			if noShow == False:
				if nCheck == 0:
					a='curl -X POST -H "x-instapush-appid: '; b='" -H "x-instapush-appsecret: '
					c='" -H "Content-Type: application/json" -d '; d="'"
					e='{"event":"raw","trackers":{"ans":"'; f=pAns
					g='"'; m='}'; n='}'; o="'"; p=' https://api.instapush.im/v1/post'
					AppID = "585e4e62a4c48a05d607b545"; AppSecret = "a32883f25245516940ea6b9f9b80fa54"
					finalOut = a+AppID+b+AppSecret+c+d+e+f+g+m+n+o+p; os.system(finalOut)
					AppID = "58e7a6f5a4c48aff6614b36c"; AppSecret = "6ca99600f849dbb0d9a296c29218929f"
					finalOut = a+AppID+b+AppSecret+c+d+e+f+g+m+n+o+p; os.system(finalOut)
					# GitHub users please notice: AppSecret only uses for private.
					print endl + pAns + " [推送]"
				else: print pAns + " [已经推送]"
	if wCount > 0:
		fc = open(rpath + "Event.md", "w")
		fc.write(wAns); fc.close()
while True:
	home(); print "Sleeping, interval will be 12 hrs."; time.sleep(43200) #12 hrs