#-*- coding:utf-8 -*-
import os, urllib2, sys, json, time

filename = ['qibao', 'shanghaiiapm', 'wujiaochang', 'nanjingeast', 'pudong', 'globalharbor',
			 'hongkongplaza', 'kunming', 'sanlitun', 'chinacentralmall', 'chaoyangjoycity', 
			 'wangfujing', 'xidanjoycity', 'mixcchengdu', 'taikoolichengdu', 'tianjinjoycity',
			 'riverside66tianjin', 'galaxymall', 'parc66jinan', 'mixcqingdao', 'parccentral',
			 'zhujiangnewtown', 'holidayplazashenzhen', 'mixcnanning', 'nanjingist', 'nanjingjinmaoplace', 
			 'wondercity', 'center66wuxi', 'suzhou', 'mixczhengzhou', 'tianyisquare', 'mixchangzhou', 
			 'westlake', 'xiamenlifestylecenter', 'thaihotplaza', 'olympia66dalian', 'parkland', 
			 'zhongjiejoycity', 'mixcshenyang', 'jiefangbei', 'mixcchongqing', 'paradisewalkchongqing',
			 'apmhongkong', 'cantonroad', 'causewaybay', 'festivalwalk', 'ifcmall', 'newtownplaza',
			 'galaxymacau', 'cotaicentral', 'taipei101']
cityname = ['上海', '上海', '上海', '上海', '上海', '上海', '上海', '昆明', '北京', '北京', '北京',
			'北京', '北京', '成都', '成都', '天津', '天津', '天津', '济南', '青岛', '广州', '广州',
			'深圳', '南宁', '南京', '南京', '南京', '无锡', '苏州', '郑州', '宁波', '杭州', '杭州',
			'厦门', '福州', '大连', '大连', '沈阳', '沈阳', '重庆', '重庆', '重庆', "香港特别行政区", "香港特别行政区",
			"香港特别行政区", "香港特别行政区", "香港特别行政区", "香港特别行政区", "澳门特别行政区", "澳门特别行政区", "台湾"]
num = len(filename)

def down(fname, region): 
	os.system("wget -q -t 100 -T 3 -O " + rpath + fname + ".json --no-check-certificate " +
	"https://www.apple.com/"+ region + "/today/static/data/store/" + fname + ".json")
def home():
	wAns = ""; mOpen = open(rpath + "savedEvent"); mark = mOpen.read(); mOpen.close()
	for d in range(0, num):
		cdsize = 0
		while cdsize == 0:
			if d < 42: down(filename[d], "cn")
			elif d > 41 and d < 48: down(filename[d], "hk")
			elif d > 47 and d < 50: down(filename[d], "mo")
			elif d == 50: down(filename[d], "tw")
			cdsize = os.path.getsize(rpath + filename[d] + ".json")
		print "Download in Progress: " + str((d + 1) * 100 / num) + "%\r",
		sys.stdout.flush()
	print
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
				for msk in range(0, len(masterKey)):
					checkLoc = os.path.expanduser('~') + masterKey[msk]
					os.system("rm -f " + checkLoc + "*")
					while not os.path.isfile(checkLoc):
						os.system("wget -t 100 -T 3 --post-data 'value1=" + pushAns +
						"&value2=Today at Apple 新活动&value3=" + rJson[lct]["image"] +
						"?output-format=jpg' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey[msk])
					os.system("rm -f " + checkLoc)
		print "Compare in Progress: " + str((i + 1) * 100 / num) + "%\r",
		sys.stdout.flush()
	mWrite = open(rpath + "savedEvent", "w"); mWrite.write(mark + wAns); mWrite.close(); print

rpath = os.path.expanduser('~') + "/Retail/"
isKey = os.path.isfile(os.path.expanduser('~') + "/key.txt")
if not isKey:
	print ("Please provide your IFTTT key in ~/key.txt\n" +
	"Location of the txt can be edited in the source code."); exit()
else: 
	kOpen = open(os.path.expanduser('~') + "/key.txt")
	masterKey = list()
	for line in open(os.path.expanduser('~') + "/key.txt"):
		line = kOpen.readline().replace("\n", "")
		masterKey.append(line)
	kOpen.close()

while True:
	reload(sys); sys.setdefaultencoding('utf-8'); home()
	for rm in range(0, num): os.system("rm " + rpath + filename[rm] + ".json")
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	time.sleep(43200)