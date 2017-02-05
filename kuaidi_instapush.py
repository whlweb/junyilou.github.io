# -*- coding:utf-8 -*-
import sys, json, urllib2, time, datetime, os, fileinput
def blanker(bid, notice):
	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Checked " + bid + " " + notice + ", ignore."
def pytry(tryurl):
	try:
		response = urllib2.urlopen(tryurl)
	except urllib2.URLError as err:
		if hasattr(err, 'reason') or hasattr(err, 'code'): return "False"
	else:
		return response.read()
def home(readid):
	exsc = False; es = ""
	if readid != "":
		idt = FileLocation + '/' + readid + ".txt"; exi = os.path.isfile(idt)
		if exi:
			for line in fileinput.input(idt):
				orgCounter = int(line)
			fileinput.close()
		else:
			createFile = open(idt, 'w')
			createFile.write("0")
			createFile.close()
			orgCounter = 0
		urla = "https://www.kuaidi100.com/autonumber/autoComNum?text=" + readid; trya = pytry(urla)
		if trya != "False":
			countp = trya.count("comCode")
		else:
			countp = 1
		if (countp - 1):
			comp = json.loads(urllib2.urlopen(urla).read())["auto"][0]["comCode"]
			urlb = "https://www.kuaidi100.com/query?type=" + comp + "&postid=" + readid; tryb = pytry(urlb)
			if tryb != "False":
				anst = tryb; ansj = json.loads(anst)
				today = datetime.datetime.now().strftime("%m月%d日")
				comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通'}
				if ansj["status"] == "200":
					erstat = 1
					maxnum = anst.count("location")
					if maxnum != orgCounter:
						result = ansj["data"]
						realComp = comtext.get(ansj["com"], "其他") + "快递"
						fTime = time.strftime("%m月%d日 %H:%M", time.strptime(result[0]["time"], "%Y-%m-%d %H:%M:%S"))
						reload(sys); sys.setdefaultencoding('utf-8')
						fContent = result[0]["context"].replace(" 【", "【").replace("】 ", "】")
						signCheck = fContent.count("签收") + fContent.count("感谢")
						if signCheck:
							es = "[签收] "
							exsc = True
						fileRefresh = open(idt, 'w')
						fileRefresh.write(str(maxnum))
						fileRefresh.close()
						a='curl -X POST -H "x-instapush-appid: '; b='" -H "x-instapush-appsecret: '
						c='" -H "Content-Type: application/json" -d '; d="'"
						e='{"event":"kuaidi","trackers":{"rc":"'; f=realComp
						g='","ri":"'; h=readid; i='","ft":"'; j=fTime; k='","fc":"'
						l=fContent; m='"}'; n='}'; o="'"; p=' https://api.instapush.im/v1/post'
						finalOut = a+AppID+b+AppSecret+c+d+e+es+f+g+h+i+j+k+l+m+n+o+p
						os.system(finalOut); print
					else:
						blanker(readid,"has no update")
				else:
					blanker(readid, "returned error code " + ansj["status"])
			else:
				blanker(readid, "has HTTP-Connection error")
		else:
			blanker(readid, "returned no auto-company")
	else:
		blanker("-", "readid is signed or empty")
	return exsc
arg = signCheck = 0
for m in sys.argv[1:]: arg += 1
AppID = sys.argv[1]
AppSecret = sys.argv[2]
TimeInterval = int(sys.argv[3])*60
if TimeInterval < 30: TimeInterval = 30
FileLocation = sys.argv[4]
print "Start. Time interval will be " + str(TimeInterval) + " minutes."
while True:
	for n in range(5, arg + 1):
		readid = sys.argv[n]
		if home(readid):
			sys.argv[n] = ""
	time.sleep(TimeInterval)