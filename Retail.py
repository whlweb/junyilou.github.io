#-*- coding:utf-8 -*-
import os, sys, datetime, json, time

def down(rtl):
	global upb, exce; spr = "/R" + rtl + ".png"; sx = sbn + rtl + ".png"
	if os.path.isfile(sx): oldsize = os.path.getsize(sx)
	else: oldsize = 0
	os.system("wget -t 0 -T 5 -q -N -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr)
	if os.path.isfile(sx): newsize = os.path.getsize(sx)
	else: newsize = 0
	keyList = ["bKwiDtPPRP6sY943piQKbd", "bOGI8iEAyvjh782UYFKbRa"]
	# GitHub users please notice: IFTTT key only uses for private.
	if newsize != oldsize and newsize > 1:
		try: rname = storejson[0][rtl]
		except KeyError: rname = "Store"
		pushRaw = "Apple " + rname + " (R" + rtl + ") just updated, the size of the picture is " + str(newsize / 1024) + " KB."
		upb = upb + pushRaw + "\n"; exce = exce + rtl + ", "; print pushRaw
		tellRaw = "Apple " + rname + "，零售店编号 R" + rtl + "，刚刚更新。新图片大小为 " + str(newsize / 1024) + " KB。"
		for pg in range(0, len(keyList)):
			os.system("wget -t 0 -T 8 --no-check-certificate --post-data 'value1=" + tellRaw 
				+ "&value2=Apple Store 零售店图片&value3=" + dieter + "/16_9" 
				+ spr + "' https://maker.ifttt.com/trigger/raw/with/key/" + keyList[pg])
	else: 
		try: pname = "R" + rtl + ": " + storejson[0][rtl]
		except KeyError: pname = "R" + rtl
		if newsize == 0: print pid + " Checked " + pname + " does not exist, ignore."
		else: print pid + " Checked R" + rtl + " has no update, ignore."

global upb; arg = 0; pid = str(os.getpid()); upb = exce = ""; rTime = 0
for m in sys.argv[1:]: arg += 1
rpath = "/home/pi/Retail/"; sbn = rpath + "Pictures/R"
dieter = "https://rtlimages.apple.com/cmc/dieter/store"
nameopen = open("/home/pi/Retail/name.md"); storejson = json.loads(nameopen.read()); nameopen.close()

while True:
	reload(sys); sys.setdefaultencoding('utf-8')
	sTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()); eCount = exce.count(", ")
	if arg - eCount:
		print "Starting special watchlist refreshing..."
		for s in range(1, arg + 1): 
			if not sys.argv[s] in exce: down("%03d" % int(sys.argv[s]))
	else: "No special watchlist found, ignore 1 hour."
	if not (rTime % 5):
		for j in range(1, 730): down("%03d" % j)
	rTime += 1
	print upb + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
	time.sleep(3600)