import os, sys, fileinput, urllib2
def filesize(url): 
    opener = urllib2.build_opener()
    request = urllib2.Request(url)
    request.get_method = lambda: 'HEAD'
    try: response = opener.open(request); response.read()
    except Exception, e: return 0
    else: return int(dict(response.headers).get('content-length', 0))
def down(rtl, argc):
	spr = "/R" + rtl + ".png"; sx = sbn + rtl + ".png" ; exi = os.path.isfile(sx); newsize = filesize(dieter + "/16_9" + spr)
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize and newsize > 100:
		if argc != "check":
			fb = open(rpath + "List.md"); newlist = fb.read().replace((rtl + ","), ""); fb.close()
			fc = open(rpath + "List.md", "w"); fc.write(newlist); fc.close()
			if exi:
				os.system("mv -n " + sbn + rtl + ".png " + rpath + "Other/previous" + spr); exi = False
			if not exi:
				os.system("wget -t 2 -e http_proxy=127.0.0.1:6152 -c -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr); os.system("open " + sx)
		else: print "[" + rtl + "]"
	else: 
		if argc != "check": print "Photos of R" + rtl + " had been already downloaded or not ready yet."
		else: print rtl
arg = 0; rpath = "/Users/Junyi_Lou/Downloads/Apple/Retail/"
sbn = rpath + "Pictures/R"; dieter = "https://rtlimages.apple.com/cmc/dieter/store"
for m in sys.argv[1:]: arg += 1
if arg == 0:
	for line in fileinput.input(rpath + "List.md"):
		for j in range (0, line.count(",")): 
			down((line.split(","))[j], "")
else:
	if sys.argv[1] == "check":
		for i in range(1, 706): down("%03d" % i, "check")
	else: 
		for j in range(1, arg + 1): down(sys.argv[j], "")
print