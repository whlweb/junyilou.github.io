文件介绍

Workflow
===========
kuaidi[%2017日期].wflow -  iOS App Workflow 快递查询工具，支持剪切板，请访问 [Matrix 精选 | Workflow + 快递 100 原来快递既能这么查，还能这么显示](http://sspai.com/36871 "点击访问") 了解。 

./kuaidi-wflow/kuaidi[%2016日期].wflow - 旧版本。请访问 [Workflow 通知中心查快递 4](http://matrix.sspai.com/p/d384dd60 "点击访问") 了解。 

KuaidiUpdater - kuaidi[%2016日期].wflow 自动更新旗标文件。

Python
===========
kuaidi.py - Python 快递查询源代码 请访问 [可能是最小的跨平台查快递工具](http://matrix.sspai.com/p/d006b320 "点击访问") 了解，现在已经删除。

flask-kuaidi.py - rss-kuaidi.py 的前身，通过 Pip Flask 将物流输出为更美观的 JSON 形式。

rss-kuaidi.py - 通过 Pip Flask 结合 RSS 实现自动推送物流信息 请访问 [利用 Flask 和 VPS 搭建物流更新自动推送 RSS](http://matrix.sspai.com/p/da505de0 "点击访问") 了解

kuaidi_instapush.py 通过 Instapush 在任何 VPS 乃至本地开发板上直接实现 rss-kuaidi.py 的功能，尚未公布。

instapush_signal.py 通过信号 SIGUSR1, SIGUSR2, SIGCONT, SIGTERM 来实现在 kuaidi_instapush.py 运行途中直接增加新快递单，无需退出 Python 重新运行的源代码。

RetailID.py - 本地执行的 Apple 零售店图片快速下载和整理工具。

RetailID_Instapush.py - Apple 零售店图片快速下载和整理工具的 Instapush 版本。

Event_Instapush.py - 每天刷新中国大陆 Apple Store 零售店的特别活动，帮助你最快报名参加。

Markdown
===========
README.md - 本文件; name.md - Apple 零售店编号和对应名称

因习惯喜欢将纯文本保存为 Markdown 格式，可能实际上没有特别用途。

联系
=======
专注于 Workflow 和 Python 开发

Twitter: [@Junyi_Lou](https://twitter.com/Junyi_Lou "@Junyi_Lou") 

Sina Weibo: [@Junyi_Lou_](https://weibo.com/n/Junyi_Lou_ "@Junyi_Lou_")

Matrix: [Junyi Lou](http://matrix.sspai.com/p/da7b1760 "Junyi Lou - Matrix")
