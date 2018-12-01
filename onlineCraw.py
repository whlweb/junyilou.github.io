#-*- coding:utf-8 -*-
import urllib2, os, sys, time, ssl
from BeautifulSoup import BeautifulSoup

alphabet = ([chr(i) for i in range(65, 73)] + [chr(i) for i in range(74, 79)] + 
			[chr(i) for i in range(80, 83)] + [chr(i) for i in range(84, 91)]) #I, O, S
numlist = [chr(i) for i in range(48, 58)]
flist = numlist + alphabet
psbhd = ['T', 'U', 'V']
ans = list()

def title(partno):
	reload(sys); sys.setdefaultencoding('utf-8')
	url = "https://www.apple.com/cn/shop/product/" + partno
	try: soup = BeautifulSoup(urllib2.urlopen(url, timeout = 30))
	except ssl.SSLError: return "[获取产品名称超时]"
	else: return soup.title.string.replace(" - Apple (中国)", "").replace(" - Apple", "").replace("购买 ", "")

for k in range(0, len(psbhd)):
	for i in range(0, len(flist)):
		for j in range(0, len(flist)):
			slct = psbhd[k] + flist[i] + flist[j]
			ans.append('M' + slct + '2')

runtim = 0; upb = ""
isKey = os.path.isfile(os.path.expanduser('~') + "/key.txt")
if not isKey:
	print ("Please provide your IFTTT key in ~/key.txt\n" +
	"Location of the txt can be edited in the source code."); exit()
else: 
	kOpen = open(os.path.expanduser('~') + "/key.txt")
	masterKey = list()
	for line in open(os.path.expanduser('~') + "/key.txt"):
		line = kOpen.readline().replace("\n", "")
		masterKey.append(line)
	kOpen.close()

while True:
	runtim += 1; runnot = "[" + str(runtim) + "] "
	mOpen = open(os.path.expanduser('~') + "/savedProduct")
	mRead = mOpen.read(); mOpen.close()
	for a in range(0, len(ans)):
		url = 'https://www.apple.com/cn/shop/product/' + ans[a]
		try: p = urllib2.urlopen(url, timeout = 20)
		except ssl.SSLError: 
			print runnot + ans[a] + " 500 [" + str(a + 1) + "/" + str(len(ans)) + "]\r",
 			sys.stdout.flush()
		except urllib2.HTTPError: 
			print runnot + ans[a] + " 404 [" + str(a + 1) + "/" + str(len(ans)) + "]\r",
			sys.stdout.flush()
		else: 
			if ans[a] in mRead: 
				print runnot + ans[a] + " 302 [" + str(a + 1) + "/" + str(len(ans)) + "]\r",
				sys.stdout.flush()
			else:
				uOut = "New Product Found: " + ans[a] + " at " + str(a + 1) + "/" + str(len(ans)) + "\n"
				print "\n" + uOut; upb += uOut
				picURL = ("https://as-images.apple.com/is/image/AppleInc/aos/published/images" + 
				"/M/" + ans[a][:2] + "/" + ans[a] + "/" + ans[a] + "?fmt=jpg")
				hWrite = open(os.path.expanduser('~') + "/savedProduct", "w"); hWrite.write(mRead + ans[a] + "\n"); hWrite.close();
				os.system("wget -t 100 -T 5 --no-check-certificate --post-data 'value1=Apple Online Store 更新了新产品：" 
					+ title(ans[a]) + "，产品部件号：" + ans[a] + "。&value2=" + picURL + "&value3=" + url 
					+ "' https://maker.ifttt.com/trigger/linkraw/with/key/" + masterKey[0])
				os.system("rm -f " + masterKey[0] + "*")
	print "\n" + upb + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
	time.sleep(1800)