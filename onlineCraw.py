#-*- coding:utf-8 -*-
import urllib2, os, sys, time
from BeautifulSoup import BeautifulSoup

alphabet = [chr(i) for i in range(65,91)]
numlist = [chr(i) for i in range(48,58)]
flist = alphabet + numlist
psbhd = ['U', 'V']
ans = list()

def title(partno):
	reload(sys); sys.setdefaultencoding('utf-8')
	url = "https://www.apple.com/cn/shop/product/" + partno
	soup = BeautifulSoup(urllib2.urlopen(url))
	return partno + " " + soup.title.string.replace(" - Apple (中国)", "").replace("购买 ", "")

for k in range(0, len(psbhd)):
	for i in range(0, len(flist)):
		for j in range(0, len(flist)):
			slct = psbhd[k] + flist[i] + flist[j]
			ans.append('M' + slct + '2')

kOpen = open(os.path.expanduser('~') + "/MU.txt")
kRead = kOpen.read(); kOpen.close()
pushAns = ""; runtim = 0

while True:
	runtim += 1
	for a in range(0, len(ans)):
		url = 'https://www.apple.com/cn/shop/product/' + ans[a]
		try: p = urllib2.urlopen(url, timeout=5)
		except urllib2.HTTPError: 
			print str(runtim) + " " + ans[a] + " 404 [" + str(a) + "/" + str(len(ans)) + "]\r",
			sys.stdout.flush()
		else: 
			if ans[a] in kRead: 
				print str(runtim) + " " + ans[a] + " 302 [" + str(a) + "/" + str(len(ans)) + "]\r",
				sys.stdout.flush()
			else:
				kWrite = open(os.path.expanduser('~') + "/MU.txt", "w"); kWrite.write(kRead + ans[a] + "\n"); kWrite.close();
				pushAns = pushAns + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + ans[a] + "\n"
				os.system("wget -t 100 -T 5 --no-check-certificate --post-data 'value1=重要的事情说三遍：新产品！！这一次先不告诉你是什么东西你赶紧看看，再不看就买不到了！！" 
				+ "&value2=https://www.apple.com/cn/home/images/heroes/holiday/holiday_hero_1c_medium_2x.jpg"
				+ "&value3=" + url + "' https://maker.ifttt.com/trigger/linkraw/with/key/d8xzMnWyRiM9cI4i0Zz6Cm")
				os.system("wget -t 100 -T 5 --no-check-certificate --post-data 'value1=重要的事情说三遍：新产品！！新产品的 Part Number 是 " + ans[a] + "，马上买买买！！" 
				+ "&value2=https://www.apple.com/cn/home/images/heroes/holiday/holiday_hero_1c_medium_2x.jpg"
				+ "&value3=" + url + "' https://maker.ifttt.com/trigger/linkraw/with/key/d8xzMnWyRiM9cI4i0Zz6Cm")
				os.system("wget -t 100 -T 5 --no-check-certificate --post-data 'value1=重要的事情说三遍：新产品！！新产品是 " + title(ans[a])
				+ "&value2=https://www.apple.com/cn/home/images/heroes/holiday/holiday_hero_1c_medium_2x.jpg"
				+ "&value3=" + url + "' https://maker.ifttt.com/trigger/linkraw/with/key/d8xzMnWyRiM9cI4i0Zz6Cm")
	print pushAns
	time.sleep(60)
