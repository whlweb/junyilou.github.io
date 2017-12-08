import json, sys, os
from collections import OrderedDict
arg = 0
for m in sys.argv[1:]: arg += 1
for i in range(1, arg + 1):
	f = open(sys.argv[i]); fr = f.read(); f.close()
	print "\n# "  + os.path.basename(sys.argv[i]) + " #\n" + json.dumps(json.loads(fr, object_pairs_hook = OrderedDict), ensure_ascii = False, indent = 2)