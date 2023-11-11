# AI-Digital-Human

鸽子：6 月下旬出教程，放代码。

先把用到的开源项目整理出来，**一键安装包、详细的教学** ，放到后面发布的视频里讲解。

**视频教程：**

第一期（vits语音合成，一键训练启动包）：

https://www.bilibili.com/video/BV1K94y1k7Bw/

第二期（特定场景GPT）：

https://www.bilibili.com/video/BV1Gw411T7fb

1、图像超分辨率重建

针对人脸修复效果较好的是 CodeFormer，“鲁迅”那期视频，就是使用该技术创建的虚拟人物。

https://github.com/sczhou/CodeFormer

2、大语言模型

大语言模型可以使用开源的 ChatGLM2-6B，官方也开源了 finetune 代码。

https://github.com/THUDM/ChatGLM2-6B

“鲁迅”那期视频所使用的模型为非开源的，所以这里可以使用 ChatGLM2-6B 代替，效果是一样的。

3、声音模型

将大语言模型生成的文本，转成音频，可以使用某个人的干声数据做训练，最好能有 1 个小时的数据，音频质量也要好，训练的效果不会差。

https://github.com/jaywalnut310/vits

4、画面驱动

最后就是使用大语言模型生成的文本转成的音频，驱动修复后的高清图片，可以使用的开源项目是 SadTalker。

https://github.com/OpenTalker/SadTalker

“鲁迅”那期视频使用的一个画面驱动算法是非开源的，所以这里用 SadTalker 进行了替代，效果可能会差一丢丢。

5、可视化交互页面

我互动的可视化页面，是使用 gradio 做的，填充框架的内容即可，这个相对简单。

https://github.com/gradio-app/gradio

第一期教学视频，正在做呢，还没做完，赶进度中...

对不住，鸽了一段时间，实在太忙。因为内容较多，涉及：图片生成/修复、大模型训练、语音合成、画面驱动。一期视频搞不定，我决定弄成系列的，更新速度经常打脸，我就努力继续更吧。
