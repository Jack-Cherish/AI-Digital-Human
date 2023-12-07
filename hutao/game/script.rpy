# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("胡桃")
define y = Character("你")
define config.gl2 = True
# define config.developer = True

image hutao = Live2D("Resources/hutao vtuber", base=.6, loop = True, fade=True)
image bg = "images/background_4.png"

init python:
    import socket
    import time
    thinking = 0
    total_data = bytes()
    renpy.block_rollback()
    ip_port = ('127.0.0.1', 9000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(ip_port)

# 游戏在此开始。

label start:
    $ renpy.block_rollback()
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show hutao talking
    show hutao talking
    voice "/audio/hello.ogg"
    e "嘿 你好 我是往生堂第七十七代堂主胡桃 你是我的客户吗"
    voice sustain

    # 此处显示各行对话。

    jump inputMethod

    # 此处为游戏结尾。

    return


label inputMethod:
    $ renpy.block_rollback()
    show hutao m01
    menu inputMethod1: #input 1
        e "请选择输入方式"
        "键盘输入":
            python:
                client.send(("0").encode())
                keyboard = True
            jump talk_keyboard
        "语音输入":
            python:
                client.send(("1").encode())
                keyboard = False
            jump talk_voice


label talk_keyboard:
    $ renpy.block_rollback()
    show hutao m02
    python:
        message = renpy.input("你：")
        client.send(message.encode())
        data = bytes()
    jump checkRes

label talk_voice:
    $ renpy.block_rollback()
    if(thinking == 0):
        show hutao m02
    y "请说话："
    python:
        client.setblocking(0)
        try:
                finishInput = client.recv(1024)
        except:
                finishInput = bytes()
                client.setblocking(1)

    if(len(finishInput) > 0):
        $ finishInput = finishInput.decode()
        $ renpy.block_rollback()
        y "[finishInput]"
        $ thinking = 0
        jump checkRes
    $ thinking = 1
    jump talk_voice

label checkRes:
    $ renpy.block_rollback()
    if(thinking == 0):
        show hutao m03
    e "思考中..."

    python:
        client.setblocking(0)
        try:
            data = client.recv(1024)
            total_data += data
        except:
            data = bytes()
            client.setblocking(1)

    if(len(data) > 0 and len(data) < 1024):
        python:
            response = total_data.decode()
            total_data = bytes()
            thinking = 0
        jump answer
    else:
        $ renpy.block_rollback()
        e "思考中......"
        $ thinking = 1
        jump checkRes

label answer:
    show hutao talking
    voice "/audio/test.ogg"
    $ renpy.block_rollback()
    e "[response]"
    voice sustain
    show hutao m02
    if keyboard:
        $ client.send("语音播放完毕".encode())
        jump talk_keyboard
    else:
        $ client.send("语音播放完毕".encode())
        jump talk_voice