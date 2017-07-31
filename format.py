import json, sys
from collections import OrderedDict
f = open(sys.argv[1]); fr = f.read(); f.close()
print json.dumps(json.loads(fr, object_pairs_hook = OrderedDict), ensure_ascii = False, indent = 2)