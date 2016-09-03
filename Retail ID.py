# -*- coding:utf-8 -*-
#rtl = "%03d" % j
import os, sys, fileinput
def down():
	exia = os.path.isfile("".join([fourbythree, rtl, ".png"]))
	sx = "".join([sixbynine, rtl, ".png"])
	exib = os.path.isfile(sx)
	if exia and exib : exic = True
	else: exic = False
	if exic:
		print "".join(["\nPhotos of R",rtl," already found, checking..."])
		os.system("".join(["wget -q -t 3 -c ", dieter, "16_9/R", rtl, ".png"]))
		prefix = "".join(["/Users/Junyi_Lou/R", rtl, ".png"])
		newsize = os.path.getsize(prefix)
		oldsize = os.path.getsize(sx)
		if newsize != oldsize and newsize > 81920:
			os.system("".join(["mv -n ", sixbynine, rtl, ".png ", rpath, "/Other/R", rtl, ".png"]))
			os.system("".join(["rm ", fourbythree, rtl, ".png"]))
			fb = open("".join([rpath, "/List.md"]))
			newlist = fb.read().replace(("".join([rtl,","])),"")
			fb.close()
			fc = open("".join([rpath, "/List.md"]),"w")
			fc.write(newlist)
			fc.close()
			exic = False
		else:
			print "Photos may already downloaded or new photos not yet ready."
		os.remove(prefix)
	if not exic:
		equa = ["4_3", "16_9"]
		for k in range(0, 2):
			os.system("".join(["wget -t 3 -c -P ", rpath, "/", equa[k], "/ ", dieter, equa[k], "/R", rtl, ".png"])) 
			k = k + 1
arg = 0
rpath = "/Users/Junyi_Lou/Downloads/Retail"
sixbynine = "".join([rpath, "/16_9/R"])
fourbythree = "".join([rpath, "/4_3/R"])
dieter = "http://rtlimages.apple.com/cmc/dieter/store/"
for m in sys.argv[1:]: arg = arg + 1
if arg == 0:
	forloop = 1
	for line in fileinput.input("".join([rpath, "/List.md"])):
		for j in range (0, line.count(",")):
			rtl = (line.split(","))[j]
			down()
else:
	for j in range(1, arg + 1):
		rtl = sys.argv[j]
		down()
print