import os, sys
arg = 0
for m in sys.argv[1:]: arg += 1
for i in range(1, arg + 1):
	path = sys.argv[i]
	basename = os.path.basename(path)
	location = path.replace(basename, "")
	basename = basename.replace("png", "jpg")
	os.system("sips -s format jpeg --out " + location + basename + " " + path)