import json, sys
arg = 0
for m in sys.argv[1:]: arg += 1
f = open(sys.argv[1]); fr = f.read(); f.close()
print json.dumps(json.loads(fr), ensure_ascii = False, indent = 2)