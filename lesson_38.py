"""
Lesson 38: Intro to Image processing
"""

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import seaborn as sns
sns.set()

import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

#plt.imshow(phase_im, cmap=plt.cm.viridis)

hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')

# Apply a threshold to our Image
thresh = 270
im_phase_thresh = phase_im < thresh

with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)

plt.close()

with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

#plt.show()
plt.close()

# Slice out region with a hot pixel.
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)

# Generate a structural element
selem = skimage.morphology.square(3)
cfp_filt = skimage.filters.median(cfp_im, selem)
with sns.axes_style('dark'):
    plt.imshow(cfp_filt[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)
#plt.show()
plt.close()

cfp_hist, cfp_bins = skimage.exposure.histogram(cfp_filt)
plt.plot(cfp_bins, cfp_hist)
plt.xlabel('pixel value')
plt.ylabel('counts')

#plt.show()
plt.close()

cfp_thresh = cfp_filt > 120
with sns.axes_style('dark'):
    plt.imshow(cfp_thresh, cmap=plt.cm.Greys_r)

plt.show()
plt.close()

phase_thresh = skimage.filters.threshold_otsu(phase_im)
cfp_thresh = skimage.filters.threshold_otsu(cfp_filt)
phase_otsu = phase_im < phase_thresh
cfp_otsu = cfp_filt > cfp_thresh

with sns.axes_style('dark'):
    plt.figure()
    plt.imshow(phase_otsu, cmap=plt.cm.Greys_r)
    plt.title('phase_otsu')
    plt.figure()
    plt.imshow(cfp_otsu, cmap=plt.cm.Greys_r)
    plt.title('cfp_otsu')

plt.show()
plt.close()
