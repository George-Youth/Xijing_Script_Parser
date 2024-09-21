from script import parse_script, fetch_script

import tkinter as tk
from tkinter import messagebox, filedialog
import os

def on_choose_path(entry_path):
    # 选择文件保存路径
    path = filedialog.askdirectory()  # 选择目录而不是文件
    if path:
        entry_path.delete(0, tk.END)  # 清空当前路径
        entry_path.insert(0, path)  # 插入选择的路径
    return entry_path

def on_confirm(entry_id, entry_path, entry_file_name):
    # 此处添加确认下载逻辑
    script_id = entry_id.get().strip()
    save_path = entry_path.get().strip()
    file_name = entry_file_name.get().strip()

    if not save_path:
        messagebox.showerror("错误", "保存路径未填写！")
        return
    
    # 使用用户输入的文件名或默认文件名
    if file_name:
        full_file_name = f"{file_name}.docx"  # 如果有输入文件名，添加扩展名
    else:
        full_file_name = f"script_{script_id}.docx" if script_id else "script_default.docx"

    full_path = os.path.join(save_path, full_file_name)

    # 这里可以添加你想要执行下载的逻辑
    # 例如：
    messagebox.showinfo("下载确认", f"剧本将保存到：{full_path}")
    parse_script(fetch_script(script_id), full_path)  # 假设这是实际下载函数

def GUI_mainloop():

    # 创建主窗口
    root = tk.Tk()
    root.title("戏鲸剧本下载器")

    # 设置窗口大小
    root.geometry("600x250")

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

    label_path = tk.Label(frame_path, text="保存路径：")
    label_path.pack(side=tk.LEFT)

    entry_path = tk.Entry(frame_path, width=40)  # 调整宽度以适应按钮
    entry_path.pack(side=tk.LEFT, padx=(5, 0))  # 右侧留出间距

    # 选择路径按钮
    choose_button = tk.Button(frame_path, text="选择保存路径", command=lambda: on_choose_path(entry_path))
    choose_button.pack(side=tk.LEFT)

    # 设置初始保存路径为桌面
    default_save_path = os.path.join(os.path.expanduser("~"), "Desktop")
    entry_path.insert(0, default_save_path)  # 将默认路径插入输入框，不包含文件名

    # 确认下载按钮
    confirm_button = tk.Button(root, text="确认", command=lambda: on_confirm(entry_id, entry_path, entry_file_name))
    confirm_button.pack(pady=20)

    root.bind('<Return>', lambda event: on_confirm(entry_id, entry_path, entry_file_name))

    # 启动主循环
    root.mainloop()

