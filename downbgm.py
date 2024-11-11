import requests
import re
import json
import os
from tkinter import messagebox



def download_bgm(url, name, file_name, save_path):
    response = requests.get(url)
    if "mp3" not in name and "wav" not in name and "m4a" not in name and "flac" not in name:
        if "mp3" or "MP3" in url:
            name = name + ".mp3"
        elif "wav" or "WAV" in url:
            name = name + ".wav"
        elif "m4a" or "M4A" in url:
            name = name + ".m4a"
        elif "flac" or "FLAC" in url:
            name = name + ".flac"
            
    path = os.path.normpath(save_path + "\\" + file_name + "_" + name)
    
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)
            
    else:
        messagebox.showinfo("失败", "{name}下载失败")

        

def parse_bgm(html_content, file_name, save_path):
    # 查找并下载bgm
    if '"bgm":[]' in html_content:
        messagebox.showinfo("失败", "这个剧本没有BGM哦~")
    else:
        pattern = re.compile(r'"bgm":.*?"}]', re.S)
        result = pattern.search(html_content)
        temp = result.group().replace("\"bgm\":", "")
        data = json.loads(temp)
        for i in data:
            download_bgm(i['url'], i['name'], file_name, save_path)
        messagebox.showinfo("成功", "BGM下载完成")
