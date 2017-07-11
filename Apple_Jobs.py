#-*- coding:utf-8 -*-
import os, json, filecmp
tilde = os.path.expanduser('~') + "/Retail/"; preDir = tilde + "Jobs/"; uPre = "https://jobs.apple.com/cn/location"

def wget(post, url, savename):
	os.system('wget -t 0 -T 3 -O ' + tilde + savename + ' --no-check-certificate --post-data "' + post + '" ' + url)

def dictionary(request):
	Dict = {"cities20.json": "重庆市", "cities19.json": "辽宁省", "cities18.json": "贵州省", "cities17.json": "福建省", "cities16.json": "江苏省",
	"cities15.json": "河南省", "cities14.json": "河北省", "cities13.json": "江苏省", "cities12.json": "广西壮族自治区", "cities11.json": "广东省",
	"cities10.json": "山西省", "cities9.json": "山东省", "cities8.json": "安徽省", "cities7.json": "天津市", "cities6.json": "四川省",
	"cities5.json": "北京市", "cities4.json": "内蒙古自治区", "cities3.json": "云南省", "cities2.json": "上海市", "cities1.json": "湖南省",
	"cities0.json": "海南省", "location0-0.json": "三亚市", "location1-0.json": "长沙市", "location2-0.json": "", "location3-0.json": "昆明市",
	"location4-0.json": "包头市", "location5-0.json": "", "location6-0.json": "成都市", "location7-0.json": "", "location8-0.json": "合肥市",
	"location8-1.json": "马鞍山市", "location9-0.json": "济南市", "location9-1.json": "青岛市", "location10-0.json": "太原市", "location11-0.json": "深圳市",
	"location11-1.json": "东莞市", "location11-2.json": "广州市", "location11-3.json": "惠州市", "location11-4.json": "汕头市", "location11-5.json": "深圳 AOS",
	"location12-0.json": "南宁市", "location13-0.json": "南京市", "location13-1.json": "扬州市", "location13-2.json": "无锡市", "location13-3.json": "泰州市",
	"location13-4.json": "盐城市", "location13-5.json": "苏州市", "location14-0.json": "秦皇岛市", "location15-0.json": "郑州市", "location16-0.json": "宁波市",
	"location16-1.json": "德清县", "location16-2.json": "杭州市", "location16-3.json": "温州市", "location17-0.json": "厦门市", "location17-1.json": "福州市",
	"location18-0.json": "贵阳市", "location19-0.json": "大连市", "location19-1.json": "沈阳市", "location20-0.json": ""}
	return Dict[request]

def down():
	sOpen = open(tilde + "states.json"); lCount = 0
	statesJson = json.loads(sOpen.read()); sOpen.close()
	for s in range(0, len(statesJson)):
		wget("countryCode=CHN&stateCode=" + str(statesJson[s]["id"]), uPre + "/cities.json", "cities" + str(s) + ".json")
		lOpen = open(tilde + "cities" + str(s) + ".json"); lCount += len(json.loads(lOpen.read()))
	citiesID = list(range(lCount))
	for c in range(0, len(statesJson)):
		cOpen = open(tilde + "cities" + str(c) + ".json")
		citiesJson = json.loads(cOpen.read()); cOpen.close()
		for g in range(0, len(citiesJson)):
			citiesID = str(c) + "-" + str(g)
			wget("countryCode=CHN&stateCode=" + str(statesJson[c]["id"]) + "&cityCode=" + citiesJson[g]["cityName"], uPre + ".json", "location" + citiesID + ".json")

def compare():
	for files in os.walk(preDir):
		for l in range(0, len(files[2])):
			oldLoc = preDir + files[2][l]; newLoc = oldLoc.replace("/Jobs", ""); p = ""
			if files[2][l][0] != ".": #隐藏文件
				if filecmp.cmp(oldLoc, newLoc) == False:
					print oldLoc, newLoc
					oldOpen = open(oldLoc); oldJson = len(json.loads(oldOpen.read())); oldOpen.close()
					newOpen = open(newLoc); newJson = len(json.loads(newOpen.read())); newOpen.close()
					if oldJson < newJson:
						p = "现在有 " + str(newJson) + " 个项目, 其原本只有 " + str(oldJson) + " 个。"
					if oldJson == newJson:
						p = "现在有文字更新，其项目数量没有改变，可能代码发生修改，或地点名字更加确定。"
					if oldJson > newJson and newJson > 0:
						p = "表明有大于等于一个地址不再招聘，前往 Apple 官网确认。"
					p = "招贤纳才 - Apple 在" + dictionary(os.path.basename(oldLoc)) + "的招聘文件" + p; print p
	if p == "": "Nothing new."
	else: os.system('curl -X POST -H "Content-Type: application/json" -d' + "'" + '{"value1":"' + p + '"}'
			   + "' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x"); print
	# GitHub users please notice: IFTTT Key only uses for private.
	os.system("rm " + preDir + "*.json");
	os.system("mv " + tilde + "cities*.json " + preDir)
	os.system("mv " + tilde + "location*.json " + preDir)

down(); compare()