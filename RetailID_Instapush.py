import os, sys, fileinput, urllib2, datetime, json, time
from instapush import Instapush, App
def filesize(url):
	opener = urllib2.build_opener()
	request = urllib2.Request(url)
	request.get_method = lambda: 'HEAD'
	try:
		response = opener.open(request)
		response.read()
	except Exception, e: return 0
	else: return int(dict(response.headers).get('content-length', 0))
def down(rtl):
	tmnow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	spr = "R" + rtl + ".png"; sx = sbn + rtl + ".png"
	exi = os.path.isfile(sx)
	newsize = filesize(dieter + "/16_9/" + spr)
	nameopen = open(rpath + "name.md")
	storejson = json.loads(nameopen.read())
	nameopen.close()
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize and newsize > 1024000:
		fb = open(rpath + "List.md")
		newlist = fb.read().replace((rtl + ","), ""); fb.close()
		fc = open(rpath + "List.md", "w")
		fc.write(newlist); fc.close()
		app = App(appid = "585e4e62a4c48a05d607b545", secret = "a32883f25245516940ea6b9f9b80fa54")
		app.notify(event_name = 'retail', trackers = {'rtl': rtl, 'size': str(newsize / 1024)+"KB", 'name': storejson[0][rtl]})
		app = App(appid = "58e64646a4c48abbdd14b36c", secret = "0480f2c86128ba527b520053bab047a8")
		app.notify(event_name = 'retail', trackers = {'rtl': rtl, 'size': str(newsize / 1024)+"KB", 'name': storejson[0][rtl]})
		# GitHub users please notice: AppSecret only uses for private.
		os.system("sudo rm " + sbn + rtl + ".png")
		os.system("sudo wget -t 2 -c -P " + rpath + " " + dieter + "/16_9/" + spr)
	else: print tmnow + " Checked R" + rtl +" has no update, ignore."
rpath = "/home/pi/Retail/"
sbn = rpath + "R"
dieter = "https://rtlimages.apple.com/cmc/dieter/store"
while True:
	for line in fileinput.input(rpath + "List.md"):
		for j in range (0, line.count(",")):
			rtl = (line.split(","))[j]
			down(rtl)
	print "Sleeping, interval will be 1 hr."; time.sleep(3600)