import requests
from tkinter import messagebox



def fetch_script(script_id):
    url = f'https://aipiaxi.com/article-detail/{script_id}'  # 拼接URL
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091202 Firefox/3.5.6'}
    try:
        response = requests.get(url = url, headers = headers)

        # 检查是否错误
        if response.status_code != 200:
            messagebox.showerror("错误", f"网页访问出错，状态码{response.status_code}")
            return
        else:

            response.raise_for_status()  # 确保请求成功
            html_content = response.text.replace('\\u002F', '/')

            if "timeout:" in html_content:  # 检查页面内容是否为空
                messagebox.showerror("错误", "访问超时，请确认剧本号是否存在")
                return

            return html_content
    
    except Exception as e:
        messagebox.showerror("错误", str(e))
