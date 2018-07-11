#-*- coding:utf-8 -*-
import os, urllib2, sys, json, platform, time

filename = ['qibao', 'shanghaiiapm', 'wujiaochang', 'nanjingeast', 'pudong', 'globalharbor',
			 'hongkongplaza', 'kunming', 'sanlitun', 'chinacentralmall', 'chaoyangjoycity', 
			 'wangfujing', 'xidanjoycity', 'mixcchengdu', 'taikoolichengdu', 'tianjinjoycity',
			 'riverside66tianjin', 'galaxymall', 'parc66jinan', 'mixcqingdao', 'parccentral',
			 'zhujiangnewtown', 'holidayplazashenzhen', 'mixcnanning', 'nanjingist', 'nanjingjinmaoplace', 
			 'wondercity', 'center66wuxi', 'mixczhengzhou', 'tianyisquare', 'mixchangzhou', 
			 'westlake', 'xiamenlifestylecenter', 'thaihotplaza', 'olympia66dalian', 'parkland', 
			 'zhongjiejoycity', 'mixcshenyang', 'jiefangbei', 'mixcchongqing', 'paradisewalkchongqing',
			 'apmhongkong', 'cantonroad', 'causewaybay', 'festivalwalk', 'ifcmall', 'newtownplaza',
			 'galaxymacau', 'cotaicentral', 'taipei101']
cityname = ['上海', '上海', '上海', '上海', '上海', '上海', '上海', '昆明', '北京', '北京', '北京',
			'北京', '北京', '成都', '成都', '天津', '天津', '天津', '济南', '青岛', '广州', '广州',
			'深圳', '南宁', '南京', '南京', '南京', '无锡', '郑州', '宁波', '杭州', '杭州', '厦门',
			'福州', '大连', '大连', '沈阳', '沈阳', '重庆', '重庆', '重庆', "香港特别行政区", "香港特别行政区",
			"香港特别行政区", "香港特别行政区", "香港特别行政区", "香港特别行政区", "澳门特别行政区", "澳门特别行政区", "台湾"]
num = len(filename); checksum = list(range(num))
for u in range(0, num): checksum[u] = 0

rpath = os.path.expanduser('~') + "/Retail/"
masterKey = "bKwiDtPPRP6sY943piQKbd"

def down(fname, region): os.system("wget -t 0 -T 3 -O " + rpath + fname + ".json --no-check-certificate " +
	"https://www.apple.com/"+ region + "/today/static/data/store/" + fname + ".json")
def home():
	wAns = ""; mOpen = open(rpath + "savedEvent"); mark = mOpen.read(); mOpen.close()
	for d in range(0, num):
		cdsize = 0
		while cdsize == 0:
			if d < 41: down(filename[d], "cn")
			elif d > 40 and d < 47: down(filename[d], "hk")
			elif d > 46 and d < 49: down(filename[d], "mo")
			elif d == 49: down(filename[d], "tw")
			cdsize = os.path.getsize(rpath + filename[d] + ".json")
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
				pushAns = "Apple 在" + citAns + "有新活动: " + singleName; pushed = 0
				pushAns = pushAns.replace('"', "").replace("'", "").replace("：", " - ")
				for pc in range(0, num):
					if cityname[pc] in pushAns: checksum[pc] += 1
				print pushAns + " " + rJson[lct]["image"]
				os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1=" +
					pushAns + "&value2=Today at Apple 新活动&value3=" + rJson[lct]["image"] +
					"?output-format=jpg' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey)
				os.system("rm -f " + masterKey + "*")
				# GitHub users please notice: IFTTT Key only uses for private.
	mWrite = open(rpath + "savedEvent", "w"); mWrite.write(mark + wAns); mWrite.close()

while True:
	reload(sys); sys.setdefaultencoding('utf-8'); home(); pcf = ""
	for f in range(0, num): 
		if checksum[f] == 0 and not cityname[f] in pcf: 
			print "Apple 在" + cityname[f] + "没有新活动。"
			pcf += cityname[f]
		os.system("rm " + rpath + filename[f] + ".json")
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	os.system("rm -f " + masterKey + "*")
	time.sleep(43200)