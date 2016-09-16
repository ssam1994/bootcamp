"""
Exercise 5
"""

import numpy as np
import scipy.stats
from os import listdir
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import seaborn as sns
sns.set_style('dark')

import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters
import skimage.measure

# Segment function
def segment(img, phase_contrast=False):
    if phase_contrast:
        # Apply a gaussian blur to the image.
        im_blur = skimage.filters.gaussian(img, 50.0)
        im_float = skimage.img_as_float(img)
        seg = im_float - im_blur

    else:
        thresh = skimage.filters.threshold_otsu(img)
        seg = img < thresh
    return seg

# Label function
def label(seg):
    seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
    props = skimage.measure.regionprops(seg_lab)

    areas = np.array([prop.area for prop in props])
    cutoff = 100

    im_cells = np.copy(seg_lab) > 0
    for i, _ in enumerate(areas):
        if areas[i] < cutoff:
            im_cells[seg_lab==props[i].label] = 0

    area_filt_lab = skimage.measure.label(im_cells)
    return area_filt_lab

# Burn in scale bar
def add_scale_bar(img, ipx_dist, scale_len, x=100, y=100):
    # Interpixel distance
    scale_bar = scale_len / ipx_dist
    plt.plot([x, x+scale_bar], [y, y], linestyle='-', linewidth=4)
    plt.text(x+scale_bar, y, str(scale_len)+'µm')

# Initialize list of files in directory
mypath = 'data/bacterial_growth/'
file_list = sorted([f for f in listdir(mypath) if '.tif' in f])

# Add list of images into array
im_list = []
for image_file in file_list:
    img = skimage.io.imread(mypath + image_file)
    im_list.append(img)

# Segment images
segmented_images = [segment(i) for i in im_list]

# Add scale bar
interpix_distance = 0.0636 #µm
plt.figure()
plt.imshow(segmented_images[0])
add_scale_bar(segmented_images[0], interpix_distance, 10)

# Growth curve
# y_vals = np.zeros(len(segmented_images))
# for i, img in enumerate(segmented_images):
#     flat = img.flatten()
#     y_vals[i] = len(flat) - sum(flat)
# plt.close()
# plt.plot(y_vals)

# Initialize list of files in directory
my_HG_path = 'data/HG105_images/'
HG_list = sorted([f for f in listdir(my_HG_path) if '.tif' in f])

# Add list of images into array
im_HG_list = []
for image_file in HG_list:
    img = skimage.io.imread(my_HG_path + image_file)
    img_seg = segment(img, phase_contrast=True)
    im_HG_list.append(img_seg)
