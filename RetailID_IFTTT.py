# -*- coding:utf-8 -*-
import os, sys, urllib2, datetime, json, time

def filesize(url):
	opener = urllib2.build_opener()
	request = urllib2.Request(url)
	request.get_method = lambda: 'HEAD'
	try: response = opener.open(request); response.read()
	except Exception, e: return 0
	else: return int(dict(response.headers).get('content-length', 0))

def down(rtl, ps):
	spr = "/R" + rtl + ".png"; sx = sbn + rtl + ".png"
	exi = os.path.isfile(sx); newsize = filesize(dieter + "/16_9" + spr)
	nameopen = open("/home/pi/Retail/name.md"); storejson = json.loads(nameopen.read()); nameopen.close()
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize and newsize > 1:
		reload(sys); sys.setdefaultencoding('utf-8')
		pushRaw = "零售店图册 - Apple " + storejson[0][rtl] + " 刚刚获得了更新，店号 R" + rtl + "，图片大小 " + str(newsize / 1024) + " KB，访问 Apple 官网了解更多。"
		if exi: os.system("mv -n " + sbn + rtl + ".png " + rpath + "Other/previous/"); exi = False
		if not exi: os.system("wget -t 2 -c -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr)
		os.system('curl --connect-timeout 2 --retry 3 -X POST -H "Content-Type: application/json" -d' + "'" + '{"value1":"' + pushRaw + '"}'
			   + "' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x"); print
		os.system('curl --connect-timeout 2 --retry 3 -X POST -H "Content-Type: application/json" -d' + "'" + '{"value1":"' + pushRaw + '"}' 
			   + "' https://maker.ifttt.com/trigger/raw/with/key/bOGI8iEAyvjh782UYFKbRa"); print
		# GitHub users please notice: IFTTT key only uses for private.
		sys.argv[ps] = ""
	else: print "Checked R" + rtl +" has no update, ignore."

rpath = "/home/pi/Retail/"; sbn = rpath + "Pictures/R"
dieter = "https://rtlimages.apple.com/cmc/dieter/store"; arg = 0
sTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
for m in sys.argv[1:]: arg += 1
while True:
	arm = 0
	#os.system("clear")
	#for j in range(713, 714): down("%03d" % j)
	for j in range(1, arg + 1): down(sys.argv[j], j)
	for k in range(1, arg + 1):
		if sys.argv[k] == "": arm += 1
	if arm == arg: break
	print "Sleeping, interval will be 2hr."; time.sleep(7200)
print "\nStarted: " + sTime + "\nEnded:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())