import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = ['train', 'test', 'val']

classes = ["mask", "unmask"]  # 我们只是检测细胞，因此只有一个类别


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('E:/code/python/YoloMask/MaskPrj/Annotations/%s.xml' % (image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymin').text),
             int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b])+ ',' + str(cls_id) )


wd = getcwd()
print(wd)
for image_set in sets:
    image_ids = open('E:/code/python/YoloMask/MaskPrj/ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('E:/code/python/YoloMask/MaskPrj/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('E:/code/python/YoloMask/MaskPrj/images/%s.jpg' % (image_id))
        convert_annotation(image_id)
        list_file.write('\n')
    list_file.close()