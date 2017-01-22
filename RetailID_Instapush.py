import os, sys, fileinput, urllib2, datetime, json, time
def filesize(url):
    opener = urllib2.build_opener()
    request = urllib2.Request(url)
    request.get_method = lambda: 'HEAD'
    try:
        response = opener.open(request)
        response.read()
    except Exception, e:
        return 0
    else:
        return int(dict(response.headers).get('content-length', 0))
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
	if newsize != oldsize and newsize > 409600:
		fb = open(rpath + "List.md")
		newlist = fb.read().replace((rtl + ","), ""); fb.close()
		fc = open(rpath + "List.md", "w")
		fc.write(newlist); fc.close()
		a='curl -X POST -H "x-instapush-appid: '; b='" -H "x-instapush-appsecret: '
		c='" -H "Content-Type: application/json" -d '; d="'"
		e='{"event":"retail","trackers":{"rtl":"'; f=rtl
		g='","size":"'; h=str(newsize / 1024)+"KB"; i='","name":"';
		j=storejson[0][rtl]; m='"}'; n='}'; o="'"; 
		p=' https://api.instapush.im/v1/post'
		AppID = "585e4e62a4c48a05d607b545"; AppSecret = "a32883f25245516940ea6b9f9b80fa54"
		finalOut = a+AppID+b+AppSecret+c+d+e+f+g+h+i+j+m+n+o+p
		os.system(finalOut)
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
	for t in range(1,12):
		print "Sleeping. " + str(12 - t) + " hours out of 12 hours left."
		time.sleep(3600)