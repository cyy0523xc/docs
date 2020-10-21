'''
配置文件

Author: alex
Created Time: 2020年09月27日 星期日 16时11分09秒
'''

# 可以根据实际需要配置cpu算法的worker数量
# 该值不应该超过cpu的核数
cpu_workers = 4

# 通常不需要修改这里的配置
# mtcnn人脸检测算法参数
mtcnn_args = {
    'model_path': 'models/det',
    'use_gpu': True,      # 是否使用GPU
    'gpu': 0,             # gpu id
    'num_worker': 2,
    'minsize': 20,        # 检测的人脸的最小尺寸
}

# 人脸检测配置
# 如果不需要启动人脸检测，则将open参数设置为False
det_args = {
    'open': True,       # 当该值为True时，则启动该模型
    'model': 'mtcnn',
    # 检测的阈值默认值，大于该值才会返回
    'threshold': 0.9,   # 该值越大，满足条件的越少
    'align': False,     # 人脸检测是否进行对齐的默认值
    'args': mtcnn_args,
}

# 人脸识别参数
# 如果不需要启动人脸识别，则将open参数设置为False
reg_args = {
    'open': True,       # 当该值为True时，则启动该模型
    # 'align': True,      # 人脸识别前是否进行对齐的默认值
    'args': {
        'gpu': 0,
        'model': 'models/rec/model,0',
        'image_size': (112, 112),
    }
}