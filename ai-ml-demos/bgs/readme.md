# BGS Croissant Example:

## Accessing and processing rock sample images from a Croissant file

TODO add some information about the Croissant file and/or API, where the images come from, etc?

## Notebook demonstrating ML workflow with Croissant
The Jupyter notebook in this repository provides an example of how standardized Croissant files can be used for Machine Learning-based data analysis. It uses a Croissant file pointing to a small set of thin-section image pairs (plane and cross polarised) to access the data. The firs step in the analysis consists of separating the rock sample in the image from the box around it. Next, we use clustering to perform a basic image segmentation process, which allows us to obtain a first visual approximation to the mineral composition of the sample.

The Python environment required to run this notebook can be replicated using the included .yml file. Additionally, the notebook utilizes several functions from the img_processing_functions and croissant_functions libraries (also present in the repository) for image access or analysis.
