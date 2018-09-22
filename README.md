概要
===========
**其实主要是瞎搞，能拿出来供 Public 使用的不太多。请参阅 Repository 的 Wiki 了解部分代码的细节。**

Workflow & Siri Shortcuts
===========
Siri 查快递 20180922.shortcut - 使用 iOS 12 的捷径 (Shortcuts) App，设置 Siri 激活口令后，即可直接在 Siri 中以特定口令通过 Siri 查快递的捷径。**有关使用方法及更多内容，请参阅 [Wiki](https://github.com/junyilou/junyilou.github.io/wiki/Siri-%E6%9F%A5%E5%BF%AB%E9%80%92.shortcut) 中的使用说明。**

快递查询 20171105.wflow -  iOS App Workflow 快递查询工具，获[少数派](https://sspai.com)推荐。捷径 App 同样支持导入 wflow 文件并将自动转换为 shortcut 格式，本文件最后更新于 2017 年 11 月 5 日，更新记录见文章底部。

<img src ="/bkP/shortcut_1809.jpg" width="750px"/></div>

Python
===========
**使用有关 IFTTT 的 Python 之前，需要提供 IFTTT Maker Key，有关申请方法，请参考[此处](https://sspai.com/post/39243)。将仅有 Key 的文本文档命名为 key.txt 放在 ~ 目录 (即用户目录) 下即可。**

* [Kuaidi.py](Kuaidi.py)

基于 IFTTT 的快递实时推送工具，运行该 Python 需要给予参数，在后面直接跟运单号码即可。可配合 nohup 或 screen 使用，需要将代码一直保持在前台。**更多内容详见 Repository 的 Wiki 页面。**

````bash
python Kuaidi.py 600316811932 199217929998
````

<img src="/bkP/kuaidi_1808.jpg" width="400px"/></div>

* [Retail.py](Retail.py)

基于 IFTTT 获取 Apple Store 图片更新工具。

<img src ="/bkP/rtl_1808.jpg" width="400px"/></div>

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/gpzdtg) 直接体验本 Python 运行结果。**9to5Mac Apple Store 栏目编辑**也关注了果铺知道 Telegram Channel 获得最快推送。**更多内容详见 Repository 的 Wiki 页面。**

<img src ="/bkP/trt_1808.jpg" width="400px"/></div>

* [Today.py](Today.py)

基于 IFTTT 获取大中华 Apple Store 的 Today at Apple 新活动的工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/gpzdtg) 直接体验本 Python 运行结果。这条 Python 会寻找所有大中华 Apple Store 开展的 [Today at Apple](https://apple.com/cn/today) 活动，基于活动名称发现新活动后将自动推送到 Telegram Channel。**更多内容详见 Repository 的 Wiki 页面。**

<img src ="/bkP/tgc_1808.jpg" width="400px"/></div>

* [m3u8.py](m3u8.py)

这是一个秘密项目，用来解析某视频网站的 m3u8 列表并下载合并为 mp4 文件。

文本
===========
[README.md](http://junyilou.github.io) - 本文件，访问 GitHub Pages 首页将重定向至此。

[name.json](name.json) - Apple 零售店编号和对应名称。

[storeList.json](storeList.json) - 经格式化的 Apple Store app 零售店信息文件，包括零售店号、地址等各类信息。用于 Retail.py 对比以确认是否更改。

previous 文件夹
==========
[pngConvert.py](/previous/pngConvert.py) - macOS 下批量转换 png 为 jpg 格式文件。

[idc.py](/previous/idc.py) - 根据身份证前 17 位计算末尾校验码，返回样例「IDC: 11000019890604000 has recaptcha 1」

````bash
python idc.py 11000019890604000
````

[Apple_Jobs.py](/previous/Apple_Jobs.py) - 获取中国大陆 Apple 招聘信息的工具，它将刷新本地下载的文件并判定远程 Apple 文件有无修改招聘信息。通过该工具可以了解 Apple 未来开店计划和招聘信息更新等。

[iReserve.py](/previous/iReserve.py) 自动获取指定型号，指定中国大陆零售店 iPhone X 手机的可预约购买情况，并在用户指定型号可预约购买（或不可预约购买，可设置仅在可预约购买时提醒）发送 IFTTT 通知至 iOS。该源代码将在下一代 iPhone 发布时重新使用。

[Event_IFTTT.py](/previous/Event_IFTTT.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特别活动的推送工具，2017 年 5 月 17 日 Today at Apple 项目公布后，该 Python 已经无法使用，被 Today_IFTTT.py 替代。

[EXIF.py](/previous/EXIF.py) - 获取 Apple 零售店图片的处理软件（Adobe Photoshop）版本。

[shrink.py](/previous/shrink.py) - 通过 TinyPNG 的 API 压缩图片并返回图片地址的源代码。曾尝试（没有 Commit 出来）用于 Today at Apple 和 Retail 两个文件中，但 Apple 的服务器自带了压缩功能，故代码闲置。

[Base62_Pythonista.py](/previous/Base62_Pythonista.py) - 输入 Base62 的微博 ID 可自动转换为数字微博 ID，并生成微博国际版分享链接。适用于 iOS App Pythonista 的 Python 3 环境。

kuaidi20171031.wflow - 旧版本，对比 kuaidi20171105.wflow 新版增加了对总用时的计算，将自动判断是否签收，以确定是从最早的一条物流计算到查询时间，还是计算到最后一条物流时间。

kuaidi20170105.wflow - 旧版本，对比 kuaidi20171031.wflow 新版修复了「今天」「昨天」Relative 词语的使用问题。

kuaidi20161210.wflow - 旧版本，请访问 [Workflow 通知中心查快递 4](http://matrix.sspai.com/p/d384dd60) 了解。

rss-kuaidi.py - 通过 Pip Flask 结合 RSS 实现自动推送物流信息 请访问 [利用 Flask 和 VPS 搭建物流更新自动推送 RSS](http://matrix.sspai.com/p/da505de0) 了解。

联系
=======
Telegram: [俊逸 娄](http://t.me/marvin_lou "俊逸 娄")

Twitter 私信: [@赛艇的同学](https://twitter.com/junyi_lou "@赛艇的同学") 

新浪微博: [@赛艇的同学](https://weibo.com/3566216663 "@赛艇的同学")