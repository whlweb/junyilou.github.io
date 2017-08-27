#-*- coding:utf-8 -*-
import os, urllib2, sys, json, platform

filename = ['nanjingeast', 'kunming', 'wangfujing', 'taikoolichengdu', 'riverside66tianjin',
			'parc66jinan', 'mixcqingdao', 'parccentral', 'holidayplazashenzhen', 'mixcnanning',
			'nanjingist', 'center66wuxi', 'mixczhengzhou', 'westlake', 'xiamenlifestylecenter',
			'thaihotplaza', 'olympia66dalian', 'zhongjiejoycity', 'jiefangbei']
cityname = ['上海', '昆明', '北京', '成都', '天津', '济南', '青岛', '广州', '深圳', '南宁', '南京', '无锡',
			'郑州', '杭州', '厦门', '福州', '大连', '沈阳', '重庆']; fullCity = ""; num = len(filename)

if "Linux" in platform.platform(): rpath = os.path.expanduser('~') + "/Retail/"
if "Darwin" in platform.platform(): rpath = os.path.expanduser('~') + "/Downloads/Apple/Raspberry/"
for f in range(0, num): fullCity = fullCity + cityname[f] + "、"
fullCity = fullCity.replace(cityname[num - 1] + "、", cityname[num - 1])

def home():
	wAns = ""; wCount = 0
	for rm in range(0, num): os.system("rm " + rpath + filename[rm] + ".json")
	mOpen = open(rpath + "Event.md"); mark = mOpen.read(); mOpen.close()
	for d in range(0, num): 
		os.system("wget -t 0 -T 3 -P " + rpath + " --no-check-certificate " + 
			"https://www.apple.com/cn/today/static/data/store/" + filename[d] + ".json");
	for i in range(0, num):
		rOpen = open(rpath + filename[i] + ".json"); raw = rOpen.read(); rOpen.close(); rJson = json.loads(raw)["courses"]
		for lct in range(0, len(rJson)):
			singleName = rJson[lct]["shortName"]
			reload(sys); sys.setdefaultencoding('utf-8')
			if not singleName in mark and not singleName in wAns: 
				wAns = wAns + singleName + ",\n"; citAns = cityname[i]
				for r in range(i, num):
					eOpen = open(rpath + filename[r] + ".json"); eAns = eOpen.read(); eOpen.close(); eJson = json.loads(eAns)["courses"]
					for ect in range(0, len(eJson)):
						if eJson[ect]["shortName"] == singleName and not cityname[r] in citAns:
							citAns += "、" + cityname[r]
				if fullCity in citAns: citAns = "全中国大陆"
				pushAns = "Apple 在" + citAns + "有新活动: " + singleName + " " + rJson[lct]["image"]; print pushAns
				os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1="
					+ pushAns + "' https://maker.ifttt.com/trigger/today/with/key/dJ4B3uIsxyedsXeQKk_D3x")
			# GitHub users please notice: IFTTT Key only uses for private.
	mWrite = open(rpath + "Event.md", "w"); mWrite.write(mark + wAns); mWrite.close()

home()