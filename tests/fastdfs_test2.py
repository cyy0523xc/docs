'''
python上传测试

Author: alex
Created Time: 2020年09月14日 星期一 15时44分39秒
'''
import requests
from io import BytesIO
from PIL import Image

# 这种方式貌似有问题，暂时不要使用
url = 'http://192.168.80.242:20936/group1/upload'
img = Image.open('/home/alex/图片/img_8563.jpg')
buf = BytesIO()
img.save(buf, 'jpeg')
buf.seek(0)
files = {
    'file': buf
}
data = {
    'output': 'json',
    'scene': 'pdf',
}

res = requests.post(url, files=files, data=data).json()
print(res)
buf.close()
