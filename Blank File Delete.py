# -*- coding:utf-8 -*-
from __future__ import division
import os,sys
arg = 0
for m in sys.argv[1:]: arg = arg + 1
for i in range(1,arg+1):
	if (os.path.getsize(sys.argv[i])/1024) < 1:
		print "\n检测到极小文件", sys.argv[i]
		j = input()
		if j:
			os.system("".join(["rm ", sys.argv[i]]))