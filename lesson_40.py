"""
Lesson 40: Intro to Image processing
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

def segmentation(im_file, thresh_range):
    im = skimage.io.imread(im_file)

    # Correct for uneven illumination.
    im_blur = skimage.filters.gaussian(im, 50.0)
    im_float = skimage.img_as_float(im)
    im_sub = im_float - im_blur

    # Correct for "hot" or "bad" pixels in an image.
    thresh = skimage.filters.threshold_otsu(im_sub)
    seg = im_sub < thresh

    # Perform a thresholding operation.

    # Remove bacteria or objects near/touching the image border.

    # Remove objects that are too large (or too small) to be bacteria.
    im_cells = np.copy(seg_lab) > 0
    for i, _ in enumerate(areas):
        if areas[i] < cutoff:
            im_cells[seg_lab==props[i].label] = 0

    area_filt_lab = skimage.measure.label(im_cells)

    return area_filt_lab
