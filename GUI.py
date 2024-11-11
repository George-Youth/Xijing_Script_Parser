from fetch_script import fetch_script
from parse_script import parse_script
from downbgm import parse_bgm

import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel
import os
import threading



def on_choose_path(entry_path):
    # 选择文件保存路径
    path = filedialog.askdirectory()  # 选择目录而不是文件
    if path:
        entry_path.delete(0, tk.END)  # 清空当前路径
        entry_path.insert(0, path)  # 插入选择的路径
    return entry_path



def on_confirm(root, entry_id, entry_path, entry_file_name, bgm_confirm):
    # 此处添加确认下载逻辑
    script_id = entry_id.get().strip()
    save_path = os.path.normpath(entry_path.get().strip())
    file_name = entry_file_name.get().strip()

    if not save_path:
        messagebox.showerror("错误", "保存路径未填写！")
        return
    
    # 使用用户输入的文件名或默认文件名
    if file_name:
        full_file_name = f"{file_name}"  # 如果有输入文件名，添加扩展名
    else:
        full_file_name = f"script_{script_id}" if script_id else "script_default"

    docx_full_path = os.path.normpath(os.path.join(save_path, full_file_name+".docx"))
    print(docx_full_path)

    # 这里可以添加你想要执行下载的逻辑
    # 例如：
    if bgm_confirm:
        result = messagebox.askyesno("下载确认", f"剧本和BGM将保存到：{save_path}")
    else:
        result = messagebox.askyesno("下载确认", f"剧本将保存为：{full_path}")

    if result:
        html_content = fetch_script(script_id)
        start_download(root, html_content, full_file_name, save_path, docx_full_path, bgm_confirm)
    else:
        pass



def start_download(root, html_content, file_name, save_path, full_path, bgm_confirm):
    # 开启新线程来执行下载，避免阻塞主线程
    script_thread = threading.Thread(target=parse_script, args=(html_content, full_path))
    if bgm_confirm:
        bgm_thread = threading.Thread(target=parse_bgm, args=(html_content, file_name, save_path))
    script_thread.start()
    bgm_thread.start()

    

def GUI_mainloop():

    # 创建主窗口
    root = tk.Tk()
    root.title("戏鲸剧本下载器")

    # 设置窗口大小
    root.geometry("600x280")

    # 创建标签和输入框的框架
    frame_id = tk.Frame(root)
    frame_id.pack(pady=10)

    label_id = tk.Label(frame_id, text="戏鲸剧本号：")
    label_id.pack(side=tk.LEFT)
    label_id.focus_set()

    entry_id = tk.Entry(frame_id, width=50)
    entry_id.pack(side=tk.LEFT, padx=(5, 0))

    # 输入文件名的框架
    frame_file_name = tk.Frame(root)
    frame_file_name.pack(pady=10)

    label_file_name = tk.Label(frame_file_name, text="保存文件名：")
    label_file_name.pack(side=tk.LEFT)

    entry_file_name = tk.Entry(frame_file_name, width=50)  
    entry_file_name.pack(side=tk.LEFT, padx=(5, 0))

    # 创建保存路径的框架
    frame_path = tk.Frame(root)
    frame_path.pack(pady=10)

    label_path = tk.Label(frame_path, text="    保存路径：")
    label_path.pack(side=tk.LEFT)

    entry_path = tk.Entry(frame_path, width=38)  # 调整宽度以适应按钮
    entry_path.pack(side=tk.LEFT, padx=(5, 0))  # 右侧留出间距

    # 选择路径按钮
    choose_button = tk.Button(frame_path, text="选择保存路径", command=lambda: on_choose_path(entry_path))
    choose_button.pack(side=tk.LEFT)

    # 设置初始保存路径为桌面
    default_save_path = os.path.normpath(os.path.expanduser(os.path.join("~", "Desktop")))
    print(default_save_path)
    entry_path.insert(0, default_save_path)  # 将默认路径插入输入框，不包含文件名

    # 创建一个变量来存储选项的状态
    bgm_confirm = tk.BooleanVar()

    # 创建选择框
    checkbutton = tk.Checkbutton(root, text="同时下载BGM", variable=bgm_confirm)
    checkbutton.pack(pady=3)

    # 确认下载按钮
    confirm_button = tk.Button(root, width=15, text="确认", command=lambda: on_confirm(root, entry_id, entry_path, entry_file_name, bgm_confirm))
    confirm_button.pack(pady=20)

    root.bind('<Return>', lambda event: on_confirm(root, entry_id, entry_path, entry_file_name, bgm_confirm))

    # 启动主循环
    root.mainloop()

