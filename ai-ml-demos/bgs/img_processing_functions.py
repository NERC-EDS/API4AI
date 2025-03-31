# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:20:03 2025

@author: itaga
"""


import numpy as np
import skimage as ski
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from sklearn.cluster import KMeans
from skimage.exposure import histogram
from scipy.signal import find_peaks, peak_widths


def mask_from_xpl_image (xpl_img_gray, xpl_img, ppl_img, LR=False, plot_checks=False):
    
    # Quick and dirty way to successfully automatically separate the box from 
    # the sample (there are more elegant ways to do it, but this should work). 
    # Get histogram, calculate its maximum and then find when it goes back to
    # background levels. Use that value as the threshold instead of using the
    # same value for all images.
    rel_heights = [0.9, 0.8, 0.7, 0.6]

    for rel_height in rel_heights:
        
        # print(rel_height)
        
        xpl_hist = histogram (xpl_img_gray, nbins=200)
        xpl_hist_x = xpl_hist[1]; xpl_hist_y = xpl_hist[0]
        xpl_hist_x = np.append (np.array([0.]), xpl_hist_x)
        xpl_hist_y = np.append (np.array([0.]), xpl_hist_y)
        hist_max = xpl_hist_y.max()
        hist_max_sample = int (np.argwhere (xpl_hist_y==xpl_hist_y.max())[0][0])
        # hist_max_height = xpl_hist[0][hist_max_sample]
        if LR == True: prom=6000
        else: prom = 100000
        peaks, _ = find_peaks (xpl_hist_y, prominence=prom)#height=hist_max)
        pwidths = list (peak_widths (xpl_hist_y, peaks, rel_height = rel_height)) # This contains peak width, 
                                                                                  # height at which width was 
                                                                                  # evaluated, and left and right 
                                                                                  # intersection points at 
                                                                                  # evaluation height
                                                                           
        # Discard peaks beyond 0.2:
        for ii, pp in enumerate(peaks):
            if xpl_hist_x[pp]>=0.2:
                pwidths = [np.delete (pwidths[j], np.where(peaks == pp)[0][0]) for j in range(len(pwidths))]
                peaks = np.delete(peaks, np.where(peaks == pp)[0][0])

        if len(peaks)==2 and peaks[1]-peaks[0]<4:
            # print ('Two prominent peaks found in close proximity...')
            # if pwidths[0][1] > pwidths[0][0]: pn=1
            # else: pn=0
            pn=1
            thresh_sample = int(np.round(pwidths[-1], 0)[pn])
            eval_height = pwidths[1][pn]
        elif len(peaks) <= 3:
            thresh_sample = int(np.round(pwidths[-1], 0)[0])
            eval_height = pwidths[1][0]    
        else:
            thresh_sample = np.nan

        # Our threshold should be the closest x value to the evaluated peak height
        # in the vicinity of the maximum:
        threshold = xpl_hist_x[thresh_sample]
        # print (threshold)
    
        # Apply threshold to cross polarised light image: this value comes from
        # looking at the histogram of the cross polarised light images and visually
        # choosing a threshold, there is no specific rule/reason to choose this 
        # value. There is probably a more scientific way of setting it, but this
        # works for the current example. (Otsu algorithm?)
        xpl_clean = xpl_img_gray > threshold
    
        # Fill edges from previously thresholded image and remove small spurious
        # objects that may remain:
        fill_edges = ndi.binary_fill_holes(xpl_clean)
        if LR==True: val=5000
        else: val=100000
        edges_clean = ski.morphology.remove_small_objects (fill_edges, val)
    
        # Get mask as a binary array instead of a boolean one:
        mask = edges_clean+1-1
        mask[mask==0] = 9999
        
        if (len(np.unique(mask))==1 or threshold>0.25) and rel_height!=rel_heights[-1]: 
            continue
        
        elif rel_height==rel_heights[-1] and len(np.unique(mask))==1:
            
            print ('Trimming histogram to find first peak...')
            
            xpl_hist_x_trim = xpl_hist_x[xpl_hist_x<0.1]
            xpl_hist_y_trim = xpl_hist_y[xpl_hist_x<0.1]
            hist_max_trim = xpl_hist_y_trim.max()
            hist_max_sample = int (np.argwhere (xpl_hist_y_trim==xpl_hist_y_trim.max())[0][0])
            # hist_max_height = xpl_hist[0][hist_max_sample]
            peaks, _ = find_peaks (xpl_hist_y_trim, prominence=1000)#height=hist_max_trim)
            pwidths = peak_widths (xpl_hist_y_trim, peaks, rel_height = rel_height) # This contains peak width, height at which width was evaluated,
                                                                                # left and right intersection points at evaluation height
            # Our threshold should be the closest x value to the evaluated peak height
            # in the vicinity of the maximum:
            thresh_sample = int(np.round(pwidths[-1], 0)[0])
            threshold = xpl_hist_x_trim[thresh_sample]
            eval_height = pwidths[1][0]
        
            # Apply threshold to cross polarised light image: this value comes from
            # looking at the histogram of the cross polarised light images and visually
            # choosing a threshold, there is no specific rule/reason to choose this 
            # value. There is probably a more scientific way of setting it, but this
            # works for the current example. (Otsu algorithm?)
            xpl_clean = xpl_img_gray > threshold
        
            # Fill edges from previously thresholded image and remove small spurious
            # objects that may remain:
            fill_edges = ndi.binary_fill_holes(xpl_clean)
            edges_clean = ski.morphology.remove_small_objects (fill_edges, 1000000)
        
            # Get mask as a binary array instead of a boolean one:
            mask = edges_clean+1-1
            mask[mask==0] = 9999
            if len(np.unique(mask))==1: raise TypeError ('Single mask value found!')
            
        else: break
    

    # Sanity check plot:
    if plot_checks==True:
        f, axes = plt.subplots (1, 2, figsize=(12, 5), layout='constrained')
        axes[0].plot (xpl_hist_x, xpl_hist_y, '.-k', markersize=0.7, linewidth=0.5)
        axes[0].axhline (eval_height, color='r')
        axes[0].axvline (threshold, color='orange', label='Box threshold')
        axes[0].set_title ('XPL Image histogram')
        axes[0].legend (loc='best')
        axes[0].set_ylabel ('Counts')
        axes[0].set_xlabel ('Grayscale value')

        axes[1].imshow (mask, cmap='Grays')
        axes[1].axis('off')
        axes[1].set_title ('Mask')
        plt.show()
    
    # Apply mask to images:
    ppl_masked = np.stack ([ppl_img[:,:,i]*mask for i in range(3)], axis=2)
    xpl_masked = np.stack ([xpl_img[:,:,i]*mask for i in range(3)], axis=2)
    ppl_masked[mask==9999] = 9999
    xpl_masked[mask==9999] = 9999

    return ppl_masked, xpl_masked, mask

 
def kmeans_segmentation (xpl_masked, num_clusters=5):
    
    # Use KMeans for some rough segmentation:
    image = xpl_masked.copy()
    X = np.float32 (image.reshape(-1,3))
     
    # Perform k-means clustering:
    k = num_clusters
    kmeans = KMeans(n_clusters=k, random_state=42).fit(X)
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # Calculate color that each cluster corresonds to and create segmented img:
    segmented_img = np.uint32 (centers[labels])
    segmented_img = segmented_img.reshape(image.shape)
     
    # Assign each image pixel its label:
    clust_img = labels.reshape (xpl_masked.shape[:2])
    # plt.imshow(clust_img)
    
    # Ideally, we'd want the box to be assigned to cluster 0:
    clust_img = find_box_cluster (clust_img)
    
    # Calculate percentage of pixels in each cluster:
    clust_percs = [np.round (len(labels[labels==ii])*100/len(labels), 1) for ii in range(k)]
    clust_labels = ['Cluster ' + str(ii) for ii in range(k)]
    
    print ('Percentage of pixels in each cluster (including box as Cluster 0):')
    for i in range(len(clust_labels)):
        print(clust_labels[i], '=', clust_percs[i], '%')
    
    return segmented_img, clust_img, clust_percs, clust_labels



def plot_test_image (ppl_img, xpl_img):
    
    f, axes = plt.subplots (1, 2, figsize=(8, 3), layout='constrained')
    axes[0].imshow (ppl_img)
    axes[1].imshow (xpl_img)
    axes[0].set_title ('Plane polarised light')
    axes[1].set_title ('Cross polarised light')    
    for ax in axes: ax.axis('off')
    plt.show()



def plot_kmeans_segmentation_results (mask, xpl_masked, ppl_img, clust_img, 
                                      clust_percs, clust_labels, sample_id, 
                                      img_save_dir=None, save_fig=False, 
                                      close_fig=False):
    
    # Colormap for clustered image:
    cmap = plt.get_cmap('Set1_r', len(np.unique(clust_img)))
    colors = cmap (np.linspace(0, 1, len(np.unique(clust_img))))
    # cmap.set_bad('darkgrey', alpha=1)
    # colors = ['dimgray', 'orangered', 'orange', 'lime', 'darkturquoise',
    #           'purple']
    # cmap = mpl.colors.ListedColormap (colors)

    bounds = np.arange (np.unique(clust_img).min()-0.5, 
                                  np.unique(clust_img).max()+1.5, 1)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    # Plot original images together with clustered one:
    f, axes = plt.subplots (2, 2, figsize=(10, 8), layout='constrained')
    # plt.subplots_adjust(wspace=0.05, hspace=0.1)
    axes[0, 0].imshow (ppl_img)
    axes[0, 0].contour (mask, colors=['r'], linewidths=[0.6])
    axes[0, 1].imshow (xpl_masked)
    # axes[0, 1].contour (mask, colors=['r'], linewidths=[0.6])
    axes[1, 0].pie (clust_percs[1:], labels=clust_labels[1:], autopct='%1.1f%%',
                    colors=colors[1:])
    im = axes[1, 1].imshow (clust_img, cmap=cmap, 
                         # vmin=np.unique(X_labelled).min(),
                         # vmax=np.unique(X_labelled).max(), 
                         norm=norm,)
    axes[0, 0].set_title ('Plane polarised light + Mask')
    axes[0, 1].set_title ('Cross polarised light (masked)')
    axes[1, 1].set_title ('Segmented image')
    axes[1, 0].set_title ('Percentage of pixels in each cluster')
    for ii in range(2):
        for ax in axes[ii]: ax.axis('off')
    
    # Create axes for the colorbar
    # divider = make_axes_locatable (axes[2])
    # cax = divider.append_axes ("right", size="5%", pad=0.1)
    cb = plt.colorbar (mpl.cm.ScalarMappable(cmap=cmap, norm=norm), 
                       ax=axes[1, 1], extend='both', spacing='proportional',
                       ticks=np.unique(clust_img),
                       shrink=0.5)
    # cb.set_ticks (np.unique(X_labelled), labels=np.unique(X_labelled))
    # cb.set_label ('Cluster number', rotation=-90, labelpad=15)
    yticks_labels = clust_labels.copy(); yticks_labels[0] = 'Box'
    cb.ax.set_yticklabels (yticks_labels)  
    cb.minorticks_off()
    
    # Add title:
    f.suptitle ('Sample = ' + sample_id, fontsize=18)
    
    # Save un-zoomed image:
    if save_fig==True:
        fname = img_save_dir + 'segmentation_test_img_' + str(sample_id)
        plt.savefig (fname + '.jpg', bbox_inches='tight', dpi=300)
    if close_fig==True: plt.close()

    plt.show()
    

def plot_kmeans_segmentation_results_zoomed (xpl_img, clust_img, clust_labels,
                                             sample_id, LR=False, img_save_dir=None, 
                                             save_fig=False, close_fig=False):

    # Colormap for clustered image:
    cmap = plt.get_cmap('Set1_r', len(np.unique(clust_img)))
    colors = cmap (np.linspace(0, 1, len(np.unique(clust_img))))
    # cmap.set_bad('darkgrey', alpha=1)
    # colors = ['dimgray', 'orangered', 'orange', 'lime', 'darkturquoise']
    # cmap = mpl.colors.ListedColormap (colors)

    bounds = np.arange (np.unique(clust_img).min()-0.5, 
                                  np.unique(clust_img).max()+1.5, 1)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
    # Zoom in segmented image and compare with cross polarised light image:    
    f, axes = plt.subplots (1, 2, figsize=(15, 8), sharex='all', sharey='all',
                            layout='constrained')
    axes[0].imshow (xpl_img)
    im = axes[1].imshow (clust_img, cmap=cmap, norm=norm,)    
    for ax in axes: ax.axis('off')
    cb = plt.colorbar (mpl.cm.ScalarMappable(cmap=cmap, norm=norm), 
                       ax=axes[1], extend='both', spacing='proportional',
                       ticks = np.unique(clust_img),
                       shrink=0.4)
    cb.minorticks_off()
    # cb.set_ticks (np.unique(X_labelled), labels=np.unique(X_labelled))
    # cb.set_label ('Cluster number', rotation=-90, labelpad=15)
    yticks_labels = clust_labels.copy(); yticks_labels[0] = 'Box'
    cb.ax.set_yticklabels (yticks_labels)  
    axes[0].set_title ('Cross polarised light')
    axes[1].set_title ('Segmented image')

    # Plot square in the middle of the image:
    if LR==False: square_size = 800
    else: square_size = 200
    x_size= xpl_img.shape[1]; y_size = xpl_img.shape[0]
    axes[0].set_xlim ([int((x_size/2)-square_size/2), int((x_size/2)+square_size/2)])
    axes[0].set_ylim ([int((y_size/2)+square_size/2), int((y_size/2)-square_size/2)])

    # Add title:
    f.suptitle ('Sample = ' + sample_id, fontsize=18)
    
    if save_fig==True:
        fname = img_save_dir + 'segmentation_test_img_' + str(sample_id)
        plt.savefig (fname + '_zoomed.jpg', bbox_inches='tight', dpi=300)
    if close_fig==True: plt.close()

    plt.show()



def find_box_cluster (clust_img):
    
    # The box isn't always the largest cluster, since sometimes the sample is
    # quite large in size. However, we can use the cluster number along the 
    # edges of the image and that should tell us which cluster number corresponds
    # to the box.
    
    # Get cluster number for the four sides of the image:
    c_vals = [clust_img[0,:], clust_img[-1, :], clust_img[:, 0], clust_img[:, -1]]
    
    # Create empty list to put the most frequent cluster number in:
    clust_nums = np.zeros (len(c_vals))
    
    # Get most frequent cluster number/label in each side of the image:
    for i, cv in enumerate(c_vals):
        vals, counts = np.unique (cv, return_counts=True)

        for j, count in enumerate(counts):
            
            if count==counts.max():
                clust_nums[i] = vals[j]
                # print (vals[cc], clust_nums[cv])
                
    box_clust, box_counts = np.unique (clust_nums, return_counts=True)

    # There might be more than one cluster number in box_clust. Take the value
    # that appears most often as the box_cluster:
    if len(box_clust)!=1:
        for bc, count in enumerate(box_counts):
            print(bc, count)
            if count==box_counts.max(): box_clust=box_clust[bc]; box_counts=box_counts[bc]
            

    # If the box cluster is not cluster 0, change labels to make it so:
    if box_clust != 0:
        clust_img[clust_img==box_clust] = 999
        clust_img[clust_img==0] = box_clust
        clust_img[clust_img==999] = 0

    return clust_img


    
    
    
    
    
    
