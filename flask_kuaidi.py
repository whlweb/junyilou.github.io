# -*- coding:utf-8 -*-
from __future__ import division
from flask import Flask, jsonify, request
import sys, json, urllib2, time
app = Flask(__name__)
#Flask needed. Created by Junyi_Lou
#未来思路:
#    参数: 最大条数 求min值 for循环最大数字
#    前天 昨天显示 参考 "http://www.iplaypython.com/sys/s100.html"
#    format 日期到 8月3日 18:23 格式
#本地处理的部分:
#    对于快递公司代号的翻译
#    对于已签收的bool值反馈
#    对于快件的备注显示
@app.route('/kuaidi/', methods=['GET'])  
def home():
    readid = request.args.get('id').__str__()
    if readid != "None":
        urla = ''.join(["https://www.kuaidi100.com/autonumber/autoComNum?text=", readid])
        comp = json.loads(urllib2.urlopen(urla).read())["auto"][0]["comCode"]
        urlb = ''.join(["https://www.kuaidi100.com/query?type=", comp, "&postid=", readid])
        responce = urllib2.urlopen(urlb)
        anst = responce.read(); ansj = json.loads(anst)
        if ansj["status"] == "200": #成功
            erstat = 1
            maxnum = anst.count("location")
            result = ansj["data"]
            tasks = list(range(maxnum+1))
            tasks [0] = {'signature': erstat, 'postid': ansj["nu"],'comp': ansj["com"],'timestamp': int(time.time())} 
            for i in range (1, maxnum+1): tasks [i] = {'time': result[i-1]["time"],'content':result[i-1]["context"]}
        else: #下载失败
            tasks = list(range(1))
            tasks [0] = {'signature': 0, 'content': ansj["message"]}
    else: #URL失败
        tasks = list(range(1))
        tasks [0] = {'signature': 0, 'content': r"URL没有指定单号"}
    return jsonify(tasks)
if __name__ == '__main__':  
    app.run()