#-*- coding:utf-8 -*-
import os, sys, json, time

# Stay foolish.

def asa():
	print "Comparing ASA remote file..."
	listLoc = rpath + "storeList.json"
	orgListSize = os.path.getsize(listLoc)
	os.system("mv " + listLoc + " " + listLoc.replace(".json", "_old.json"))
	os.system("wget -q -O " + listLoc + " --header 'x-ma-pcmh: REL-5.1.0' " + 
		"https://mobileapp.apple.com/mnr/p/cn/retail/allStoresInfoLite")
	newListSize = os.path.getsize(listLoc)
	if orgListSize != newListSize and orgListSize > 1024 and newListSize > 1024:
		os.system("wget -t 0 -T 8 --no-check-certificate --post-data 'value1=看起来 Apple Store app " 
			+ "的零售店列表文件更新了&value2=Apple Store 零售店图片&value3=https://junyilou."
			+ "github.io/bkP/ASA.jpg' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey)
		os.system("rm -f " + masterKey + "*")
	else: 
		os.system("mv " + listLoc.replace(".json", "_old.json") + " " + listLoc)
		print "No changes found."

def down(rtl, isSpecial):
	global upb, exce; spr = "/R" + rtl + ".png"; sx = sbn + rtl + ".png"
	if os.path.isfile(sx): oldsize = os.path.getsize(sx)
	else: oldsize = 0
	os.system("wget -t 100 -T 5 -q -N -P " + rpath + "Pictures/ " + dieter + spr)
	if os.path.isfile(sx): newsize = os.path.getsize(sx)
	else: newsize = 0
	if newsize != oldsize and newsize > 1:
		try: rname = storejson[0][rtl]
		except KeyError: rname = "Store"
		pushRaw = "Apple " + rname + " (R" + rtl + ") just updated,\nthe size of the picture is " + str(newsize / 1024) + " KB."
		upb = upb + pushRaw + "\n"; exce = exce + rtl + ", "; print pushRaw
		tellRaw = "零售店编号 R" + rtl + "，新图片大小是 " + str(newsize / 1024) + " KB。"
		imageURL = dieter + spr + "?output-format=jpg"
		os.system("wget -t 100 -T 8 --no-check-certificate --post-data 'value1=" + tellRaw 
			+ "&value2=🔔 Apple " + rname + " 图片更新&value3=" + imageURL + "' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey)
		os.system("rm -f " + masterKey + "*")
	else: 
		if(isSpecial):
			try: pname = "R" + rtl + ": " + storejson[0][rtl]
			except KeyError: pname = "R" + rtl
			if newsize == 0: print pid + " Checked " + pname + " does not exist, ignore."
			else: print pid + " Checked "+ pname + " has no update, ignore."

totalStore = 740
global upb; arg = 0; pid = str(os.getpid()); upb = exce = ""; rTime = 0
for m in sys.argv[1:]: arg += 1
rpath = os.path.expanduser('~') + "/Retail/"
isKey = os.path.isfile(os.path.expanduser('~') + "/key.txt")
if not isKey:
	print ("Please provide your IFTTT Maker key in ~/key.txt\n" +
	"Location of the txt can be edited in the source code."); exit()
else: kOpen = open(os.path.expanduser('~') + "/key.txt"); masterKey = kOpen.readline().replace("\n", ""); kOpen.close()
sbn = rpath + "Pictures/R"; dieter = "https://rtlimages.apple.com/cmc/dieter/store/16_9"
nameopen = open(rpath + "name.json"); storejson = json.loads(nameopen.read()); nameopen.close()

while True:
	reload(sys); sys.setdefaultencoding('utf-8')
	sTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()); eCount = exce.count(", ")
	if arg - eCount:
		print "Refreshing specified stores: " + str(rTime % 18 + 1) + "/18"
		for s in range(1, arg + 1): 
			if not sys.argv[s] in exce: down(sys.argv[s], True)
	else: print "No store was specified to watch: " + str(rTime % 18 + 1) + "/18"
	if not (rTime % 18):
		for j in range(1, totalStore): 
			down("%03d" % j, False)
			print pid + " Compare in Progress: " + str((j + 1) * 100 / totalStore) + "% on R" + "%03d" % j + "\r",
			sys.stdout.flush()
		print; asa()
	rTime += 1
	print upb + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
	time.sleep(1200)