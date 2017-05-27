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

[RetailID_IFTTT.py](RetailID_IFTTT.py) - 基于 IFTTT Maker 的 Apple Store 零售店图片更新推送工具。该项目用于自动刷新 Apple Store 的图片更新，可以让用户最快知道 Apple 更新了零售店图片的消息。

运行本文件需要在 ~/Retail/ 下有一个 List.md，可以为空，在内部填写 Apple Retail 代号（在 [name.md](name.md) 可以查看）并以无空格逗号分隔，如 669,559。运行时将自动读取该文件，如果刷新到的图片超过一定大小，Python 认为 Apple 已经最终确定该零售店图片，并自动将 List.md 中的对应店号删去。

![截图](/bkP/retailid.jpg)

[Event_IFTTT.py](Event_IFTTT.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特别活动的推送工具，2017 年 5 月 17 日 Today at Apple 项目公布后，该 Python 已经无法使用，被 Today_IFTTT.py 替代，请参阅下一段。

![截图](/bkP/event.jpg)

[Today_IFTTT.py](Today_IFTTT.py) - 基于 IFTTT Maker 获取中国 Apple Store 零售店特邀嘉宾活动的推送工具。

你可以在 Telegram Follow [果铺知道 Channel](https://t.me/ars_teller) 直接体验本 Python 运行结果。这条 Python 可以帮助你找到中国 Apple Store Today at Apple 项目的活动信息，只会输出有 Apple 特邀嘉宾的活动，例如 与卢根一起行摄重庆 此类艺术家活动。它需要在 ~/Retail/ 下有一个文件 Event.md ，可以为空，用来记录 ID 以便确定每次检查到的新活动是不是已经推送过。

![截图](/bkP/taa.jpg)

Markdown
===========
[README.md](http://junyilou.github.io) - 本文件，访问 GitHub Pages 将重定向至此。

[name.md](name.md) - Apple 零售店编号和对应名称。

[future.md](future.md) - Apple 零售店未来计划。

[url.md](url.md) - 这是 [Today_IFTTT.py](Today_IFTTT.py) 依赖的下载文件列表，Apple 在存储零售店活动信息时，即使文件不同，但每个城市所有零售店使用文件的内容完全一致。如中国重庆有三家零售店，Apple 解放碑和 Apple 重庆北城天街使用的文件分别为 [https://www.apple.com/cn/.../jiefangbei.json](https://www.apple.com/cn/today/static/data/store/jiefangbei.json) 和 [https://www.apple.com/cn/.../paradisewalkchongqing.json](https://www.apple.com/cn/today/static/data/store/paradisewalkchongqing.json) 但实则完全相同，本列表选择了所有有 Apple Store 城市中的其中一架店作为下载文件。

previous 文件夹
==========
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