# -*- coding:utf-8 -*-
import os, sys, fileinput, urllib2
def filesize(url): #通过HEAD分析远程文件大小
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
def down(rtl): #rtl样例 092
	spr = "".join(["/R", rtl, ".png"]) #spr样例 /R092.png
	sx = "".join([sbn, rtl, ".png"]) #sx样例 ~/Downloads/Retail/16_9/R092.png
	exi = os.path.isfile(sx) #exia为4:3存在bool, exib为16_9
	newsize = filesize("".join([dieter, "/16_9", spr]))
	if exi: oldsize = os.path.getsize(sx)
	else: oldsize = 0
	if newsize != oldsize and newsize > 409600:
		fb = open("".join([rpath, "List.md"]))
		newlist = fb.read().replace(("".join([rtl, ","])), ""); fb.close() #注意,不能空格替换
		fc = open("".join([rpath, "List.md"]), "w")
		fc.write(newlist); fc.close()
		if exi:
			os.system("".join(["mv -n ", sbn, rtl, ".png ", rpath, "Other/previous", spr]))
			exi = False
		if not exi:
			os.system("".join(["wget -t 2 -e \"http_proxy=http://127.0.0.1:6152\" -c -P ", rpath, "Pictures/ ", dieter, "/16_9", spr]))
			os.system("".join(["open ", sx]))
	else: print "".join(["Photos of R", rtl, " had been already downloaded or not ready yet."])		
arg = 0
rpath = "/Users/Junyi_Lou/Downloads/Apple/Retail/"
sbn = "".join([rpath, "Pictures/R"]) #~/Downloads/Retail/Pictures/R
dieter = "https://rtlimages.apple.com/cmc/dieter/store"
print
for m in sys.argv[1:]: arg += 1
if arg == 0:
	for line in fileinput.input("".join([rpath, "List.md"])):
		for j in range (0, line.count(",")): #注意,不能空格替换
			rtl = (line.split(","))[j] #注意,不能空格替换
			down(rtl)
else:
	for j in range(1, arg + 1):
		rtl = sys.argv[j]
		down(rtl)
print
