#-*- coding:utf-8 -*-
import json, os, sys

rpath = os.path.expanduser('~') + "/Retail/Jobs/"
stateCHN = ["新加坡", "土耳其", "阿联酋", "英国", "德国", "台湾", "美国", "墨西哥",
			"瑞士", "比利时", "荷兰", "泰国", "西班牙", "香港", "瑞典", "中国", "法国",
			"澳大利亚", "意大利", "奥地利", "澳门", "巴西", "日本", "韩国", "加拿大"]
stateCode = ["SG", "TR", "AE", "UK", "DE", "TW", "US", "MX",
			"CH", "BE", "NL", "TH", "ES", "HK", "SE", "CN", "FR",
			"AU", "IT", "AT", "MO", "BR", "JP", "KR", "CA"]
specialistCode = [8238, 8164, 8225, 8145, 8043, 8311, 8158, 8297,
				8017, 8251, 8119, 8346, 8056, 8082, 8132, 8030, 8069,
				7991, 8095, 8333, 8282, 8176, 8107, 8326, 8004]

for adpre in range(0, len(specialistCode)): 
	realCode = "11443" + str(specialistCode[adpre])
	savename = rpath + stateCode[adpre] + "/state.json"
	os.system("wget -q -t 100 -T 5 -O " + savename + " https://jobs.apple.com/api" + 
		"/v1/jobDetails/PIPE-" + realCode + "/stateProvinceList")
	jOpen = open(savename); stateJSON = json.loads(jOpen.read())["searchResults"]; jOpen.close()
	for i in range(0, len(stateJSON)): 
		dID = stateJSON[i]["id"]
		savename = rpath + stateCode[adpre] + "/location_" + dID.replace("postLocation-", "") + ".json"
		print "正在下载" + stateCHN[adpre] + "的城市文件, 进度 " + str((i + 1) * 100 / len(stateJSON)) + "%\r",
		sys.stdout.flush()
		os.system("wget -q -t 100 -T 5 -O " + savename + " 'https://jobs.apple.com/api/v1/jobDetails/PIPE-" 
			+ realCode + "/storeLocations?searchField=stateProvince&fieldValue=" + dID + "'")
	print "\n" + stateCHN[adpre] + "已招聘零售店:"
	for j in range(0, len(stateJSON)): 
		oID = stateJSON[j]["id"]
		savename = rpath + stateCode[adpre] + "/location_" + oID.replace("postLocation-", "") + ".json"
		cityJSON = json.loads(open(savename).read().decode('utf-8-sig'))
		for c in range(0, len(cityJSON)):
			rolloutCode = cityJSON[c]["code"]
			print rolloutCode + ",",
	print "\n"