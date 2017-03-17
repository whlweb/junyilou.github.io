# -*- coding:utf-8 -*-
import sys, json, urllib2, time, datetime, os, fileinput, signal
arg = signCheck = siging = brew = 0; sm = binvar = ""; argv = list(range(10))

def user1(a,b): global binvar; binvar += "0"
def user2(a,b): global binvar; binvar += "1"
signal.signal(signal.SIGUSR1,user1)
signal.signal(signal.SIGUSR2,user2)
def sig_start(a,b):
	global siging, binvar; siging = 1; binvar = ""
	print 'Received Linux siganal, analyzing.'
def sig_end(a,b): 
	global siging, arg, binvar, brew; sigans = int(binvar,2); siging = 0
	print "Binary: " + binvar + "\nReceived new readid:", sigans
	arg += 1; brew += 1; argv[arg] = str(sigans); binvar = ""
signal.signal(signal.SIGCONT,sig_start)
signal.signal(signal.SIGTERM,sig_end)

def blanker(bid, notice):
	blanktime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print str(os.getpid()) + " " + blanktime + " Checked " + bid + " " + notice + ", ignore."
def pytry(tryurl):
	try: response = urllib2.urlopen(tryurl)
	except urllib2.URLError as err: 
		if hasattr(err, 'reason') or hasattr(err, 'code'): return "False"
	else: return response.read()
def home(readid):
	exsc = False; es = ""
	idt = FileLocation + '/' + readid + ".txt"; exi = os.path.isfile(idt)
	if exi:
		for line in fileinput.input(idt): orgCounter = int(line)
		fileinput.close()
	else:
		createFile = open(idt, 'w'); createFile.write("0")
		createFile.close(); orgCounter = 0
	urla = "https://www.kuaidi100.com/autonumber/autoComNum?text=" + readid; trya = pytry(urla)
	if trya != "False": countp = trya.count("comCode")
	else: countp = 1
	if (countp - 1):
		comp = json.loads(urllib2.urlopen(urla).read())["auto"][0]["comCode"]
		urlb = "https://www.kuaidi100.com/query?type=" + comp + "&postid=" + readid; tryb = pytry(urlb)
		if tryb != "False":
			anst = tryb; ansj = json.loads(anst)
			today = datetime.datetime.now().strftime("%m月%d日")
			comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通', 'jd': '京东'}
			if ansj["status"] == "200":
				erstat = 1
				maxnum = anst.count("location")
				if maxnum != orgCounter:
					result = ansj["data"]
					realComp = comtext.get(ansj["com"], "其他") + "快递"
					fTime = time.strftime("%m月%d日 %H:%M", time.strptime(result[0]["time"], "%Y-%m-%d %H:%M:%S"))
					reload(sys); sys.setdefaultencoding('utf-8')
					fContent = result[0]["context"].replace(" 【", "【").replace("】 ", "】")
					signCount = fContent.count("签收") + fContent.count("感谢") + fContent.count("代收")
					sendCount = fContent.count("派送") + fContent.count("派件") + fContent.count("准备")
					if signCount > 0 and sendCount < 1:
						es = "[签收] "; exsc = maxnum
					fileRefresh = open(idt, 'w'); fileRefresh.write(str(maxnum)); fileRefresh.close()
					a='curl -X POST -H "x-instapush-appid: '; b='" -H "x-instapush-appsecret: '
					c='" -H "Content-Type: application/json" -d '; d="'"
					e='{"event":"kuaidi","trackers":{"rc":"'; f=realComp
					g='","ri":"'; h=readid; i='","ft":"'; j=fTime; k='","fc":"'
					l=fContent; m='"}'; n='}'; o="'"; p=' https://api.instapush.im/v1/post'
					finalOut = a+AppID+b+AppSecret+c+d+e+es+f+g+h+i+j+k+l+m+n+o+p
					os.system(finalOut); print
				else: blanker(readid, "has no update")
			else: blanker(readid, "returned code " + ansj["status"])
		else: blanker(readid, "has HTTP-Connect error")
	else: blanker(readid, "returned no auto-company")
	return exsc
for m in sys.argv[1:]: arg += 1; brew = arg;
AppID = "585e4e62a4c48a05d607b545"
AppSecret = "a32883f25245516940ea6b9f9b80fa54"
TimeInterval = int(sys.argv[1])*60
FileLocation = sys.argv[2]
for r in range (1,arg + 1): argv[r] = sys.argv[r]
print "\nStart with PID " + str(os.getpid()) + "."
print "Time interval will be " + sys.argv[1] + "min.\n"
while True:
	if not siging:
		checkbrew = str(argv).count("-")
		for n in range(3, arg + 1):
			readid = argv[n]
			if readid != "-": stat = home(readid)
			else: stat = 0
			if stat:
				print "Checked " + str(readid) + " signed, " + str(stat) + " updates in total recorded."
				argv[n] = "-"; os.system("rm " + FileLocation + '/' + readid + ".txt")
		if checkbrew == (brew-2): break
		time.sleep(TimeInterval)
	if checkbrew == (brew-2): break
nt = "============================================="
st = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print "\nSummary:\n" + nt + "\n" + st + " All " + str(brew-2) + " packages signed, exit.\n" + nt