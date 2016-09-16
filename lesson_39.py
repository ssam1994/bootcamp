"""
Lesson 39: Intro to Image processing
"""

import numpy as np
import scipy.stats
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

phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.show()
plt.close()

# Apply a gaussian blur to the image.
im_blur = skimage.filters.gaussian(phase_im, 50.0)

# Show the blurred image.
plt.imshow(im_blur, cmap=plt.cm.viridis)
plt.show()
plt.close()

phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

plt.show()
plt.close()

thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

plt.close('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)
plt.show()

# Label cells
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)

plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)
plt.show()
plt.close()

# Compute the regionproperties and extract area of each object.
ip_dist = 0.063 # µm per pixel
props = skimage.measure.regionprops(seg_lab)

areas = np.array([prop.area for prop in props])
cutoff = 300

im_cells = np.copy(seg_lab) > 0
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)
plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
plt.show()
plt.close()
