
# -*- coding: utf-8 -*-
#
# FastAPI输入输出参数配置
# Author: alex
# Created Time: 2020年05月04日 星期一 21时54分16秒
from typing import List
from pydantic import BaseModel, Field
from settings import det_args, reg_args

# 人脸关键点的样例
landmarks_example = [
    [30.2946, 51.6963],
    [65.5318, 51.5014],
    [48.0252, 71.7366],
    [33.5493, 92.3655],
    [62.7299, 92.2041]
]


class DetParams(BaseModel):
    """检测参数"""
    images: List[str] = Field(..., title='待检测的图像列表',
                              description='base64格式。每个图像可能会识别到多个人脸')
    threshold: float = Field(det_args['threshold'], ge=0.,
                             title='人脸检测的得分阈值',
                             description='可以使用该值过滤掉一些质量比较差的人脸')
    align: bool = Field(det_args['align'], title='人脸是否进行对齐',
                        description='若为true，则需要对返回的人脸进行对齐。')


class DetItem(BaseModel):
    """单个图像的检测结果"""
    faces: List[str] = Field(..., title='识别到的人脸图像列表',
                             description='base64格式')
    boxes: List[List[float]] = Field(..., example=[[10, 11, 15, 16]],
                                     title='人脸图像在原图像中的坐标',
                                     description='注意这里的坐标是相对于输入图像的。坐标格式：[x1, y1, x2, y2]')
    scores: List[float] = Field(..., example=[0.995],
                                title='人脸的得分值',
                                description='该值越大，人脸质量通常越好。前端可以根据该值做进一步的过滤')
    landmarks: List[List[List[float]]] = Field(..., example=[landmarks_example],
                                               title='人脸图像的关键点坐标',
                                               description='每个人脸有关键点共5个，注意这里的坐标是相对于输入图像的。坐标格式：[[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5]]')


class RegParams(BaseModel):
    """识别参数"""
    faces: List[str] = Field(..., title='待识别的人脸图像列表',
                             description='base64格式')


class RegItem(BaseModel):
    """单个人脸图像的识别结果"""
    embedding: List[float] = Field(..., title='人脸特征向量',
                                   description='每个人脸对应一个特征向量')