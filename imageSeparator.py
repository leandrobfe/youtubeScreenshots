import os
import shutil
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from skimage.feature import hog

# Define the directory containing your images
image_dir = 'D:/Leandro/Programação/PyVideoPrint'

# Define the base directory for the output folders
output_dir = 'D:/Leandro/Programação/PyVideoPrint/output'

# Create the base directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Extract HOG features from the images
features = []
filenames = []
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Add any other image types if needed.
        try:
            with Image.open(os.path.join(image_dir, filename)) as img:
                feature = hog(np.array(img.convert('L')), pixels_per_cell=(16, 16))
                features.append(feature)
                filenames.append(filename)
        except Exception as e:
            print(f"Unable to process image {filename}. Error: {e}")

# Cluster the images based on their HOG features
kmeans = KMeans(n_clusters=2, random_state=0).fit(features)

# Move the images into different folders based on their assigned cluster
for filename, cluster in zip(filenames, kmeans.labels_):
    cluster_dir = os.path.join(output_dir, f'cluster_{cluster}')
    os.makedirs(cluster_dir, exist_ok=True)
    shutil.copy(os.path.join(image_dir, filename), cluster_dir)
