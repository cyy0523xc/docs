'''
python上传测试

Author: alex
Created Time: 2020年09月14日 星期一 15时44分39秒
'''
import requests

# 不同的项目，上传地址可能是不一样的
url = 'http://192.168.80.242:20936/group1/upload'
files = {
    'file': open('./test.py', 'rb')
}
# scene: 该参数有命名空间的效果，根据实际需要传递
data = {
    'output': 'json',
    'scene': 'pdf'
}

res = requests.post(url, files=files, data=data).json()
print(res)
