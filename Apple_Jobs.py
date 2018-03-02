#-*- coding:utf-8 -*-
import os, json, filecmp, platform, time

if "Linux" in platform.platform(): tilde = os.path.expanduser('~') + "/Retail/"
if "Darwin" in platform.platform(): tilde = os.path.expanduser('~') + "/Downloads/Apple/Raspberry/"

trans = ["海南", "上海", "云南", "内蒙古", "北京", "四川", "天津", "安徽", "山东", "山西", 
		"广东", "广西", "江苏", "河北", "河南", "浙江", "福建", "贵州", "辽宁", "重庆"]
codnm = ["HNA", "SHA", "KMG", "NEI", "PEK", "CTU", "TJN", "ANH", "SDG", "SXI", 
		"CAN", "GXI", "JSU", "HBE", "HEN", "HGZ", "FUJ", "GUZ", "LIA", "CKG"]
preDir = tilde + "Jobs/"

def wget(post, filen, savename):
	os.system('wget -t 0 -T 4 -O ' + tilde + savename
		+ ' --no-check-certificate --post-data "countryCode=CHN'
		+ post + '" https://jobs.apple.com/cn/location' + filen + '.json')
def push(pushRaw):
	os.system("wget -t 0 -T 8 --no-check-certificate --post-data 'value1=" 
		+ pushRaw + "' https://maker.ifttt.com/trigger/raw/with/key/bKwiDtPPRP6sY943piQKbd")

def down():
	lSize = 0
	while lSize < 3: wget("", "/states", "states.json"); lSize = os.path.getsize(tilde + "states.json")
	sOpen = open(tilde + "states.json"); sJson = json.loads(sOpen.read()); sOpen.close()
	if len(sJson) > 20:
		print "Apple Jobs updated states.json.\nPlease edit the script to fit the new JSON.\n"
		push("[招贤纳才]Apple 更新了 states.json，请手动修改程序。")
		os.system("rm " + tilde + "states.json"); exit()
	for s in range(0, len(sJson)):
		sSize = 0
		while sSize < 3:
			wget("&stateCode=" + str(sJson[s]["id"]), "/cities", "cities" + str(s) + ".json")
			sSize = os.path.getsize(tilde + "cities" + str(s) + ".json")
			uOpen = open(tilde + "cities" + str(s) + ".json"); uRead = uOpen.read(); uOpen.close()
			if "<!DOCTYPE html>" in uRead:
				print "Apple Jobs is now having an update.\nPlease check jobs information later.\n"
				push("[招贤纳才]Apple 招聘页面开始维护了，监测将退出。")
				os.system("rm " + tilde + "cities*.json"); exit()
	for c in range(0, len(sJson)):
 		cOpen = open(tilde + "cities" + str(c) + ".json"); cJson = json.loads(cOpen.read()); cOpen.close()
 		for g in range(0, len(cJson)):
 			cSize = 0
 			while cSize < 3:
	 			wget("&stateCode=" + str(sJson[c]["id"]) + "&cityCode=" + cJson[g]["cityName"], "", "location" + str(c) + "-" + str(g) + ".json")
	 			cSize = os.path.getsize(tilde + "location" + str(c) + "-" + str(g) + ".json")

def compare():
	changeOut = noChange = p = c = ""; global changeSummary
	for files in os.walk(preDir):
		for l in range(0, len(files[2])):
			oldLoc = preDir + files[2][l]; newLoc = oldLoc.replace("/Jobs", "")
			if files[2][l][0] != "." and files[2][l][-5:] == ".json":
				if filecmp.cmp(oldLoc, newLoc) == False:
					oldOpen = open(oldLoc); oldJson = len(json.loads(oldOpen.read())); oldOpen.close()
					newOpen = open(newLoc); newJson = len(json.loads(newOpen.read())); newOpen.close()
					os.system("mv " + newLoc + " " + newLoc.replace(os.path.basename(newLoc), os.path.basename(newLoc).replace(".json", "-1.json")))
					if oldJson < newJson: p = "had " + str(newJson - oldJson) + " more item now."; c = "增加了 " + str(newJson - oldJson) + "个招聘地点。"
					if oldJson > newJson and newJson > 0: p = "seems to stopped some hiring."; c = "似乎停止了部分地点的招聘。"
					if oldJson > newJson and newJson == 0: p = "stopped hiring."; c = "已经不再招聘了。"
					if "cities" in os.path.basename(oldLoc): repOldLoc = os.path.basename(oldLoc).replace("cities", "").replace(".json", "")
					if "location" in os.path.basename(oldLoc):
						noLoc = os.path.basename(oldLoc).replace("location", "").replace(".json", "")
						for rl in range(0, len(noLoc)):
							if noLoc[rl] == "-": rans = rl
						rl -= 1; repOldLoc = noLoc[:rl]
					changeOut =  "[*] Apple Jobs at " + codnm[int(repOldLoc)] + " " + p
					push("[招贤纳才]Apple 在" + trans[int(repOldLoc)] + c)
					print changeOut; changeSummary = changeSummary.replace("No changes found yet, please check back soon.", "") + changeOut + "\n"
				else: noChange = noChange + "Checked file '" + os.path.basename(oldLoc) + "' has no update.\n"
	if changeSummary == "": changeSummary = "No changes found yet, please check back soon."
	print noChange + "\n============\n" + changeSummary
	os.system("mv -f " + tilde + "cities*.json " + preDir)
	os.system("mv -f " + tilde + "location*.json " + preDir)
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()); time.sleep(43200)

global changeSummary; changeSummary = ""
while True: down(); compare()