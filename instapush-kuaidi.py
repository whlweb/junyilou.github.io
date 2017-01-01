#coding=utf-8
import sys, json, urllib2, time, datetime, os, fileinput
def relpy():
    reload(sys) 
    sys.setdefaultencoding('utf-8')
def home(readid):
    exsc = False; es = ""
    if readid != "":
        idt = readid + ".txt"; exi = os.path.isfile(idt)
        if exi:
            for line in fileinput.input(idt):
                orgCounter = int(line)
            fileinput.close()
        else:
            createFile = open(idt, 'w')
            createFile.write("0")
            createFile.close()
            orgCounter = 0
        urla = "https://www.kuaidi100.com/autonumber/autoComNum?text=" + readid
        countp = urllib2.urlopen(urla).read().count("comCode")
        if (countp - 1):
            comp = json.loads(urllib2.urlopen(urla).read())["auto"][0]["comCode"]
            urlb = "https://www.kuaidi100.com/query?type=" + comp + "&postid=" + readid
            responce = urllib2.urlopen(urlb)
            anst = responce.read(); ansj = json.loads(anst)
            today = datetime.datetime.now().strftime("%m月%d日")
            comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通'}
            if ansj["status"] == "200":
                erstat = 1
                maxnum = anst.count("location")
                if maxnum != orgCounter:
                    result = ansj["data"]
                    realComp = comtext.get(ansj["com"], "其他") + "快递"
                    fTime = time.strftime("%m月%d日 %H:%M", time.strptime(result[0]["time"], "%Y-%m-%d %H:%M:%S"))
                    relpy()
                    fContent = result[0]["context"].replace(" 【", "【").replace("】 ", "】")
                    signCheck = fContent.count("签收") + fContent.count("感谢")
                    if signCheck:
                        es = "[快件签收 停止推送] "
                        exsc = True
                    fileRefresh = open(idt, 'w')
                    fileRefresh.write(str(maxnum))
                    fileRefresh.close()
                    a='curl -X POST -H "x-instapush-appid: '; b='" -H "x-instapush-appsecret: '
                    c='" -H "Content-Type: application/json" -d '; d="'"
                    e='{"event":"kuaidi","trackers":{"rc":"'; f=realComp
                    g='","ri":"'; h=readid; i='","ft":"'; j=fTime; k='","fc":"'
                    l=fContent; m='"}'; n='}'; o="'"; p=' https://api.instapush.im/v1/post'
                    finalOut = "".join([a,AppID,b,AppSecret,c,d,e,es,f,g,h,i,j,k,l,m,n,o,p])
                    os.system(finalOut)
                    print
                else:
                    print "".join([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Checked ", readid, " has no update, ignore."])
            else:
                print "".join([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Checked ", readid, " returned error code ", ansj["status"], ", ignore."])
        else:
            print "".join([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Checked ", readid, " returned no auto-company, ignore."])
    return exsc
arg = signCheck = 0
for m in sys.argv[1:]: arg += 1
AppID = sys.argv[1]
AppSecret = sys.argv[2]
TimeInterval = int(sys.argv[3])*60
readid = sys.argv[4]
if TimeInterval < 30: TimeInterval = 30
while True:
    if home(readid) : break
    time.sleep(TimeInterval)
