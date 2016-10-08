import os
print "Input workflow.is code."
code = raw_input()
print "Input version number."
ver = input()
fc = open("/Users/Junyi_Lou/junyilou.github.io/kuaidi.html", "w")
html = "".join(["<head><meta http-equiv=",'"',"refresh",'"'," content=",'"',"0;url=https://workflow.is/workflows/",code,".wflow",'"',"/></head><body></body>"])
fc.write(html)
fc.close()
os.system ("".join(["wget -t 3 -c -O /Users/Junyi_Lou/junyilou.github.io/Kuaidi", str(ver), ".wflow https://workflow.is/workflows/", code, ".wflow"]))