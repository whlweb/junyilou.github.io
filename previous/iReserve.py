# -*- coding:utf-8 -*-
# GitHub users please notice: IFTTT key only uses for private.
import json, os, sys, time
def pushbots(pushRaw): os.system("wget --post-data 'value1=" + pushRaw + "' -t 0 -T 3 https://maker.ifttt.com/trigger/iphone/with/key/" + masterKey)
def check(rtl): os.system('wget --post-data="regioncode=CN&onlyshowavailability=false&storecode=R' + str(rtl) + '" -O ~/ans_' +str(os.getpid()) + '.json -q http://ir.weip.tech/Home/GetStoreiPhoneList')
nLocation = os.path.expanduser('~') + "/noshow_" + str(os.getpid()) + ".txt"; os.system("cd >" + nLocation)
storeList = input("输入零售店 Rollout 编号，按照数组形式排列。",); endl = "\n"
modelSelect = input("选择所需 iPhone 机型：\niPhone X 256GB 银色 - 1\niPhone X 256GB 深空灰色 - 2\niPhone X 64GB 深空灰色 - 3\niPhone X 64GB 银色 - 4\n按照数组形式输入所有设备。",)
masterKey = raw_input("输入 IFTTT Maker 密钥，可使用 default 代替 Junyi_Lou 的密钥。",)
if masterKey == "default": masterKey = "dJ4B3uIsxyedsXeQKk_D3x"
postSelect = input("你想要在所需设备无法预约时额外接受提示么？")
while True:
	print "******************** 新结果 ********************"
	nOpen = open(nLocation); nRead = nOpen.read(); nOpen.close(); nSingle = ""; nOut = ""
	try: lenStore = len(storeList)
	except TypeError: lenStore = 1
	for s in range(0, lenStore):
		try: singleStore = storeList[s]
		except TypeError: singleStore = storeList
		check(singleStore); aOpen = open(os.path.expanduser('~') + "/ans_" + str(os.getpid()) + ".json"); aRead = aOpen.read(); aOpen.close(); aJSON = json.loads(aRead); Data = aJSON["Data"]
		output = list(range(4)); oBool = list(range(4)); oNoShow = list(range(4))
		for i in range(0, 4):
			reload(sys); sys.setdefaultencoding('utf-8')
			if Data[i]["CanReserve"]: regBool = "可预约"; oBool[i] = True
			else: regBool = "不可预约"; oBool[i] = False
			output[i] = "iReserve - Apple " + Data[i]["RetailName"] + "的 " + Data[i]["Name"] + "现在" + regBool
			if output[i] in nRead: output[i] += "[No Show]"; oNoShow[i] = True
			else: oNoShow[i] = False
		try: lenModel = len(modelSelect)
		except TypeError: lenModel = 1; 
		for r in range(0, lenModel):
			if lenModel == 1: nSingle = output[modelSelect - 1]
			else: nSingle = output[int(modelSelect[r]) - 1]
			print nSingle; nOut += nSingle
			if not "[No Show]" in nSingle:
				if postSelect: pushbots(output[i])
				if not postSelect: 
					if not "不可预约" in output[i]: pushbots(output[i])
		nOut = nOut.replace("[No Show]", "") + endl
	nWrite = open(nLocation, "w"); nWrite.write(nOut); nWrite.close()
	os.system("rm -f " + os.path.expanduser('~') + "/" + masterKey + "*")
	print "Sleeping, interval will be 1 minute."; time.sleep(60)