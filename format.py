import json, sys
from collections import OrderedDict
arg = 0
for m in sys.argv[1:]: arg += 1
f = open(sys.argv[1]); fr = f.read(); f.close()
print json.dumps(json.loads(fr, object_pairs_hook = OrderedDict), ensure_ascii = False, indent = 2)