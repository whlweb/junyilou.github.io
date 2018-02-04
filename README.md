文件介绍

其实主要是瞎搞，能拿出来供 Public 使用的不太多。我个人很喜欢 Kuaidi_IFTTT.py，另外 Today at Apple 和 Apple Jobs 则是为自己的公众号准备内容用的比较多。

Workflow
===========
kuaidi20171105.wflow -  iOS App Workflow 快递查询工具，支持剪切板，请访问 [Matrix 精选 | Workflow + 快递 100 原来快递既能这么查，还能这么显示](http://sspai.com/36871) 了解，本文件最后更新于 2017 年 11 月 5 日，更新记录见文章底部。

![截图](/bkP/wf_relative.png)

Python
===========
**请注意，自用 IFTTT Maker Key 在源代码中有明文保存，请不要恶意使用，[IFTTT Maker](https://maker.ifttt.com) 是 IFTTT 提供的服务。使用有关 IFTTT 的 Python 之前，请先将代码中 dJ4B3uIsxy 开头的 IFTTT Maker Key 改为你自己的 Key，有关申请方法，请参考[此处](https://sspai.com/post/39243)。**

[Kuaidi_IFTTT.py](Kuaidi_IFTTT.py) 基于 IFTTT Maker 的快递实时推送工具，运行该 Python 需要给予参数，在后面直接跟运单号码即可，如：
````bash
python Kuaidi_IFTTT.py 600316811932 199217929998
````
Python 会自动在 ~ 目录下创建以快递单号命名的 txt 文件。这个 txt 会保存快递公司代号、获取到的数目用于日后比对，以及最后一条物流信息的时间：这是为了避免某些快递公司会出现内容没有变化但是条数莫名其妙的变化。

![截图](/bkP/rtk.jpg)

快递公司识别使用的是快递 100 的服务，有极小的概率出错或者无法判断（出现 201 或 400 错误），可以手动输入快递公司代号（一般为全拼）并逗号空格。例如「jd, 」，这样就会强制让程序使用京东快递来查询。

[RetailID_IFTTT.py](RetailID_IFTTT.py) - 基于 IFTTT Maker 获取 Apple Store 图片更新工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/gpzdtg) 直接体验本 Python 运行结果。该项目会读取本地库中已经下载的 Apple 零售店图片并比较大小，刷新 Apple Store 的图片更新，可以让用户最快知道 Apple 更新了零售店图片的消息。由于它将枚举 001 至 730，根据网络环境不同，运行一次事件可能超过 20 分钟。

你还可以直接设置特别关注店号，刷新频率则从 6 小时变为 1 小时。利用该脚本，果铺知道较官网宣布和其他媒体发布消息早 3 小时收到图片更新，并预告韩国零售店 Garosugil 开幕消息。

![截图](/bkP/Garosugil_2018.png)

[Today_at_Apple.py](Today_at_Apple.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特邀嘉宾活动的推送工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/gpzdtg) 直接体验本 Python 运行结果。这条 Python 会寻找所有中国大陆 Apple Store 开展的 [Today at Apple](https://apple.com/cn/today) 活动，基于活动名称发现新活动后将自动推送到 Telegram Channel。需要有 Event.md 来保存已有的活动以判断是否为新活动。

![截图](/bkP/TaA_2018.png)

[Apple_Jobs.py](Apple_Jobs.py) - 获取中国大陆 Apple 招聘信息的工具，它将刷新本地下载的文件（可以用代码中的 down() 来下载），并判定远程 Apple 文件有无修改招聘信息。通过该工具可以了解 Apple 未来开店计划和招聘信息更新等。

[idc.py](idc.py) - 根据身份证前 17 位计算末尾校验码，返回样例「IDC: 11000019890604000 has recaptcha 1」

````bash
python idc.py 11000019890604000
````

Markdown
===========
[README.md](http://junyilou.github.io) - 本文件，访问 GitHub Pages 首页将重定向至此。

[name.md](name.md) - Apple 零售店编号和对应名称。

previous 文件夹
==========
[iReserve.py](/previous/iReserve.py) 自动获取指定型号，指定中国大陆零售店 iPhone X 手机的可预约购买情况，并在用户指定型号可预约购买（或不可预约购买，可设置仅在可预约购买时提醒）发送 IFTTT 通知至 iOS。该源代码将在下一代 iPhone 发布时重新使用。

![运行截图](/bkP/iPX_RCsc.png)

[Event_IFTTT.py](/previous/Event_IFTTT.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特别活动的推送工具，2017 年 5 月 17 日 Today at Apple 项目公布后，该 Python 已经无法使用，被 Today_IFTTT.py 替代。

![截图](/bkP/event.jpg)

[EXIF.py](/previous/EXIF.py) - 获取 Apple 零售店图片的处理软件（Adobe Photoshop）版本。

[format.py](format.py) - 通过 Python json.dumps 以显示 JSON 格式化结果，可一次性输出多个文件，将文件拖入终端即可。

````bash
python format.py ~/states.json
````

kuaidi20171031.wflow - 旧版本，对比 kuaidi20171105.wflow 新版增加了对总用时的计算，将自动判断是否签收，以确定是从最早的一条物流计算到查询时间，还是计算到最后一条物流时间。

kuaidi20170105.wflow - 旧版本，对比 kuaidi20171031.wflow 新版修复了「今天」「昨天」Relative 词语的使用问题。

kuaidi20161210.wflow - 旧版本，请访问 [Workflow 通知中心查快递 4](http://matrix.sspai.com/p/d384dd60) 了解。

rss-kuaidi.py - 通过 Pip Flask 结合 RSS 实现自动推送物流信息 请访问 [利用 Flask 和 VPS 搭建物流更新自动推送 RSS](http://matrix.sspai.com/p/da505de0) 了解。

联系
=======

少数派: [Junyi Lou](http://matrix.sspai.com/p/da7b1760 "Junyi Lou - Matrix")

新浪微博: [@Junyi_Lou_](https://weibo.com/n/Junyi_Lou_ "@Junyi_Lou_")