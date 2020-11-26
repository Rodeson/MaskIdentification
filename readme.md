# Readme

## Environment：

***Software：***

TensorFlow-GPU 2.3.0

Keras 2.4.3

CUDA 11.0

Python 3.7.4

***Hardware：***

GPU NVIDIA GeForce GTX 1050(4G)

CPU Inter(R) Core(TM) i7-8750H CPU @ 2.20GHz



## Information

1.项目名称:MaskIdentification

2.文件夹简介：

​    Annotation：存放标签,因为文件太大，打包时已删除

​    ImageSets：存放训练集 测试集图片名称

​    JPEGImages：存放图片文件 因为文件太大 打包时已删除

​    LOG：存放权重文件

​    yolo3：存放yolo模型

​    model_data:存放yolo模型配置文件

3.文件说明

​    convert.py 将.weight文件转为.h5文件

​    makeTxt.py随机生成训练集 测试集编号

​    voc_label.py将训练集路径信息与标签链接

​    yolo.py yolo设定模型参数，路径

​    yolo_video.py调用摄像头进行测试

4.程序运行方式 

​    使用终端打开该文件夹，并运行 pyhton yolo_video.py 等待片刻即可。



## Contact

If you have any problem when you try this project , you can contact with me by send email.

Email address: lds947003754@outlook.com (Subject : Github_MaskIdentification)  



由于权重文件大于100M 因此需要从网盘下载权重文件并放入Log文件夹内。

https://pan.baidu.com/s/1GNeG3sIZoEvrx7KPn0xbCw （vdl5 ）


## Reference

1.Weights

https://github.com/MacwinWin/face_mask_dataset

2.Dataset

https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset

3.Blogs

https://blog.csdn.net/qinchang1/article/details/89608058

https://blog.csdn.net/cungudafa/article/details/105074825\





