import os, sys, fileinput, urllib2, platform, time

def filesize(url): 
    opener = urllib2.build_opener()
    request = urllib2.Request(url)
    request.get_method = lambda: 'HEAD'
    try: response = opener.open(request); response.read()
    except Exception, e: return 0
    else: return int(dict(response.headers).get('content-length', 0))

def down(rtl, argc):
	global cans; spr = "/R" + rtl + ".png"; sx = sbn + rtl + ".png" ; exi = os.path.isfile(sx); newsize = filesize(dieter + "/16_9" + spr)
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize and newsize > 100:
		if argc != "check":
			if exi: os.system("mv -n " + sbn + rtl + ".png " + rpath + "Other/previous" + spr); exi = False
			if not exi: os.system("wget -t 2 -c -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr)
		else:
			print "[" + rtl + "] " + str(newsize) + " compare to " + str(oldsize)
			cans = cans + rtl + ", "
	else: 
		if argc != "check": print "Photos of R" + rtl + " had been already downloaded or not ready yet."
		else: print rtl

arg = 0; rpath = ""; cans = ""
if "Linux" in platform.platform(): rpath = "/home/pi/Retail/"
if "Darwin" in platform.platform(): rpath = "/Users/Junyi_Lou/Downloads/Apple/Retail/"
sbn = rpath + "Pictures/R"; dieter = "https://rtlimages.apple.com/cmc/dieter/store"
for m in sys.argv[1:]: arg += 1
if sys.argv[1] == "check":
	print "Start checking in platform " + platform.platform()
	sTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	for i in range(1, 714): down("%03d" % i, "check")
	print "\nStarted: " + sTime + "\nEnded:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\nAnswer: " + cans
else: 
	for j in range(1, arg + 1): down(sys.argv[j], "")
print 