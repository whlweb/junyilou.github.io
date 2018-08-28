import os, sys
arg = 0
for m in sys.argv[1:]: arg += 1
for i in range(1, arg + 1):
	path = sys.argv[i]
	basename = os.path.basename(path)
	location = path.replace(basename, "")
	basename = basename.replace("png", "jpeg")
	os.system("sips -s format jpeg --out " + location + basename + " " + path)
	os.system("mv " + location + basename + " " + location + basename.replace("jpeg", "jpg"))
if (input("Do you want to remove the original file? ")):
	for i in range(1, arg + 1):
		os.system("rm " + path[i])
