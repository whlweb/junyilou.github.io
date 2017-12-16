#-*- coding:utf-8 -*-
import os, json, filecmp, platform, time

if "Linux" in platform.platform(): tilde = os.path.expanduser('~') + "/Retail/"
if "Darwin" in platform.platform(): tilde = os.path.expanduser('~') + "/Downloads/Apple/Raspberry/"
preDir = tilde + "Jobs/"

def cRep(org, dep, des = ""): return org.replace(dep, des)
def wget(post, url, savename):
	os.system('wget -t 0 -T 3 -O ' + tilde + savename
		+ ' --no-check-certificate --post-data "countryCode=CHN&stateCode='
		+ post + '" https://jobs.apple.com/cn/location' + url)

def down():
	sOpen = open(tilde + "states.json")
	sJson = json.loads(sOpen.read()); sOpen.close()
	for s in range(0, len(sJson)):
		wget(str(sJson[s]["id"]), "/cities.json", "cities" + str(s) + ".json")
		lOpen = open(tilde + "cities" + str(s) + ".json"); lRead = lOpen.read(); lOpen.close()
		if "<!DOCTYPE html>" in lRead:
			print "Apple Jobs is now having an update.\nPlease check jobs information later.\n"
			os.system("rm " + preDir + "cities*.json"); exit()
	check("cities")
	for c in range(0, len(sJson)):
		cOpen = open(tilde + "cities" + str(c) + ".json")
		try: cJson = json.loads(cOpen.read()); cOpen.close()
		except ValueError: dl_fix("cities" + str(c) + ".json"); cJson = 0
		for g in range(0, len(cJson)):
			cID = str(c) + "-" + str(g)
			wget(str(sJson[c]["id"]) + "&cityCode=" + cJson[g]["cityName"], ".json", "location" + cID + ".json")
	check("location")

def check(cInclude, cCount = 0, cString = ""):
	for checks in os.walk(tilde):
		for n in range(0, len(checks[2])):
			if checks[2][n][0] != "." and checks[2][n][-5:] == ".json" and cInclude in checks[2][n]:
				cLocation = tilde + checks[2][n]; cSize = os.path.getsize(cLocation)
				if cSize != 0: cCount += 1
				else: cString += (checks[2][n] + ", ")
	if cInclude == "cities": checkItems = 20
	if cInclude == "location": checkItems = 38
	if cCount / 2 != checkItems:
		cLen = len(cString) / 2; cString = cString[:cLen]
		print cString + "detected to be redownload."
		cSpl = cString.split(", ")
		for k in range(0, len(cSpl)):
			while os.path.getsize(tilde + cSpl[k]) == 0: dl_fix(cSpl[k])

def dl_fix(fileName, byp = 0):
	print "\n" + fileName + " is detected to be redownloaded."
	sOpen = open(tilde + "states.json"); sJson = json.loads(sOpen.read()); sOpen.close()
	if "cities" in fileName:
		byp += 1; cID = int(cRep(cRep(fileName, "cities"), ".json"))
		wget(str(sJson[cID]["id"]), "/cities.json", fileName)
	if "location" in fileName:
		byp += 1; lcB = cRep(cRep(cRep(fileName, "location"), ".json"), "-")[-1]
		lcA = int(cRep(cRep(cRep(fileName, "location"), ".json"), "-" + lcB))
		cOpen = open(tilde + "cities" + str(lcA) + ".json"); cJson = json.loads(cOpen.read()); cOpen.close()
		wget(str(sJson[lcA]["id"]) + "&cityCode=" + cJson[int(lcB)]["cityName"], ".json", fileName)
	if byp == 0: print "Not a location or city file."

def compare():
	for files in os.walk(preDir):
		for l in range(0, len(files[2])):
			oldLoc = preDir + files[2][l]; newLoc = cRep(oldLoc, "/Jobs"); p = ""
			if files[2][l][0] != "." and files[2][l][-5:] == ".json":
				if filecmp.cmp(oldLoc, newLoc) == False:
					oldOpen = open(oldLoc); oldJson = len(json.loads(oldOpen.read())); oldOpen.close()
					newOpen = open(newLoc); newJson = len(json.loads(newOpen.read())); newOpen.close()
					os.system("mv " + newLoc + " " + newLoc.replace(os.path.basename(newLoc), os.path.basename(newLoc).replace(".json", "-1.json")))
					if oldJson < newJson: p = "had  " + str(newJson) + " items, instead of " + str(oldJson) + " now."
					if oldJson == newJson: p = "has a text update without numbers updates."
					if oldJson > newJson and newJson > 0: p = "seems to have a stop hiring."
					if oldJson > newJson and newJson == 0: p = "stopped hiring."
					print "[*] The location for file '" + os.path.basename(oldLoc) + "' " + p
				else: print "Checked file '" + os.path.basename(oldLoc) + "' has no update."
	os.system("mv -f " + tilde + "cities*.json " + preDir)
	os.system("mv -f " + tilde + "location*.json " + preDir)

def custom():
	while True:
		newSuzhou = tilde + "Suzhou.json"; os.system("touch " + newSuzhou); oldSuzhou = preDir + "Suzhou.json"
		newChengdu = tilde + "Chengdu.json"; os.system("touch " + newChengdu); oldChengdu = preDir + "Chengdu.json"
		while os.path.getsize(newSuzhou) < 650: wget("165&cityCode=Suzhou", ".json", "Suzhou.json")
		while os.path.getsize(newChengdu) < 1300: wget("178&cityCode=Chengdu", ".json", "Chengdu.json")
		mRead = open(newSuzhou); maintain = mRead.read()
		if "<!DOCTYPE html>" in maintain: os.system("wget -t 0 -T 8 --no-check-certificate --post-data 'value1=[招贤纳才]Apple 招聘页面开始维护了。' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x"); exit()
		else:
			if filecmp.cmp(oldSuzhou, newSuzhou) == False:
				os.system("wget -t 0 -T 8 --no-check-certificate --post-data 'value1=[招贤纳才]Apple 在苏州的招聘计划似乎发生了改变。' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x"); exit()
			if filecmp.cmp(oldChengdu, newChengdu) == False:
				os.system("wget -t 0 -T 8 --no-check-certificate --post-data 'value1=[招贤纳才]Apple 在成都的招聘计划似乎发生了改变。' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x"); exit()
		print "Sleeping, interval will be 12 hr."; os.system("rm " + newSuzhou); os.system("rm " + newChengdu); time.sleep(43200)
#down(); compare()
custom()