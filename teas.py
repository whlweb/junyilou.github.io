#coding=utf-8
from flask import Flask, jsonify, request
import sys, json, urllib2, time, datetime, PyRSS2Gen
app = Flask(__name__)
@app.route('/', methods=['GET'])  
def home():
    readid = request.args.get('id').__str__()
    readmax = int(request.args.get('max').__str__())
    if readid != "None":
        urla = ''.join(["https://www.kuaidi100.com/autonumber/autoComNum?text=", readid])
        countp = urllib2.urlopen(urla).read().count("comCode")
        if (countp-1):
            comp = json.loads(urllib2.urlopen(urla).read())["auto"][0]["comCode"]
            urlb = ''.join(["https://www.kuaidi100.com/query?type=", comp, "&postid=", readid])
            responce = urllib2.urlopen(urlb)
            anst = responce.read(); ansj = json.loads(anst)
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%m月%d日")
            fronteday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%m月%d日")
            comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通'}
            if ansj["status"] == "200":
                erstat = 1
                maxnum = min(anst.count("location"),readmax)
                result = ansj["data"]
                tasks = list(range(maxnum+1))
#                tasks [0] = {'signature': erstat, 'postid': ansj["nu"],'comp': ''.join([comtext.get(ansj["com"],"其他"),"快递"]),'timestamp': int(time.time())} 
                for i in range (1, maxnum+1):
                    ResultTime = result[i-1]["time"]
                    StrfTime = time.strftime("%m月%d日 %H:%M", time.strptime(ResultTime, "%Y-%m-%d %H:%M:%S"))
                    result[i-1]["time"] = StrfTime.replace(yesterday,"昨天").replace(fronteday,"前天")
                for j in range (1, maxnum+1): 
                    tasks [j] = {'time': result[j-1]["time"],'content':result[j-1]["context"]}
            else:
            	a = 1
        else:
        	a = 1
    else:
    	a = 1
    rss = PyRSS2Gen.RSS2(
    	title = "".join(["Package Tracking ID",readid]),
    	link = "http://hk2.yuuki.moe:6555",
    	description = "".join([str(erstat), " ",comtext.get(ansj["com"],"其他")]),
    	lastBuildDate = datetime.datetime.now(),
    	items = [
    		PyRSS2Gen.RSSItem(
    			title = result[0]["time"],
    			link = "http://hk2.yuuki.moe:6555",
    			description = result[0]["context"],
    			pubDate = datetime.datetime.now()
    		)
    	]
    )
    rss.write_xml(open("".join([readid,".txt"]), "w"))
    f = open("".join([readid,".txt"]),'rb') 
    return f.read()
if __name__ == '__main__':  
    app.run(host='0.0.0.0',port=6555,debug=True)