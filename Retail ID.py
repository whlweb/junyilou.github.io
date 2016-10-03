# -*- coding:utf-8 -*-
#rtl = "%03d" % j
import os, sys, fileinput
def down():
	spr = "".join(["/R", rtl, ".png"])
	exia = os.path.isfile("".join([fbt, rtl, ".png"]))
	sx = "".join([sbn, rtl, ".png"])
	exib = os.path.isfile(sx)
	if exia and exib : exic = True
	else: exic = False
	if exic:
		print "".join(["\nPhotos of R",rtl," already found, checking..."])
		os.system("".join(["wget -q -t 3 -c ", dieter, "16_9", spr]))
		prefix = "".join(["/Users/Junyi_Lou",spr])
		newsize = os.path.getsize(prefix); oldsize = os.path.getsize(sx)
		if newsize != oldsize and newsize > 81920:
			os.system("".join(["mv -n ", sbn, rtl, ".png ", rpath, "/Other", spr," && rm ", fbt, rtl, ".png"]))
			fb = open("".join([rpath, "/List.md"]))
			newlist = fb.read().replace(("".join([rtl, ","])), ""); fb.close()
			fc = open("".join([rpath, "/List.md"]),"w")
			fc.write(newlist); fc.close()
			exic = False
		else: print "Photos may already downloaded or new photos not yet ready."
		os.remove(prefix)
	if not exic:
		equa = ["4_3", "16_9"]
		for k in range(0, 2):
			os.system("".join(["wget -t 2 -c -P ", rpath, "/", equa[k], "/ ", dieter, equa[k], spr])) 
			k += 1
		os.system("".join(["open ", sx]))
arg = 0
rpath = "/Users/Junyi_Lou/Downloads/Retail"
sbn = "".join([rpath, "/16_9/R"]) #sixteen by nine
fbt = "".join([rpath, "/4_3/R"]) #four by three
dieter = "http://rtlimages.apple.com/cmc/dieter/store/"
for m in sys.argv[1:]: arg += 1
if arg == 0:
	fl = 0
	for line in fileinput.input("".join([rpath, "/List.md"])):
		fl += 1
		if fl < 2:
			for j in range (0, line.count(",")):
				rtl = (line.split(","))[j]
				down()
else:
	for j in range(1, arg + 1):
		rtl = sys.argv[j]
		down()
print