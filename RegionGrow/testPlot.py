import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#image = mpimg.imread('../data/images/201309011030_001_001.png')
image = mpimg.imread('3.bmp')

from skimage import morphology
from skimage.morphology import watershed, is_local_maximum
from scipy import ndimage

image = image[:,:,0]
distance = ndimage.distance_transform_edt(image)
#local_maxi = is_local_maximum(distance)
local_maxi = is_local_maximum(distance, image, np.ones((25, 25)))
markers = morphology.label(local_maxi)
labels_ws = watershed(-distance, markers, mask=image)

#C = image[labels_ws]
plt.imshow(labels_ws)
plt.show()