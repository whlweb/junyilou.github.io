#-*- coding:utf-8 -*-
import json, os, sys

rpath = os.path.expanduser('~') + "/Retail/Jobs/"; wAns = ""
imageURL = "https://www.apple.com/jobs/images/retail/hero/desktop.jpg"

stateCHN = ["新加坡", "土耳其", "阿联酋", "英国", "德国", "台湾", "美国", "墨西哥",
			"瑞士", "比利时", "荷兰", "泰国", "西班牙", "香港", "瑞典", "中国", "法国",
			"澳大利亚", "意大利", "奥地利", "澳门", "巴西", "日本", "韩国", "加拿大"]
stateCode = ["SG", "TR", "AE", "UK", "DE", "TW", "US", "MX",
			"CH", "BE", "NL", "TH", "ES", "HK", "SE", "CN", "FR",
			"AU", "IT", "AT", "MO", "BR", "JP", "KR", "CA"]
stateEmoji = ["🇸🇬", "🇹🇷", "🇦🇪", "🇬🇧", "🇩🇪", "🇹🇼", "🇺🇸", "🇲🇽",
			"🇨🇭", "🇧🇪", "🇳🇱", "🇹🇭", "🇪🇸", "🇭🇰", "🇸🇪", "🇨🇳", "🇫🇷",
			"🇦🇺", "🇮🇹", "🇦🇹", "🇲🇴", "🇧🇷", "🇯🇵", "🇰🇷", "🇨🇦"]
specialistCode = [8238, 8164, 8225, 8145, 8043, 8311, 8158, 8297,
				8017, 8251, 8119, 8346, 8056, 8082, 8132, 8030, 8069,
				7991, 8095, 8333, 8282, 8176, 8107, 8326, 8004]
#stateCHN = ["澳大利亚"]; stateCode = ["AU"]; stateEmoji = ["🇦🇺"]; specialistCode = [7991] #Debug

mOpen = open(rpath + "savedJobs"); mark = mOpen.read(); mOpen.close()

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

for adpre in range(0, len(specialistCode)):
	reload(sys); sys.setdefaultencoding('utf-8')
	realCode = "11443" + str(specialistCode[adpre])
	savename = rpath + stateCode[adpre] + "/state.json"; whileCount = True
	while whileCount:
		os.system("wget -q -t 100 -T 5 -O " + savename + " https://jobs.apple.com/api" + 
		"/v1/jobDetails/PIPE-" + realCode + "/stateProvinceList")
		if os.path.getsize(savename) > 0: whileCount = False
	jOpen = open(savename); stateJSON = json.loads(jOpen.read())["searchResults"]; jOpen.close()
	print "                                                                \r", #Pre Scheme
	sys.stdout.flush()
	for i in range(0, len(stateJSON)): 
		dID = stateJSON[i]["id"]
		savename = rpath + stateCode[adpre] + "/location_" + dID.replace("postLocation-", "") + ".json"
		header = " [" + str(adpre + 1) + "/" + str(len(specialistCode)) + "] "
		statusBar = "正在下载" + stateCHN[adpre] + "的城市文件, 已完成 " + str((i + 1) * 100 / len(stateJSON))
		print header + statusBar + "% \r",
		sys.stdout.flush(); whileCount = True
		while whileCount:
			os.system("wget -q -t 100 -T 5 -O " + savename + " 'https://jobs.apple.com/api/v1/jobDetails/PIPE-" 
			+ realCode + "/storeLocations?searchField=stateProvince&fieldValue=" + dID + "'")
			if os.path.getsize(savename) > 0: whileCount = False
	for j in range(0, len(stateJSON)): 
		oID = stateJSON[j]["id"]
		savename = rpath + stateCode[adpre] + "/location_" + oID.replace("postLocation-", "") + ".json"
		cityJSON = json.loads(open(savename).read().decode('utf-8-sig'))
		for c in range(0, len(cityJSON)):
			rolloutCode = cityJSON[c]["code"]
			if not rolloutCode in mark:
				wAns += stateEmoji[adpre] + rolloutCode + ", "
				mWrite = open(rpath + "savedJobs", "w"); mWrite.write(mark + wAns); mWrite.close()
				pushAns = "新店新机遇: " + stateCHN[adpre] + "新增招聘地点 " + rolloutCode + ", 名称「" 
				pushAns += cityJSON[c]["name"] + "」, 文件名 " + oID.replace("postLocation-", "") + ".json"
				for msk in range(0, len(masterKey)):
					os.system("wget -t 100 -T 8 --no-check-certificate --post-data 'value1=" + pushAns
					+ "&value2=Apple 招贤纳才&value3=" + imageURL + "' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey[msk])
					os.system("rm -f " + masterKey[msk] + "*")
print