客户端代码、服务端代码均已上传。

注意：这个小项目，想要学习 python 的小伙伴可以当作一个小项目尝试。

建议：想要学习编程 or 已经编程基础的人尝试。

需要学习：

1、Renpy 的使用，可以看这个视频快速入门：

https://www.bilibili.com/video/BV19y4y1e7UV/

看完后，你就知道项目里的 game 代码怎么用了。

2、bert vits2 也需要会部署，这个教程特别多，不过因为每个版本都不一样，而且还各有各的问题。

建议直接用最新代码，然后自己从头部署，自己训练音频模型。我不会分享任何训练好的音频模型哈，毕竟这个有风险。

想要学习的人，可以自己尝试训练。

Bert-VITS2 声音模型：
https://github.com/fishaudio/Bert-VITS2

原神音频数据集：
https://github.com/AI-Hobbyist/Genshin_Datasets

如果不着急也可以等我出一期教学视频。

3、代码分为后端和前端。

后端就是 hutao_server.py 都在这里，主要负责调度语音识别、语音翻译这些后端服务，处理前端（Renpy）发送过来的数据。需要学习 websocket 的使用。

如果你具备了以上基础，那么就可以尝试复现本项目了。

步骤：

1、python hutao_server.py 启动后端服务。

2、使用 Renpy 启动器运行游戏。

部署教程，文字稿已发，视频跪求三连！

https://www.bilibili.com/video/BV1tc411i7bq
