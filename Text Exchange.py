# -*- coding:utf-8 -*-
import os, sys
os.system("clear")
print "输入需要替换为空的文本"
exc = raw_input()
arg = 0
for m in sys.argv[1:]: arg = arg + 1
for j in range(1, arg + 1): os.system(''.join(["mv -n ", '"', sys.argv[j], '" "', sys.argv[j].replace(exc, ""), '"']))