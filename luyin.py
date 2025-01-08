#######################################################
#功能：录音并保存到远程共享盘
#环境：python3.6+pyaudio+shutil
#作者：李鹏超
#日期：2025-01-02
#######################################################
import pyaudio
import wave
from smbprotocol.connection import Connection
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect
import os
import shutil
from datetime import datetime
import random


# 录音参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 0
WAVE_OUTPUT_FILENAME = ""

# 远程共享盘参数
# 注意：远程共享盘的路径末尾不要带斜杠
# 例如：远程共享盘路径为：\\10.70.1.123\xjzx\luyin，则REMOTE_PATH为/xjzx/luyin
# 注意：远程共享盘的用户名和密码需要在远程共享盘服务器上设置
REMOTE_SERVER = "10.1.6.62" #"WIN-26TQF9OFS1Q" #"10.1.6.62"
REMOTE_SHARE = "Luyin"
REMOTE_USER = "WIN-26TQF9OFS1Q" #"Administrator"
REMOTE_PASSWORD = "Admin123"
REMOTE_PATH = "/Luyin"

def create_file_name():
    # 获取当前时间
    now = datetime.now()
    # 将时间格式化为字符串
    time_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    random_num = random.randint(1000, 9999)
    file_name = f"{time_str}_{random_num}.wav"
    # 定义文件名
    #file_name = f"{time_str}.wav"
    return file_name

def create_time():
    # 获取分钟数
    try:
        minutes = float(input("请输入分钟数: "))
        seconds = minutes * 60
        print(f"{minutes} 分钟等于 {seconds} 秒。")
        return seconds
    except ValueError:
        print("输入无效，请输入一个有效的数字。")
        return 0

def record_audio():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录制")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* Done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("录制结束")


def save_to_remote():

    print(f"开始保存：{REMOTE_SERVER}")
    conn = Connection(REMOTE_SERVER,445)  
    #conn.login(REMOTE_USER, REMOTE_PASSWORD)
    print({conn})
    # 连接远程共享盘
    try:
        conn.connect()
        print({conn.connect()})
        session = Session(conn)
        print(session)
        session.connect()
        tree = TreeConnect(session, REMOTE_SHARE)
        print(tree)
        with open(WAVE_OUTPUT_FILENAME, 'rb') as local_file:
            remote_path = os.path.join(REMOTE_PATH, WAVE_OUTPUT_FILENAME)
            with tree.open(remote_path, desired_access=0x12019f, share_access=0x01, create_disposition=1) as remote_file:
                remote_file.write(local_file.read())

        tree.disconnect()
        session.disconnect()
        conn.disconnect()
    except Exception as e:
        print(f"连接或操作过程中出现错误: {e}")
        print("保存远程失败")

def save_to_bendishi():
    print("保存本地开始")
    shutil.copy(WAVE_OUTPUT_FILENAME, "Z:\luyin") 
    shutil.copy(WAVE_OUTPUT_FILENAME, "D:\luyin") 
    print("保存本地结束")

if __name__ == "__main__":
    WAVE_OUTPUT_FILENAME = create_file_name()
    RECORD_SECONDS = create_time()
    print(f"开始录音：文件名：{WAVE_OUTPUT_FILENAME} 录制时间：{RECORD_SECONDS} 秒")
    record_audio()
    save_to_bendishi()
    #save_to_remote()
    #if os.path.exists(WAVE_OUTPUT_FILENAME):
        #os.remove(WAVE_OUTPUT_FILENAME)
