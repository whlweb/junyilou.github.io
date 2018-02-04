#-*- coding:utf-8 -*-
import os, json, filecmp, platform, time

if "Linux" in platform.platform(): tilde = os.path.expanduser('~') + "/Retail/"
if "Darwin" in platform.platform(): tilde = os.path.expanduser('~') + "/Downloads/Apple/Raspberry/"

trans = ["海南", "上海", "云南", "内蒙古", "北京", "四川", "天津", "安徽", "山东", "山西", 
		"广东", "广西", "江苏", "河北", "河南", "浙江", "福建", "贵州", "辽宁", "重庆"]
codnm = ["HNA", "SHA", "KMG", "NEI", "PEK", "CTU", "TJN", "ANH", "SDG", "SXI", 
		"CAN", "GXI", "JSU", "HBE", "HEN", "HGZ", "FUJ", "GUZ", "LNG", "CKG"]
preDir = tilde + "Jobs/"

def wget(post, savename):
	os.system('wget -t 0 -T 4 -O ' + tilde + savename
		+ ' --no-check-certificate --post-data "countryCode=CHN&stateCode='
		+ post + '" https://jobs.apple.com/cn/location/cities.json')
def push(pushRaw):
	os.system("wget -t 0 -T 8 --no-check-certificate --post-data 'value1=" 
		+ pushRaw + "' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x")

def down():
	sOpen = open(tilde + "states.json"); sJson = json.loads(sOpen.read()); sOpen.close()
	for s in range(0, len(sJson)):
		cSize = 0
		while not cSize:
			wget(str(sJson[s]["id"]), "cities" + str(s) + ".json")
			cSize = os.path.getsize(tilde + "cities" + str(s) + ".json")
			uOpen = open(tilde + "cities" + str(s) + ".json"); uRead = uOpen.read(); uOpen.close()
			if "<!DOCTYPE html>" in uRead:
				print "Apple Jobs is now having an update.\nPlease check jobs information later.\n"
				push("[招贤纳才]Apple 招聘页面开始维护了，监测将退出。")
				os.system("rm " + preDir + "cities*.json"); exit()

def compare():
	changeOut = noChange = p = c = ""; global changeSummary
	for files in os.walk(preDir):
		for l in range(0, len(files[2])):
			oldLoc = preDir + files[2][l]; newLoc = oldLoc.replace("/Jobs", "")
			if files[2][l][0] != "." and files[2][l][-5:] == ".json" and "cities" in files[2][l]:
				if filecmp.cmp(oldLoc, newLoc) == False:
					oldOpen = open(oldLoc); oldJson = len(json.loads(oldOpen.read())); oldOpen.close()
					newOpen = open(newLoc); newJson = len(json.loads(newOpen.read())); newOpen.close()
					os.system("mv " + newLoc + " " + newLoc.replace(os.path.basename(newLoc), os.path.basename(newLoc).replace(".json", "-1.json")))
					if oldJson < newJson: p = "had " + str(newJson - oldJson) + " more items now."; c = "增加了 " + str(newJson - oldJson) + "个招聘地点。"
					if oldJson > newJson and newJson > 0: p = "seems to have some stop hiring."; c = "似乎停止了部分地点的招聘。"
					if oldJson > newJson and newJson == 0: p = "stopped hiring."; c = "已经不再招聘了。"
					changeOut =  "[*] Apple Jobs at " + codnm[int(os.path.basename(oldLoc).replace("cities", "").replace(".json", ""))] + " " + p
					push("[招贤纳才]Apple 在" + trans[int(os.path.basename(oldLoc).replace("cities", "").replace(".json", ""))] + c)
					print changeOut; changeSummary = changeSummary + changeOut
				else: noChange = noChange + "Checked file '" + os.path.basename(oldLoc) + "' has no update.\n"
	if changeSummary == "": changeSummary = "No changes found yet, please check back soon."
	print noChange + "\n============\n" + changeSummary
	os.system("mv -f " + tilde + "cities*.json " + preDir)
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()); time.sleep(86400)

global changeSummary; changeSummary = ""
while True: down(); compare()