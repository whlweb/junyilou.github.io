#coding=utf-8
from flask import Flask, jsonify, request
import sys, json, urllib2, time, datetime
import sys
app = Flask(__name__)
@app.route('/', methods=['GET'])  
def home():
    readid = request.args.get('id').__str__()
    if readid != "None":
        urla = ''.join(["https://www.kuaidi100.com/autonumber/autoComNum?text=", readid])
        countp = urllib2.urlopen(urla).read().count("comCode")
        if (countp-1):
            comp = json.loads(urllib2.urlopen(urla).read())["auto"][0]["comCode"]
            urlb = ''.join(["https://www.kuaidi100.com/query?type=", comp, "&postid=", readid])
            responce = urllib2.urlopen(urlb)
            anst = responce.read(); ansj = json.loads(anst)
            today = datetime.datetime.now().strftime("%m月%d日")
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%m月%d日")
            fronteday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%m月%d日")
            comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通'}
            blankOutput = "".join(['<?xml version="1.0"?><rss version="2.0"><channel><title>快递单号 ',readid,"</title><link>http://t.cn/RI2gPuN</link><description>一个快件跟踪RSS</description><item></item><</channel></rss>"])
            if ansj["status"] == "200":
                erstat = 1
                maxnum = anst.count("location")
                result = ansj["data"]
                realComp = ''.join([comtext.get(ansj["com"],"其他"),"快递"])
                output = "".join(['<?xml version="1.0"?><rss version="2.0"><channel><title>',realComp,' ',readid,'</title><link>http://t.cn/RI2gPuN</link><description>一个快件跟踪RSS</description>'])
                for i in range (1, maxnum+1):
                    ResultTime = result[i-1]["time"]
                    StrfTime = time.strftime("%m月%d日 %H:%M", time.strptime(ResultTime, "%Y-%m-%d %H:%M:%S"))
                    result[i-1]["time"] = StrfTime.replace(today,"今天").replace(yesterday,"昨天").replace(fronteday,"前天")
                    fTime = result[i-1]["time"]; fContent = result[i-1]["context"]
                    reload(sys) 
                    sys.setdefaultencoding('utf-8')
                    fContent = fContent.replace(" 【","【").replace("】 ","】")
                    output = "".join([output, '<item><title>',fTime,'</title><link>http://t.cn/RI2gPuN</link><description>',fContent,'</description></item>'])
                output = "".join([output,"</channel></rss>"])
            else:
                output = blankOutput
        else:
            output = blankOutput
    else:
        readid = "N/A"
        output = blankOutput
    return output
if __name__ == '__main__':  
    app.run(host='0.0.0.0',port=6555,debug=False)