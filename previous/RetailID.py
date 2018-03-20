import os, sys, urllib2, platform, time

def filesize(url): 
    opener = urllib2.build_opener()
    request = urllib2.Request(url)
    request.get_method = lambda: 'HEAD'
    try: response = opener.open(request); response.read()
    except Exception, e: return 0
    else: return int(dict(response.headers).get('content-length', 0))

def down(rtl):
	global cans; spr = "/R" + rtl + ".png"; sx = sbn + rtl + ".png"
	exi = os.path.isfile(sx); newsize = filesize(dieter + "/16_9" + spr)
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize:
		if exi: os.system("mv -n " + sbn + rtl + ".png " + rpath + "Other/previous" + spr); exi = False
		if not exi: os.system("wget --no-check-certificate -t 2 -c -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr)
		if "Darwin" in platform.platform(): os.system("open " + rpath)
	else: 
		print "Photos of R" + rtl + " had been already downloaded or not ready yet."

arg = 0; rpath = ""; cans = ""
if "Linux" in platform.platform(): rpath = os.path.expanduser('~') + "/Retail/"
if "Darwin" in platform.platform(): rpath = os.path.expanduser('~') + "/Downloads/Apple/Raspberry/"
sbn = rpath + "Pictures/R"; dieter = "https://rtlimages.apple.com/cmc/dieter/store"
for m in sys.argv[1:]: arg += 1
for j in range(1, arg + 1): down(sys.argv[j])