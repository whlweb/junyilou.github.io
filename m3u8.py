import os, sys

def output(cont, file):
	w = open(os.path.expanduser("~") + "/Desktop/" + file + ".txt", "w")
	w.write(cont); w.close()

arg = 0; a = b = c = ""; d = "cat "
for m in sys.argv[1:]: arg += 1
item = int(sys.argv[1]); item += 1; dNum = item / 3
m3u8URL = sys.argv[2].replace(".m3u8", ".mp4/")

for i in range(1, dNum):
	a += m3u8URL + "seg-" + str(i) + "-v1-a1.ts" + "\n"
for j in range(dNum, dNum * 2):
	b += m3u8URL + "seg-" + str(j) + "-v1-a1.ts" + "\n"
for k in range(dNum * 2, item):
	c += m3u8URL + "seg-" + str(k) + "-v1-a1.ts" + "\n"

output(a, "[1]"); output(b, "[2]"); output(c, "[3]")

d += "wget --user-agent='Mozilla' --header='Referer: https://avgle.com' -i\n\n"
for l in range(1, item): d += "seg-" + str(l) + "-v1-a1.ts "
d += "> comb.ts\n\n"
d += "ffmpeg -i comb.ts -acodec copy -vcodec copy -f mp4 comb.mp4\n"
d += "rm *.ts\nrm Desktop/[*.txt"

output(d, "[C]")
print "Done!"