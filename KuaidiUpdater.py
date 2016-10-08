import os
print "Input workflow.is code."
code = raw_input()
print "Input version number."
ver = input()
os.system ("".join(["wget -t 3 -c -O /Users/Junyi_Lou/junyilou.github.io/Kuaidi", str(ver), ".wflow https://workflow.is/workflows/", code, ".wflow"]))