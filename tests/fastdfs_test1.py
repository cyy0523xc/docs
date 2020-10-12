'''
python上传测试

Author: alex
Created Time: 2020年09月14日 星期一 15时44分39秒
'''
import requests

url = 'http://192.168.80.242:20936/group1/upload'
files = {
    'file': open('./test.py', 'rb')
}
data = {
    'output': 'json',
    'scene': 'pdf'
}

res = requests.post(url, files=files, data=data).json()
print(res)
