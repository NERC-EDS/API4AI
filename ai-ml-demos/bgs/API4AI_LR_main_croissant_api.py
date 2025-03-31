# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 08:43:26 2025

@author: itaga
"""

import os
import mlcroissant as mlc
from skimage.io import imread, imshow

from croissant_functions import get_images_urls_api
from img_processing_functions import *



# main_dir = 'C:/Users/itaga/Projects/API4AI/'
# json_csv = pd.read_csv (main_dir + 'json-in-csv.csv')

# Get image urls:
f = 'https://resources.bgs.ac.uk/petrologyThinSectionsHighResDemo/api-croissant.json' #main_dir + 'api-croissant.json'
ds = mlc.Dataset(f)
record_set = ds.metadata.record_sets
ppl_urls, xpl_urls, sample_ids = get_images_urls_api (ds, record_set)

######################################################################

# OPTIONAL: The output images can be saved to file, but they can also just be
# shown on screen without saving.
save_dir = 'C:/Users/itaga/Projects/API4AI/out/'
if not os.path.exists (save_dir): os.makedirs (save_dir)   
    
#####################################################################

img_num = 77    #Cool examples: 5, 10, 20, 30, 37, 40, 52, 61, 77

# Get sample id, and fix it if necessary:
sample_id = sample_ids[img_num]
if '/' in sample_id: sample_id = sample_id.replace ('/', '')

# Load images:
ppl_img = imread (ppl_urls[img_num])
xpl_img = imread (xpl_urls[img_num])
xpl_img_gray = imread (xpl_urls[img_num], as_gray=True)
# plot_test_image (ppl_img, xpl_img)

# Get mask to separate sample from background/box:
ppl_masked, xpl_masked, mask = mask_from_xpl_image (xpl_img_gray, xpl_img, ppl_img, LR=True, plot_checks=True)
    
# Use KMeans for some rough segmentation: 
# segmented_img is a "reconstruction" of the original image, assigning each 
# cluster the color closer to the original one. clust_img just assigns each
# pixel a cluster label. Clust_percs and clust_labels are the percentage
# of pixels in each cluster and a string label for each one.
segmented_img, clust_img, clust_percs, clust_labels = kmeans_segmentation (xpl_masked, num_clusters=8)

# Plot results:
plot_kmeans_segmentation_results (mask, xpl_masked, ppl_img, clust_img, 
                                  clust_percs, clust_labels, sample_id,
                                  save_fig=False, close_fig=False)

plot_kmeans_segmentation_results_zoomed (xpl_img, clust_img, clust_labels, sample_id, 
                                         LR=True, save_fig=False, close_fig=False)










