概要
===========
**其实主要是瞎搞，能拿出来供 Public 使用的不太多。请参阅 Repository 的 Wiki 了解部分代码的细节。**

Workflow & Siri Shortcuts
===========
Siri 查快递 20180922.shortcut - 使用 iOS 12 的捷径 (Shortcuts) App，设置 Siri 激活口令后，即可直接在 Siri 中以特定口令通过 Siri 查快递的捷径。**有关使用方法及更多内容，请参阅 [Wiki](https://github.com/junyilou/junyilou.github.io/wiki/Siri-%E6%9F%A5%E5%BF%AB%E9%80%92.shortcut) 中的使用说明。**

快递查询 20171105.wflow -  iOS App Workflow 快递查询工具，获[少数派](https://sspai.com)推荐。捷径 App 同样支持导入 wflow 文件并将自动转换为 shortcut 格式，本文件最后更新于 2017 年 11 月 5 日，更新记录见文章底部。

<img src ="/bkP/shortcut_1809.jpg" width="750px"/></div>

您也可以在下方查看上述两个 Workflow 的视频使用教程：

[![YouTube 教程](bkP/video_tet.png)](http://www.youtube.com/watch?v=30s_alJWIGo)

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

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/guopuzd) 直接体验本 Python 运行结果。**9to5Mac Apple Store 栏目编辑**也关注了果铺知道 Telegram Channel 获得最快推送。**更多内容详见 Repository 的 Wiki 页面。**

<img src ="/bkP/trt_1808.jpg" width="400px"/></div>

* [Today.py](Today.py)

基于 IFTTT 获取大中华 Apple Store 的 Today at Apple 新活动的工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/guopuzd) 直接体验本 Python 运行结果。这条 Python 会寻找所有大中华 Apple Store 开展的 [Today at Apple](https://apple.com/cn/today) 活动，基于活动名称发现新活动后将自动推送到 Telegram Channel。**更多内容详见 Repository 的 Wiki 页面。**

<img src ="/bkP/tgc_1808.jpg" width="400px"/></div>

* [Recruitment.py](Recruitment.py)

获取全球 Apple 招聘信息的工具。该工具将刷新全球 Specialist 的招聘店，并判断该店是否为已经在营业的零售店从而了解 Apple 未来招聘和开店计划。

<img src ="/bkP/recruitment_sgep.jpg" width="400px"/></div>

* [onlineCraw.py](onlineCraw.py)

该代码将刷新 Apple Online Store 页面，枚举 M _ _ _ 2 格式的 Apple 产品部件号，通过页面是否为 404 和已存储的产品部件号判断是否有新品开始发售，并推送通知至 IFTTT Maker。

<img src ="/bkP/onlineCraw_demo.jpg" width="400px"/></div>

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

[Apple_Jobs.py](/previous/Apple_Jobs.py) - 作用与 Recruitment.py 相似。2018 年 10 月 Apple Jobs 页面改版后，该 Python 已经无法使用，被 Recruitment.py 取代。

[Event_IFTTT.py](/previous/Event_IFTTT.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特别活动的推送工具，2017 年 5 月 17 日 Today at Apple 项目公布后，该 Python 已经无法使用，被 Today.py 替代。

[Base62_Pythonista.py](/previous/Base62_Pythonista.py) - 输入 Base62 的微博 ID 可自动转换为数字微博 ID，并生成微博国际版分享链接。适用于 iOS App Pythonista 的 Python 3 环境。

kuaidi20171031.wflow - 旧版本，对比 kuaidi20171105.wflow 新版增加了对总用时的计算，将自动判断是否签收，以确定是从最早的一条物流计算到查询时间，还是计算到最后一条物流时间。

kuaidi20170105.wflow - 旧版本，对比 kuaidi20171031.wflow 新版修复了「今天」「昨天」Relative 词语的使用问题。

kuaidi20161210.wflow - 旧版本，请访问 [Workflow 通知中心查快递 4](http://matrix.sspai.com/p/d384dd60) 了解。

联系
=======
Telegram: [俊逸 娄](http://t.me/marvin_lou "俊逸 娄")

Twitter 私信: [@赛艇的同学](https://twitter.com/junyi_lou "@赛艇的同学") 

新浪微博: [@赛艇的同学](https://weibo.com/3566216663 "@赛艇的同学")