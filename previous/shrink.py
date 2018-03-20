def tinyAPI(oURL):
	os.system('wget --no-check-certificate --auth-no-challenge ' + 
		'--http-user api --http-password QhVOEXYm9JMroorXDgPlbD_uz2Mzl_e9 ' +
		'--post-data ' + "'" + '{"source":{"url":"' + oURL + '"}'+ "}' " + 
		'--header Content-Type:application/json https://api.tinify.com/shrink')
	aOpen = open("shrink"); ajson = json.loads(aOpen.read()); aOpen.close()
	os.system("rm -f shrink")
	try: return ajson["output"]["url"]
	except KeyError: return oURL

tinyAPI("https://junyilou.github.io/bkP/c_ems.png")