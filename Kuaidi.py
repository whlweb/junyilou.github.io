# -*- coding:utf-8 -*-
import sys, json, urllib2, time, datetime, os, signal, exceptions

arg = signCheck = brew = tti = 0; nt = ""
endl = "\n"; argv = list(range(50))

def blanker(bid, notice): 
	insTime = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
	print "[" + str(os.getpid()) + "] " + insTime + " " + bid + " " + notice + ".\r",
	sys.stdout.flush()

def netTry(tryurl):
	try: response = urllib2.urlopen(tryurl)
	except: return "network"
	else: return response.read()

def pushbots(pushRaw, pushTitle, pushURL): 
	os.system("wget -t 100 -T 3 --no-check-certificate --post-data 'value1=" +
			pushRaw + "&value2=" + pushTitle + "&value3=" + pushURL +
			"' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey[0])

def autocomp(readid):
	aTry = netTry("https://www.kuaidi100.com/autonumber/autoComNum?text=" + readid)
	if aTry != "network":
		countp = aTry.count("comCode")
		if countp >= 2: return json.loads(aTry)["auto"][0]["comCode"]
		else: return "noAnswer"
	else: return "networkFailed"

def home(readid):
	noShow = False; orgCounter = exsc = 0; es = ""; idt = FileLocation + readid + ".txt"; comp = "auto"; linetime = "N/A"
	if not os.path.isfile(idt): os.system("cd >" + idt); es = "[新增]"
	dtRead = open(idt); dt = dtRead.read()
	if len(dt) > 2:
		comp = dt.split(", ")[0]
		try: orgCounter = int(dt.split(", ")[1])
		except (IndexError, exceptions.ValueError): pass
		try: linetime = dt.split(", ")[2]
		except (IndexError, exceptions.ValueError): pass
	dtRead.close()
	if comp == "auto": comp = autocomp(readid)
	if comp != "noAnswer":
		urlb = "https://www.kuaidi100.com/query?type=" + comp + "&postid=" + readid; tryb = netTry(urlb)
		if tryb != "network":
			ansj = json.loads(tryb)
			comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通', 'jd': '京东', 'ems': '邮政 EMS', 'zhaijisong': '宅急送'}
			if ansj["status"] == "200":
				maxnum = tryb.count("location")
				if maxnum > orgCounter:
					result = ansj["data"]
					realComp = comtext.get(ansj["com"], "其他") + "快递"
					fTime = time.strftime("%-m月%-d日 %H:%M", time.strptime(result[0]["time"], "%Y-%m-%d %H:%M:%S"))
					if linetime.count(fTime) > 0: noShow = True
					reload(sys); sys.setdefaultencoding('utf-8')
					fContent = result[0]["context"].replace(" 【", "【").replace("】 ", "】").replace(" （", "（").replace(" ）", ")")
					fContent = fContent.replace("( ", "(").replace(" )", ")").replace('"(点击查询电话)"', "")
					signCount = fContent.count("签收") + fContent.count("感谢") + fContent.count("代收") + fContent.count("取件")
					sendCount = fContent.count("派送") + fContent.count("派件") + fContent.count("准备") + fContent.count("正在") + fContent.count("发往")
					if signCount > 0 and (signCount - sendCount) > 0: es = "[签收] "; exsc = maxnum;
					fileRefresh = open(idt, 'w'); fileRefresh.write(comp + ", " + str(maxnum) + ", " + fTime); fileRefresh.close()
					end = es + fTime + " " + fContent; realComp = realComp.replace("EMS快递", "EMS"); pushImage = ""
					if "其他" in realComp: pushImage = bkPloc + "other.png"
					else: pushImage = bkPloc + ansj["com"] + ".png"
					if noShow == False: print end + endl; pushbots(end, "快递查询: " + realComp + " " + readid, pushImage)
					else: blanker(readid, "[noShow]")
				else: 
					if maxnum == orgCounter: blanker(readid, "[Pass]")
					if maxnum < orgCounter: blanker(readid, "[lessPut]")
			else:
				blanker(readid, "[API " + ansj["status"] + "]")
				if ansj["status"] == "400": blanker(readid, "[COMCODE " + comp + "]")
		else: blanker(readid, "[NetworkFailed]")
	else: blanker(readid, "[" + comp + "]")
	os.system("rm -f " + FileLocation + masterKey[0] + "*")
	global tti; tti += 1; return exsc

for m in sys.argv[1:]: arg += 1; brew = arg
TimeInterval = 600
FileLocation = os.path.expanduser('~') + "/"
for r in range (1, arg + 1): argv[r] = sys.argv[r]
print (endl + "Start with PID " + str(os.getpid()) + "." +
	endl + "Time interval will be 10 minutes." + endl)
bkPloc = "https://junyilou.github.io/bkP/c_"

isKey = os.path.isfile(FileLocation + "key.txt")
if not isKey:
	print ("Please provide your IFTTT key in ~/key.txt" + endl +
	"Location of the txt can be edited in the source code."); exit()
else: 
	kOpen = open(FileLocation + "key.txt")
	masterKey = list()
	for line in open(FileLocation + "key.txt"):
		line = kOpen.readline().replace(endl, "")
		masterKey.append(line)
	kOpen.close()

print "Latest update:"
while True:
	checkbrew = str(argv).count("-")
	for n in range(1, arg + 1): 
		readid = argv[n]
		if readid != "-": stat = home(readid)
		else: stat = 0
		if stat:
			print "Checked " + str(readid) + " signed, " + str(stat) + " updates in total recorded."
			argv[n] = "-"; os.system("rm " + FileLocation + readid + ".txt")
	if checkbrew == brew: break
	time.sleep(TimeInterval)

for ntm in range (0, 45): nt = nt + "="
print (endl + "Summary:" + endl + nt + endl + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
	+ " All " + str(brew) + " signed, exit." + endl + nt + endl)
if brew > 0: pushbots("共 " + str(brew) + " 个快递单已经被识别为签收，程序自动退出。签收单号为 " 
	+ ", ".join(sys.argv[1:]) + "。", "快递查询: 退出提示", bkPloc + "exit.png")