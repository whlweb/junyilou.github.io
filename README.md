文件介绍

Workflow
===========
kuaidi20170105.wflow -  iOS App Workflow 快递查询工具，支持剪切板，请访问 [Matrix 精选 | Workflow + 快递 100 原来快递既能这么查，还能这么显示](http://sspai.com/36871) 了解。

![截图](/bkP/workflow.jpg)

Python
===========
**请注意，私人 IFTTT Maker Key 在源代码中有明文保存，请不要恶意使用，[IFTTT Maker](https://maker.ifttt.com) 是 IFTTT 提供的服务。使用有关 IFTTT 的 Python 之前，请先将代码中 dJ4B3uIsxy 开头的 IFTTT Maker Key 改为你自己的 Key，有关申请方法，请参考[此处](https://sspai.com/post/39243)。**

[Kuaidi_IFTTT.py](Kuaidi_IFTTT.py) 基于 IFTTT Maker 的快递实时推送工具，运行该 Python 需要给予参数，在后面直接跟运单号码即可，如：
````bash
python Kuaidi_IFTTT.py 600316811932 199217929998
````
Python 会自动在 ~ 目录下创建以快递单号命名的 txt 文件，并保存从快递 100 获取到的物流条数和最后一条的时间。通过物流条数确定是否有更新，由于快递 100 的 bug，申通和圆通快递单可能出现物流条数无理由增加，但物流信息并为更新的情况，第三个参数用于解决此问题，判定物流信息是否真的有更新。

![截图](/bkP/rtk.jpg)

由于快递 100 自动计算的公司出错概率仍然存在（较小），你可以手动在 ~ 创建以快递单号命名的 txt 文件，并写入 "[公司代号(一般为全拼)], " 保存，就可以自定义公司名，常用公司代号在 py 文件中有写。

![截图](/bkP/nano.png)

[IFTTT_Signal.py](IFTTT_Signal.py) 通过 signal 向 [Kuaidi_IFTTT.py](Kuaidi_IFTTT.py) 增添快递单的工具。

该文件将读取 ~/pid.txt 下的进程编号，运行 [Kuaidi_IFTTT.py](Kuaidi_IFTTT.py) 时该文件会自动创建，并通过 Linux 信号 SIGUSR1 和 SIGUSR2 传递二进制信号，首先将快递单号转换为二进制。并发送信号交由运行中的 Python 分析。这将使 0 字头的快递单号失效，但现实中使用 0 字快递单的只有顺丰快捷下单服务，你可以重新运行 Kuaidi_IFTTT.py 并在参数中添加。

![截图](/bkP/signal.png)

如果没有 ~/pid.txt，它将自动用 screen 创建一个名为 jdk 的新窗体并运行 Kuaidi_IFTTT.py，这将使得你只需要运行这条 Python 它将自动判断是向已有进程添加，还是创建新进程。

[RetailID.py](RetailID.py) - 用于本地库执行的 Apple 零售店图片快速下载和整理工具，这一文件仅供在个人电脑执行，需要超过 2GB 的本地文件支持，对 GitHub 用户该文件仅供参考代码。

[RetailID_IFTTT.py](RetailID_IFTTT.py) - 基于 IFTTT Maker 的 Apple Store 零售店图片更新推送工具。该项目会读取本地库中已经下载的 Apple 零售店图片并比较大小，刷新 Apple Store 的图片更新，可以让用户最快知道 Apple 更新了零售店图片的消息。

![截图](/bkP/retailid.jpg)

使用时在后面接 Retail 编号（在 [name.md](name.md) 可以找到），如：
````bash
python RetailID_IFTTT.py 713
````

由于 request 库无法较好的管理超时问题，为避免后台运行卡死，枚举店号现已被注释。虽然说它实在方便，为了减轻负担，目前将 Time interval 设置为了 2h，这也造成了一些媒体跑的比香港记者还快。

![截图](/bkP/hkjournal.png)

全新 [Today_at_Apple.py](Today_at_Apple.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特邀嘉宾活动的推送工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/ars_teller) 直接体验本 Python 运行结果。这条 Python 会寻找所有中国大陆 Apple Store 开展的 [Today at Apple](https://apple.com/cn/today) 活动，基于活动名称发现新活动后将自动推送到 Telegram Channel。需要有 Event.md 来保存已有的活动以判断是否为新活动。

![截图](/bkP/NewTaa.jpg)

[Apple_Jobs.py](Apple_Jobs.py) - 获取中国大陆 Apple 招聘信息的工具，它将刷新本地下载的文件（可以用代码中的 down() 来下载），并判定远程 Apple 文件有无修改招聘信息。通过该工具可以了解 Apple 未来开店计划和招聘信息更新等。

[format.py](format.py) - 通过 Python json.dumps 以显示 JSON 格式化结果，可一次性输出多个文件，将文件拖入终端即可。

[EXIF.py](EXIF.py) - 通过 PIL 来获取图片生成软件（例如 Adobe Photoshop CS 2017 (Macintosh)）。

Markdown
===========
[README.md](http://junyilou.github.io) - 本文件，访问 GitHub Pages 首页将重定向至此。

[name.md](name.md) - Apple 零售店编号和对应名称。

[future.md](future.md) - Apple 零售店计划表。

[states.json](states.json) - Apple 官网招聘页面的中国省份列表。

previous 文件夹
==========
[Event_IFTTT.py](Event_IFTTT.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特别活动的推送工具，2017 年 5 月 17 日 Today at Apple 项目公布后，该 Python 已经无法使用，被 Today_IFTTT.py 替代。

![截图](/bkP/event.jpg)

kuaidi20161210.wflow - 旧版本，请访问 [Workflow 通知中心查快递 4](http://matrix.sspai.com/p/d384dd60) 了解。

KuaidiUpdater - 上述文件的自动更新旗标文件。

kuaidi.py - Python 快递查询源代码，请访问 [可能是最小的跨平台查快递工具](http://matrix.sspai.com/p/d006b320 ) 了解，已经删除。

flask-kuaidi.py - rss-kuaidi.py 的前身，通过 Pip Flask 将物流输出为更美观的 JSON 形式。

rss-kuaidi.py - 通过 Pip Flask 结合 RSS 实现自动推送物流信息 请访问 [利用 Flask 和 VPS 搭建物流更新自动推送 RSS](http://matrix.sspai.com/p/da505de0) 了解。

联系
=======
专注于 Workflow 和 Python 开发

Twitter: [@Junyi_Lou](https://twitter.com/Junyi_Lou "@Junyi_Lou") 

Sina Weibo: [@Junyi_Lou_](https://weibo.com/n/Junyi_Lou_ "@Junyi_Lou_")

少数派 Matrix: [Junyi Lou](http://matrix.sspai.com/p/da7b1760 "Junyi Lou - Matrix")