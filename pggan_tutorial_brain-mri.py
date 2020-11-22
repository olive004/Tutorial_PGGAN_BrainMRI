# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 
# https://www.kaggle.com/mateuszbuda/lgg-mri-segmentation#TCGA_CS_6188_20010812_13_mask.tif

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.
########################## m'code
from PIL import Image
import matplotlib
import cv2


# EDA: CHECKED ALL THE BRAIN MRI SEGS AND THEY'RE ALL (256, 256)
def is_image(filename):
    extensions = {".jpg", ".png", ".gif", ".tif"}    # Accepted extensions we workin with
    img_bool = False
    for ext in extensions:
        img_bool = filename.endswith(ext)
        if img_bool: break
    return img_bool

# check that all the images are unifrom in dimension
def get_unique_img_dims():
    dims = set()    # initialize set, where set.add(v) adds v if v unique
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            if is_image(filename):
                image = Image.open(os.path.join(dirname, filename))
                dims.add(image.size)
#             else: continue
    print(dims) 
    
    
    
    
    
    
# load an image as an rgb numpy array       FUNCTION FROM https://machinelearningmastery.com/how-to-train-a-progressive-growing-gan-in-keras-for-synthesizing-faces/
def load_image(filepath):
    # load image from file
#     image = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    image = Image.open(filepath)
    # convert to RGB, if needed
    image = image.convert('RGB')
    # Resize image before converting to an array
    new_size = (128,128)
    image = image.resize(new_size)
    # convert to array
    pixels = np.asarray(image)
    print('yerrr')
    return pixels


# load images and extract faces for all images in a directory
def load_images(n_images):
    images = list()
    # enumerate files
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
#             print(os.path.join(dirname, filename))
#             if is_image(filename):
            # load the image
            if len(images) >= n_images:
                break
            print('filename', filename)
            print(len(images))
            
            if is_image(filename):
                print(os.path.join(dirname, filename))
                pixels = load_image(os.path.join(dirname, filename))
#                 print('pixels:', pixels)
            # store
                if (pixels is not None):
                    images.append(pixels)
    #                 print(len(pixels), pixels.shape)
                else: images.append(0)
                # stop once we have enough
#     print(images)
    print('returning images')
    return np.asarray(images)



        


# Random image for testing
# random_img = load_image('/kaggle/input/lgg-mri-segmentation/kaggle_3m/TCGA_HT_7684_19950816/TCGA_HT_7684_19950816_22.tif')
# print(random_img.shape)
# random_img = cv2.resize(random_img, (128,128))
# display(random_img.shape)










