#coding=utf-8
from flask import Flask, request
import sys, json, urllib2, time, datetime
def relpy():
    reload(sys) 
    sys.setdefaultencoding('utf-8')
def blanker(bid, reason):
    return '<?xml version="1.0"?>\n<rss version="2.0">\n<channel><title>快递单号 ' + bid + "</title><link>http://t.cn/RI2gPuN</link><description>一个快件跟踪RSS</description><item><title>" + reason + "</title><link>http://t.cn/RI2gPuN</link><description>查询错误</description></item></channel></rss>"
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    readid = request.args.get('id').__str__()
    if readid != "None":
        urla = "https://www.kuaidi100.com/autonumber/autoComNum?text=" + readid
        countp = urllib2.urlopen(urla).read().count("comCode")
        if (countp-1):
            comp = json.loads(urllib2.urlopen(urla).read())["auto"][0]["comCode"]
            urlb = "https://www.kuaidi100.com/query?type=" + comp + "&postid=" + readid
            responce = urllib2.urlopen(urlb)
            anst = responce.read(); ansj = json.loads(anst)
            today = datetime.datetime.now().strftime("%m月%d日")
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%m月%d日")
            fronteday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%m月%d日")
            comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通'}
            if ansj["status"] == "200":
                erstat = 1
                maxnum = anst.count("location")
                result = ansj["data"]
                url = 'https://m.kuaidi100.com/result.jsp?nu=' + readid
                realComp = comtext.get(ansj["com"], "其他") + "快递"
                output = '<?xml version="1.0"?>\n<rss version="2.0">\n<channel><title>' + realComp + ' ' + readid + '</title><link>' + url + '</link><description>一个快件跟踪RSS</description>'
                for i in range (1, maxnum+1):
                    ResultTime = result[i-1]["time"]
                    StrfTime = time.strftime("%m月%d日 %H:%M", time.strptime(ResultTime, "%Y-%m-%d %H:%M:%S"))
                    result[i-1]["time"] = StrfTime.replace(today, "今天").replace(yesterday, "昨天").replace(fronteday, "前天")
                    fTime = result[i-1]["time"]; fContent = result[i-1]["context"]
                    relpy()
                    fContent = fContent.replace(" 【", "【").replace("】 ", "】")
                    output = output + '<item><title>' + fTime + ' ' + fContent + '</title><link>' + url + '</link><description>' + fContent + '</description></item>'
                output = output + "</channel></rss>"
            else: #快递单号本身有误
                if ansj["status"] == "201":
                    passer = " 如果刚刚发出请不要取消并直接等待更新"
                else:
                    passer = ""
                relpy()
                output = blanker(readid, ansj["status"] + " " + ansj["message"] + passer)
        else: #无法识别公司
            relpy()
            output = blanker(readid, "无法识别单号对应快递公司")
    else:
        relpy()
        output = blanker("N/A", "快递单号输入错误")
    return output
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8080, debug=False)
