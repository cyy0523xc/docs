
# -*- coding: utf-8 -*-
#
# FastAPI入口
# Author: alex
# Created Time: 2020年05月04日 星期一 21时52分59秒
from typing import List
from fastapi import FastAPI
# from fastapi import status, HTTPException
from ibbd_algo.utils import conc_map
from image_utils.convert import base64_cv2, cv2_base64
from main_settings import DetItem, DetParams
from main_settings import RegItem, RegParams
from server import images_detect, images_recognize        # 这是人脸检测与识别的主函数
from settings import det_args, reg_args, cpu_workers

DESCRIPTION = """
主要实现功能：

- 人脸检测
- 人脸识别

### 接口列表：

"""
DET_URL = '/images/detect'
REG_URL = '/images/recognize'
if det_args['open']:
    DESCRIPTION += '- 人脸检测 %s\n' % DET_URL
if reg_args['open']:
    DESCRIPTION += '- 人脸识别 %s\n' % REG_URL
DESCRIPTION += """\n

### 使用说明

1. 将图像转为base64格式

可以看这里：https://github.com/ibbd-dev/python-image-utils/blob/master/image_utils/convert.py ，方法`pil_base64`或者`cv2_base64`

2. 测试代码: 看[这里](https://github.com/IBBD/docs/blob/main/tests/%E4%BA%BA%E8%84%B8%E8%AF%86%E5%88%AB%E5%BC%95%E6%93%8E%E6%B5%8B%E8%AF%95.ipynb)。

"""

# 版本号
VERSION = '0.8'
app = FastAPI(
    title="人脸检测与识别引擎",
    description=DESCRIPTION,
    version=VERSION,
)

if det_args['open']:
    @app.post(DET_URL, response_model=List[DetItem],
              summary='人脸检测')
    async def api_detect(params: DetParams):
        """输入多个图像，返回人脸box及其关键点
        说明：一个图像可能会识别到多个人脸
        """
        if len(params.images) == 0:
            return []
        params.images = conc_map(base64_cv2, params.images,
                                 max_workers=cpu_workers)
        res = images_detect(**dict(params))
        for img_data in res:     # 格式化返回值
            img_data['faces'] = conc_map(cv2_base64, img_data['faces'],
                                         max_workers=cpu_workers)
            img_data['scores'] = list(img_data['scores'])
            img_data['boxes'] = [list(b) for b in img_data['boxes']]
            img_data['landmarks'] = [[list(l) for l in lmk] 
                                      for lmk in img_data['landmarks']]

        return res

if reg_args['open']:
    @app.post(REG_URL, response_model=List[RegItem],
              summary='人脸识别')
    async def api_recognize(params: RegParams):
        """人脸识别，返回人脸特征向量，每个人脸图像会对应一个特征向量
        每个特征向量是一个多维的列表
        """
        if len(params.faces) == 0:
            return []
        params.faces = conc_map(base64_cv2, params.faces,
                                max_workers=cpu_workers)
        res = images_recognize(**dict(params))
        for data in res:     # 格式化返回值
            data['embedding'] = data['embedding'].tolist()

        return res