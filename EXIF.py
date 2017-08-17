from PIL import Image
import os #sudo pip install Pillow
def GetMiddleStr(content, startStr, endStr):
	try: startIndex = content.index(startStr)
	except ValueError: 
		startStr = 'xmp:CreatorTool="'; endStr = 'Macintosh'
		try: startIndex = content.index(startStr)
		except ValueError: return "none"
	if startIndex >= 0:
		startIndex += len(startStr)
	endIndex = content.index(endStr)
	return content[startIndex:endIndex]
for i in range(1, 714):
	rtl = "%03d" % i
	loc = "/Users/Junyi_Lou/Downloads/Apple/Retail/Pictures/R" + rtl + ".png"
	if os.path.isfile(loc):
		img = Image.open(loc)
		ans = GetMiddleStr(str(img.info), '<xmp:CreatorTool>', '</xmp:CreatorTool>').replace("(", "").replace(")", "").replace("Macintosh", "")
		if len(ans)!= 4 : print ans[:-1] + "	" + rtl