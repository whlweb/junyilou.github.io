import urllib2, json
from flask import Flask, request

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
shareURL = "http://overseas.weico.cc/portal.php?a=get_share_url&ct=weibo&uid=3566216663&weibo_id="

app = Flask(__name__)
@app.route('/<query>')
def index(query):
	dURL = shareURL + url_to_mid(query)
	responce = urllib2.urlopen(dURL)
	fOpen = open("log.log"); fRead = fOpen.read(); fOpen.close()
	fReopen = open("log.log", "w"); clearURL = json.loads(responce.read())["data"]["url"][:38]
	fWrite = fReopen.write(fRead + query + " " + clearURL +"\n"); fReopen.close()
	return clearURL

def base62_encode(num):
	arr = []; base = 62
	while num:
		rem = num % base
		num = num // base
		arr.append(alphabet[rem])
	arr.reverse()
	return arr

def base62_decode(string):
	base = 62; strlen = len(string)
	num = 0; idx = 0
	for char in string:
		power = (strlen - (idx + 1))
		num += alphabet.index(char) * (base ** power)
		idx += 1
	return num

def url_to_mid(url):
	url = str(url)[::-1]
	size = len(url) / 4 if len(url) % 4 == 0 else len(url) / 4 + 1
	result = []
	for i in range(size):
		s = url[i * 4: (i + 1) * 4][::-1]
		s = str(base62_decode(str(s)))
		s_len = len(s)
		if i < size - 1 and s_len < 7: s = (7 - s_len) * '0' + s
		result.append(s)
	result.reverse()
	return result[0] + result[1] + result[2]

def mid_to_url(midint):
	midint = str(midint)[::-1]
	size = len(midint) / 7 if len(midint) % 7 == 0 else len(midint) / 7 + 1
	result = []; rgA = rgB = ""
	for i in range(size):
		s = midint[i * 7: (i + 1) * 7][::-1]
		s = base62_encode(int(s))
		s_len = len(s)
		if i < size - 1 and len(s) < 4: s = '0' * (4 - s_len) + s
		result.append(s)
	result.reverse()
	for i in range(0, 4): rgA += result[1][i]; rgB += result[2][i]
	return str(result[0][0]) + rgA + rgB

app.run(host = "0.0.0.0", port = 8080)