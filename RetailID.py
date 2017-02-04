import os, sys, fileinput, urllib2
def filesize(url): 
    opener = urllib2.build_opener()
    opener.add_handler(urllib2.ProxyHandler({'https' : "127.0.0.1:6152"}))  
    opener.add_handler(urllib2.ProxyHandler({'http' : "127.0.0.1:6152"}))
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
	spr = "/R" + rtl + ".png"
	sx = sbn + rtl + ".png" 
	exi = os.path.isfile(sx)
	newsize = filesize(dieter + "/16_9" + spr)
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize and newsize > 409600:
		fb = open(rpath + "List.md")
		newlist = fb.read().replace((rtl + ","), ""); fb.close()
		fc = open(rpath + "List.md", "w")
		fc.write(newlist); fc.close()
		if exi:
			os.system("mv -n " + sbn + rtl + ".png " + rpath + "Other/previous" + spr)
			exi = False
		if not exi:
			os.system("wget -t 2 -e http_proxy=127.0.0.1:6152 -c -P " + rpath + "Pictures/ " + dieter + "/16_9" + spr)
			os.system("open " + sx)
	else: print "Photos of R" + rtl + " had been already downloaded or not ready yet."		
arg = 0
rpath = "/Users/Junyi_Lou/Downloads/Apple/Retail/"
sbn = rpath + "Pictures/R" 
dieter = "https://rtlimages.apple.com/cmc/dieter/store"
print
for m in sys.argv[1:]: arg += 1
if arg == 0:
	for line in fileinput.input(rpath + "List.md"):
		for j in range (0, line.count(",")): 
			rtl = (line.split(","))[j]
			down(rtl)
else:
	for j in range(1, arg + 1):
		rtl = sys.argv[j]
		down(rtl)
print