import urllib.request, urllib.error, urllib.parse, json, clipboard, appex, ui

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
shareURL = "http://overseas.weico.cc/portal.php?a=get_share_url&ct=weibo&uid=3566216663&weibo_id="
clearURL = ""

def index(query):
	weiboID = int(url_to_mid(query))
	dURL = shareURL + str(weiboID)
	responce = urllib.request.urlopen(dURL)
	global clearURL
	clearURL = json.loads(responce.read())["data"]["url"][:38]
	return weiboID

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
	for i in range(int(size)):
		s = url[i * 4: (i + 1) * 4][::-1]
		s = str(base62_decode(str(s)))
		s_len = len(s)
		if i < size - 1 and s_len < 7: s = (7 - s_len) * '0' + s
		result.append(s)
	result.reverse()
	return result[0] + result[1] + result[2]

def toClipButton(a):
	global clearURL
	clipboard.set(clearURL)

def main(text):
	v = ui.View(frame=(0, 0, 320, 120))
	label = ui.Label(frame=(20, 0, 320 - 44 - 30, 120), flex='wh')
	label.name = 'text_label'
	label.font = ('Menlo', 13)
	label.number_of_lines = 0
	v.add_subview(label)
	clear_btn = ui.Button(frame=(320-44-10, 0, 44, 120), flex='hl')
	clear_btn.image = ui.Image.named('iow:clipboard_32')
	clear_btn.action = toClipButton
	v.add_subview(clear_btn)
	appex.set_widget_view(v)
	label.text = 'Base 62: ' + text + "\n数字 ID: " + str(index(text)) +"\n微博国际版 URL: " + clearURL

clip = clipboard.get()
if "weibo.com" in clip:
	main(clip.replace(clip[:-9], ""))
else:
	label = ui.Label(font=('Menlo', 14), alignment=ui.ALIGN_CENTER)
	label.text = '当前没有复制微博链接'
	appex.set_widget_view(label)
