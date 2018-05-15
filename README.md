概要
===========
**其实主要是瞎搞，能拿出来供 Public 使用的不太多。请参阅 Repository 的 Wiki 了解部分代码的细节。**

Workflow
===========
kuaidi20171105.wflow -  iOS App Workflow 快递查询工具，获[少数派](https://sspai.com)推荐。本文件最后更新于 2017 年 11 月 5 日，更新记录见文章底部。

<div align=center><img src ="/bkP/wf_relative_reb.png" /></div>

Pythonista
===========
iOS App [Pythonista 3](https://itunes.apple.com/cn/app/pythonista-3/id1085978097?mt=8) 为用户提供了在手机上运行 Python2 的可能。

当前主要计划将 Kuaidi.py 和 Weibo_Base62.py 优化：现有未完工的 Kuaidi_Pythonista.py 和已完成的 Weibo_Base62_Pythonista.py。未来计划优化 Today.py

[Kuaidi_Pythonista.py](Kuaidi_Pythonista.py) - 尚未完工，已优化代码输出结果，正设计 UI 将其展示在 iOS 系统的 Widget 页面中。代码请参照下文 [Kuaidi.py](Kuaidi.py)。

[Weibo_Base62_Pythonista.py](Weibo_Base62_Pythonista.py) - [Weibo_Base62.py](Weibo_Base62.py) 的 iOS 优化版本，复制完整的 weibo.com/userid/base62 链接，即可在 Today Widget 获取微博 ID 数字和国际版 fx.weibo.cc 链接，并将链接复制到剪切板。

<div align=center><img src ="/bkP/Pythonista_NJT.jpg" /></div>

Python
===========
**请注意，自用 IFTTT Maker Key 在源代码中有明文保存，请不要恶意使用，[IFTTT Maker](https://maker.ifttt.com) 是 IFTTT 提供的服务。使用有关 IFTTT 的 Python 之前，请先将代码中 bKwiDt 开头的 IFTTT Maker Key 改为你自己的 Key，有关申请方法，请参考[此处](https://sspai.com/post/39243)。**

[Kuaidi.py](Kuaidi.py) 基于 IFTTT 的快递实时推送工具，运行该 Python 需要给予参数，在后面直接跟运单号码即可，如：
````bash
python Kuaidi.py 600316811932 199217929998
````

可配合 nohup 或 screen 使用，需要将代码一直保持在前台。

<div align=center><img src="/bkP/rich_kuaidi_square.jpg" /></div>

<br>**更多内容详见 Repository 的 Wiki 页面。**

[Retail.py](Retail.py) - 基于 IFTTT 获取 Apple Store 图片更新工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/gpzdtg) 直接体验本 Python 运行结果。

利用该脚本，果铺知道较官网宣布和其他媒体发布消息早 3 小时收到图片更新，并预告韩国零售店 Garosugil 开幕消息，奥地利零售店 Kaerntner Strasse 则比主流媒体快了约 6 小时。

<div align=center><img src ="/bkP/Kaerntner_2018_reb.png" /></div>

**更多内容详见 Repository 的 Wiki 页面。**

[Today_at_Apple.py](Today_at_Apple.py) - 基于 IFTTT 获取中国 Apple Store Today at Apple 新活动的工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/gpzdtg) 直接体验本 Python 运行结果。这条 Python 会寻找所有中国大陆 Apple Store 开展的 [Today at Apple](https://apple.com/cn/today) 活动，基于活动名称发现新活动后将自动推送到 Telegram Channel。需要有 Event.md 来保存已有的活动以判断是否为新活动。

<div align=center><img src ="/bkP/TaA_2018_reb.png" /></div>

**更多内容详见 Repository 的 Wiki 页面。**

[Apple_Jobs.py](Apple_Jobs.py) - 获取中国大陆 Apple 招聘信息的工具，它将刷新本地下载的文件并判定远程 Apple 文件有无修改招聘信息。通过该工具可以了解 Apple 未来开店计划和招聘信息更新等。

[Weibo_Base62.py](Weibo_Base62.py) - 修改自[脚本之家](http://www.jb51.net/article/49353.htm)所展示的 Python 代码，利用 Python Flask，将微博 62 进制 URL 链接（示例：G56yQ4FFi）转换为 10 进制 Weibo ID 数字，并生成微博国际版（overseas.weibo.cc 和 fx.weibo.cc）分享链接。

挂载 Flask 环境后，只需访问 IP地址:8080/<62进制>，如 192.168.24.74:8080/G56yQ4FFi，即可获得 fx.weibo.cc 的微博国际版分享地址。

[idc.py](idc.py) - 根据身份证前 17 位计算末尾校验码，返回样例「IDC: 11000019890604000 has recaptcha 1」

````bash
python idc.py 11000019890604000
````

文本
===========
[README.md](http://junyilou.github.io) - 本文件，访问 GitHub Pages 首页将重定向至此。

[name.json](name.json) - Apple 零售店编号和对应名称。

previous 文件夹
==========
[iReserve.py](/previous/iReserve.py) 自动获取指定型号，指定中国大陆零售店 iPhone X 手机的可预约购买情况，并在用户指定型号可预约购买（或不可预约购买，可设置仅在可预约购买时提醒）发送 IFTTT 通知至 iOS。该源代码将在下一代 iPhone 发布时重新使用。

![运行截图](/bkP/iPX_RCsc.png)

[Event_IFTTT.py](/previous/Event_IFTTT.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特别活动的推送工具，2017 年 5 月 17 日 Today at Apple 项目公布后，该 Python 已经无法使用，被 Today_IFTTT.py 替代。

[EXIF.py](/previous/EXIF.py) - 获取 Apple 零售店图片的处理软件（Adobe Photoshop）版本。

[format.py](/previous/format.py) - 通过 Python json.dumps 以显示 JSON 格式化结果，可一次性输出多个文件，将文件拖入终端即可。

````bash
python format.py ~/states.json
````

[shrink.py](/previous/shrink.py) - 通过 TinyPNG 的 API 压缩图片并返回图片地址的源代码。曾尝试（没有 Commit 出来）用于 Today at Apple 和 Retail 两个文件中，但 Apple 的服务器自带了压缩功能，故代码闲置。

kuaidi20171031.wflow - 旧版本，对比 kuaidi20171105.wflow 新版增加了对总用时的计算，将自动判断是否签收，以确定是从最早的一条物流计算到查询时间，还是计算到最后一条物流时间。

kuaidi20170105.wflow - 旧版本，对比 kuaidi20171031.wflow 新版修复了「今天」「昨天」Relative 词语的使用问题。

kuaidi20161210.wflow - 旧版本，请访问 [Workflow 通知中心查快递 4](http://matrix.sspai.com/p/d384dd60) 了解。

rss-kuaidi.py - 通过 Pip Flask 结合 RSS 实现自动推送物流信息 请访问 [利用 Flask 和 VPS 搭建物流更新自动推送 RSS](http://matrix.sspai.com/p/da505de0) 了解。

联系
=======
Telegram: [俊逸 娄](http://t.me/marvin_lou "俊逸 娄")

Twitter 私信: [@赛艇的同学](https://twitter.com/junyi_lou "@赛艇的同学") 

新浪微博: [@赛艇的同学](https://weibo.com/3566216663 "@赛艇的同学")