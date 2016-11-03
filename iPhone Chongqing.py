# -*- coding:utf-8 -*-
import urllib2,urllib,os; equa = ["R480", "R476","R573"]; eqn = 3
for p in range(0, eqn): 
	k = urllib2.urlopen(urllib2.Request("http://ir.weip.tech/Home/GetStoreiPhoneList",urllib.urlencode({'storecode':equa[p],'regioncode':'CN','onlyshowavailability':'true'}))).read()
	print k; p += 1