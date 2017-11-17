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
		pushRaw = "[零售店图片]Apple " + storejson[0][rtl] + " 刚刚更新，店号 R" + rtl + "，图片大小 " + str(newsize / 1024) + " KB。"
		if exi: os.system("mv -n " + sbn + rtl + ".png " + rpath + "Other/previous/"); exi = False
		os.system("wget -t 0 -c -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr)
		os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1=" + pushRaw 
				+ "' https://maker.ifttt.com/trigger/raw/with/key/dJ4B3uIsxyedsXeQKk_D3x")
		os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1=" + pushRaw 
				+ "' https://maker.ifttt.com/trigger/raw/with/key/bOGI8iEAyvjh782UYFKbRa")
		# GitHub users please notice: IFTTT key only uses for private.
		argv[ps] = ""; return 1
	else: print "Checked R" + rtl +" has no update, ignore."; return 0

rpath = "/home/pi/Retail/"; sbn = rpath + "Pictures/R"; argv = list(range(10))
dieter = "https://rtlimages.apple.com/cmc/dieter/store"; arg = arm = 0;
sTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
for m in sys.argv[1:]: arg += 1
for r in range (1, arg + 1): argv[r] = sys.argv[r]
while True:
	for j in range(1, arg + 1): 
		if argv[j] != "": ant = down(argv[j], j)
		if ant: arm += 1 
	if arm == arg: break
	print "Sleeping, interval will be 2hr."; time.sleep(7200)
print "\nStarted: " + sTime + "\nEnded:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())