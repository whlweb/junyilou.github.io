import os
from instapush import Instapush, App
AppID = "58fcc453a4c48a7623de6e9c"; AppSecret = "bfd223832711a220f2c7e25c93cd77f5"

app = App(appid = AppID, secret = AppSecret)
app.notify(event_name = 'raw', trackers = {'ans': 'It works in pypi!'})

a='curl -X POST -H "x-instapush-appid: '; b='" -H "x-instapush-appsecret: '
c='" -H "Content-Type: application/json" -d '; d="'"
e='{"event":"raw","trackers":{"ans":"'; f='It works in curl!'
g='"'; m='}'; n='}'; o="'"; p=' https://api.instapush.im/v1/post'
finalOut = a + AppID + b + AppSecret + c + d + e + f + g + m + n + o + p; os.system(finalOut)

print

# GitHub users please notice: AppSecret only uses for private.