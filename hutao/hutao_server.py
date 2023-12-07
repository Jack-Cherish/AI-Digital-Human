#-*- coding:utf-8 -*-
from llm import get_answer
from urllib.request import urlretrieve
from config import vits_predict, vist_host, samplerate
import requests
from pydub import AudioSegment
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import sys

# Socket
import socket
ip_port = ('127.0.0.1', 9000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
s.bind(ip_port)
s.listen(5)

# Voice Recognition
q = queue.Queue()
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def voice_input():
    model = Model(lang="cn")
    print("You:")
    with sd.RawInputStream(samplerate = samplerate, blocksize = 8000, device = sd.default.device,
                           dtype="int16", channels=1, callback=callback):

        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                a = json.loads(rec.Result())
                a = str(a['text'])
                a = ''.join(a.split())
                if(len(a) > 0):
                    user_input = a
                    stop_flag = 1
                    return user_input

def generate_sound(input_str):
    playload = {
        "fn_index":0,
        "data":[
            input_str,
            "hutao_zh",
            0.2,
            0.6,
            0.8,
            1,
            "ZH"
            ]
        }
    playload = json.dumps(playload)
    resp = requests.post(vits_predict, data = playload)
    resp = json.loads(resp.text)
    if resp["data"][0] == "Success":
        fname = resp["data"][1]["name"]
        file_url = vist_host + "file=" + fname
        save_fname = "output.wav"
        urlretrieve(url = file_url, filename = save_fname)        

if __name__ == "__main__":

    print("Sockets server runing!")
    client, client_addr = s.accept()

    total_data = bytes()

    inputMethod = int(client.recv(1024).decode())
    # Keyboard
    if inputMethod == 0:
        print("键盘输入")
    elif inputMethod == 1:
        print("语音输入")

    while True:
        if inputMethod == 0:
            total_data = bytes()
            while True:
                data = client.recv(1024)
                total_data += data
                if len(data) < 1024:
                    break
            question = total_data.decode()

        elif inputMethod == 1:
            question = voice_input()
            client.send(question.encode())

        print("接受到的提问: " + question)
        answer = get_answer(question)
        
        generate_sound(answer)
        
        # convert wav to ogg
        src = "./output.wav"
        dst = "G:/renpy_wife/girlfriend_hutao/game/audio/test.ogg"
        sound = AudioSegment.from_wav(src)
        sound.export(dst, format="ogg")
        # send response to UI
        # print(answer.encode())
        client.send(answer.encode())
        # finish playing audio
        print(client.recv(1024).decode())