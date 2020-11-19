import os
import h5py
import numpy as np
import pandas as pd
import cv2


def get_box_data(data, index):
    meta_data = dict()
    meta_data['height'] = []
    meta_data['label'] = []
    meta_data['left'] = []
    meta_data['top'] = []
    meta_data['width'] = []

    def print_attrs(name, obj):
        vals = []
        if obj.shape[0] == 1:
            vals.append(obj[0][0])
        else:
            for k in range(obj.shape[0]):
                vals.append(int(data[obj[k][0]][0][0]))
        meta_data[name] = vals

    box = data['/digitStruct/bbox'][index]
    data[box[0]].visititems(print_attrs)
    return meta_data

train_name = os.listdir("/home/sidney/Desktop/hw2/data/custom/images/train")

train_name.sort(key=lambda x: int(x[:-4]))
tpath = []
for i in train_name:
    tpath.append('/home/sidney/Desktop/hw2/data/custom/images/train/'+i)

with open('/home/sidney/Desktop/hw2/data/custom/train.txt', 'w') as f:
    for item in tpath:
        f.write("%s\n" % item)

valid_name = os.listdir("/home/sidney/Desktop/hw2/data/custom/images/valid")
valid_name.sort(key=lambda x: int(x[:-4]))
vpath = []
for i in valid_name:
    vpath.append('/home/sidney/Desktop/hw2/data/custom/images/valid/'+i)

with open('/home/sidney/Desktop/hw2/data/custom/valid.txt', 'w') as f:
    for item in vpath:
        f.write("%s\n" % item)

d = h5py.File('/home/sidney/Desktop/hw2/digitStruct.mat', 'r')


def turn_to_txt(a, b):
    for i in range(a, b):
        H = np.array([])
        W = np.array([])
        label = np.array([])
        x_center = np.array([])
        y_center = np.array([])

        # if you have valid data, change train_name to valid_name
        img = cv2.imread("/home/sidney/Desktop/hw2/data/custom/images/train/" +
                         train_name[i-a])
        height = img.shape[0]
        width = img.shape[1]
        box = get_box_data(d, i)
        h = np.array([box['height'] for d in box if 'height' in d])
        w = np.array([box['width'] for d in box if 'width' in d])
        left = np.array([box['left'] for d in box if 'left' in d])
        top = np.array([box['top'] for d in box if 'top' in d])
        lab = np.array([box['label'] for d in box if 'label' in d])

        H = np.append(H, h/height)
        W = np.append(W, w/width)
        x_center = np.append(x_center, (left+w/2)/width)
        y_center = np.append(y_center, (top+h/2)/height)
        label = np.append(label, lab)
        label = label-1
        data = pd.DataFrame()
        data['label_idx'] = label.astype(int)
        data['x_center'] = x_center
        data['y_center'] = y_center
        data['width'] = W
        data['height'] = H
        np.savetxt('/home/sidney/Desktop/hw2/data/custom/labels/train/' +
                   train_name[i-a][:-4]+'.txt', data, fmt='%d %f %f %f %f')
    return data

turn_to_txt(100, 33402)
# turn_to_txt(0,100)
