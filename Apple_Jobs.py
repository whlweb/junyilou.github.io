#-*- coding:utf-8 -*-
import os, json, filecmp, platform

if "Linux" in platform.platform(): tilde = os.path.expanduser('~') + "/Retail/"
if "Darwin" in platform.platform(): tilde = os.path.expanduser('~') + "/Downloads/Apple/Raspberry/"
preDir = tilde + "Jobs/"

def wget(post, url, savename):
	os.system('wget -t 0 -T 3 -O ' + tilde + savename
		+ ' --no-check-certificate --post-data "countryCode=CHN&stateCode='
		+ post + '" https://jobs.apple.com/cn/location' + url)

Dict = {"cities19.json": "重庆市", "cities18.json": "辽宁省", "cities17.json": "贵州省", "cities16.json": "福建省", "cities15.json": "江苏省",
	"cities14.json": "河南省", "cities13.json": "河北省", "cities12.json": "江苏省", "cities11.json": "广西壮族自治区", "cities10.json": "广东省",
	"cities9.json": "山西省", "cities8.json": "山东省", "cities7.json": "安徽省", "cities6.json": "天津市", "cities5.json": "四川省",
	"cities4.json": "北京市", "cities3.json": "内蒙古自治区", "cities2.json": "云南省", "cities1.json": "上海市", "cities0.json": "海南省", 
	"location0-0.json": "三亚市", "location1-0.json": "", "location2-0.json": "昆明市", "location3-0.json": "包头市", "location4-0.json": "", 
	"location5-0.json": "成都市", "location6-0.json": "", "location7-0.json": "合肥市", "location7-1.json": "马鞍山市", "location8-0.json": "济南市",
	"location8-1.json": "青岛市", "location9-0.json": "太原市", "location10-0.json": "深圳市南山区", "location10-1.json": "深圳市", "location10-2.json": "东莞市", 
	"location10-3.json": "广州市", "location10-4.json": "惠州市", "location10-5.json": "汕头市", "location10-6.json": "深圳 AOS", "location11-0.json": "南宁市", 
	"location12-0.json": "南京市", "location12-1.json": "扬州市", "location12-2.json": "无锡市", "location12-3.json": "泰州市", "location12-4.json": "盐城市", 
	"location12-5.json": "苏州市", "location13-0.json": "秦皇岛市", "location14-0.json": "郑州市", "location15-0.json": "宁波市", "location15-1.json": "德清县", 
	"location15-2.json": "杭州市", "location15-3.json": "温州市", "location16-0.json": "厦门市", "location16-1.json": "福州市", "location17-0.json": "贵阳市", 
	"location18-0.json": "大连市", "location18-1.json": "沈阳市", "location19-0.json": ""}

def down():
	sOpen = open(tilde + "states.json")
	sJson = json.loads(sOpen.read()); sOpen.close()
	for s in range(0, len(sJson)):
		wget(str(sJson[s]["id"]), "/cities.json", "cities" + str(s) + ".json")
		if os.path.getsize(tilde + "cities" + str(s) + ".json") < 3:
			dl_fix("cities" + str(s) + ".json", 0)
		lOpen = open(tilde + "cities" + str(s) + ".json"); lRead = lOpen.read()
		if "<!DOCTYPE html>" in lRead:
			print "Apple Jobs is now having an update.\nPlease check jobs information later.\n"
			os.system("rm " + preDir + "cities*.json"); exit()
	for c in range(0, len(sJson)):
		cOpen = open(tilde + "cities" + str(c) + ".json")
		cJson = json.loads(cOpen.read()); cOpen.close()
		for g in range(0, len(cJson)):
			cID = str(c) + "-" + str(g)
			wget(str(sJson[c]["id"]) + "&cityCode=" + cJson[g]["cityName"], ".json", "location" + cID + ".json")
			if os.path.getsize(tilde + "location" + cID + ".json") < 3:
				dl_fix("location" + cID + ".json", 0)

def dl_fix(fileName, byp):
	print "\n" + fileName + " is detected to be redownloaded."
	sOpen = open(tilde + "states.json"); sJson = json.loads(sOpen.read()); sOpen.close()
	if "cities" in fileName:
		byp += 1; cID = int(fileName.replace("cities", "").replace(".json", ""))
		wget(str(sJson[cID]["id"]), "/cities.json", fileName)
	if "location" in fileName:
		byp += 1; lcB = int(fileName.replace("location", "").replace(".json", "").replace("-", "")[-1])
		lcA = int(fileName.replace("location", "").replace(".json", "").replace("-", "").replace(str(lcB), ""))
		cOpen = open(tilde + "cities" + str(lcA) + ".json"); cJson = json.loads(cOpen.read()); cOpen.close()
		wget(str(sJson[lcA]["id"]) + "&cityCode=" + cJson[lcB]["cityName"], ".json", fileName)
	if byp == 0: print "Not a location or city file."

def compare():
	for files in os.walk(preDir):
		for l in range(0, len(files[2])):
			oldLoc = preDir + files[2][l]; newLoc = oldLoc.replace("/Jobs", ""); p = ""
			if files[2][l][0] != "." and files[2][l][-5:] == ".json":
				if filecmp.cmp(oldLoc, newLoc) == False:
					oldOpen = open(oldLoc); oldJson = len(json.loads(oldOpen.read())); oldOpen.close()
					newOpen = open(newLoc); newJson = len(json.loads(newOpen.read())); newOpen.close()
					os.system("mv " + newLoc + " " + newLoc.replace(os.path.basename(newLoc), os.path.basename(newLoc).replace(".json", "-1.json")))
					if oldJson < newJson: p = "现在有 " + str(newJson) + " 个项目, 其原本只有 " + str(oldJson) + " 个。"
					if oldJson == newJson: p = "现在有文字更新，其项目数量没有改变，可能代码发生修改，或地点名字更加确定。"
					if oldJson > newJson and newJson > 0: p = "表明有大于等于一个地址不再招聘。"
					if oldJson > newJson and newJson == 0: p = "表明该地点似乎不再招聘。"
					print "招贤纳才 - Apple 在" + Dict[os.path.basename(oldLoc)] + "的招聘文件" + p		
	os.system("mv -f " + tilde + "cities*.json " + preDir)
	os.system("mv -f " + tilde + "location*.json " + preDir)

down(); compare()