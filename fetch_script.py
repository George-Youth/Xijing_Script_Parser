import requests
from tkinter import messagebox

def fetch_script(script_id):
    url = f'https://aipiaxi.com/article-detail/{script_id}'  # 拼接URL
    try:
        response = requests.get(url)

        # 检查是否错误
        if response.status_code != 200:
            messagebox.showerror("错误", f"网页访问出错，状态码{response.status_code}")
            return

        response.raise_for_status()  # 确保请求成功
        html_content = response.text

        if "timeout:" in html_content:  # 检查页面内容是否为空
            messagebox.showerror("错误", "访问超时，请确认剧本号是否存在")
            return

        return html_content
    
    except Exception as e:
        messagebox.showerror("错误", str(e))
