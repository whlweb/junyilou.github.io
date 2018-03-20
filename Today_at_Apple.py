#-*- coding:utf-8 -*-
import os, urllib2, sys, json, platform

filename = ['wangfujing', 'taikoolichengdu', 'jiefangbei', 'olympia66dalian', 'thaihotplaza',
			'parccentral', 'westlake', 'parc66jinan', 'kunming', 'nanjingist', 'mixcnanning',
			'tianyisquare', 'mixcqingdao', 'nanjingeast', 'zhongjiejoycity', 'holidayplazashenzhen',
			'riverside66tianjin', 'center66wuxi', 'xiamenlifestylecenter', 'mixczhengzhou']
cityname = ['北京', '成都', '重庆', '大连', '福州', '广州', '杭州', '济南', '昆明', '南京', 
			'南宁', '宁波', '青岛', '上海', '沈阳', '深圳', '天津', '无锡', '厦门', '郑州']
fullCity = ""; num = len(filename); checksum = list(range(num))
for u in range(0, num): checksum[u] = 0

if "Linux" in platform.platform(): rpath = os.path.expanduser('~') + "/Retail/"
if "Darwin" in platform.platform(): rpath = os.path.expanduser('~') + "/Downloads/Apple/Raspberry/"
for f in range(0, num): fullCity = fullCity + cityname[f] + "、"
fullCity = fullCity.replace(cityname[num - 1] + "、", cityname[num - 1])
masterKey = "bKwiDtPPRP6sY943piQKbd"

def down(fname): os.system("wget -t 0 -T 3 -O " + rpath + fname + ".json --no-check-certificate https://www.apple.com/cn/today/static/data/store/" + fname + ".json")
def home():
	wAns = ""; mOpen = open(rpath + "Event.md"); mark = mOpen.read(); mOpen.close()
	for d in range(0, num): 
		down(filename[d])
		while os.path.getsize(rpath + filename[d] + ".json") == 0: down(filename[d])
	for i in range(0, num):
		rOpen = open(rpath + filename[i] + ".json"); raw = rOpen.read(); rOpen.close(); rJson = json.loads(raw)["courses"]
		for lct in range(0, len(rJson)):
			singleName = rJson[lct]["shortName"]
			if not singleName in mark and not singleName in wAns: 
				wAns = wAns + singleName + ",\n"; citAns = cityname[i]
				for r in range(i, num):
					eOpen = open(rpath + filename[r] + ".json"); eAns = eOpen.read(); eOpen.close(); eJson = json.loads(eAns)["courses"]
					for ect in range(0, len(eJson)):
						if eJson[ect]["shortName"] == singleName and not cityname[r] in citAns:
							citAns += "、" + cityname[r]
				if fullCity in citAns: citAns = "全中国大陆"
				pushAns = "Apple 在" + citAns + "有新活动: " + singleName; pushed = 0
				pushAns = pushAns.replace('"', "").replace("'", "").replace("：", " - ")
				for pc in range(0, num):
					if cityname[pc] in pushAns: checksum[pc] += 1
				os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1=" +
					pushAns + "&value2=Today at Apple 新活动&value3=" + rJson[lct]["image"] +
					"?output-format=jpg' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey)
				os.system("rm -f " + masterKey + "*")
				# GitHub users please notice: IFTTT Key only uses for private.
	mWrite = open(rpath + "Event.md", "w"); mWrite.write(mark + wAns); mWrite.close()

reload(sys); sys.setdefaultencoding('utf-8'); home()
for f in range(0, num): 
	if checksum[f] == 0: print "Apple 在" + cityname[f] + "没有新活动。"
	os.system("rm " + rpath + filename[f] + ".json")
	os.system("rm -f " + masterKey + "*")