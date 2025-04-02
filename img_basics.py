"""
just some useful basic stuff
"""

import os
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt


### crop print-screens to gui window
d = 'docs/images/photos/gui_/Pictures/'
img_paths = [os.path.join(d,f) for f in os.listdir(d)]
# show an image to find crop specs
im = cv2.imread(img_paths[1], cv2.IMREAD_UNCHANGED)
plt.figure()
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.show()
# test
plt.figure()
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)[126:885, 272:1645])
plt.show()
# crop
for p in img_paths:
    im = cv2.imread(p, cv2.IMREAD_UNCHANGED)[126:885, 272:1645]
    cv2.imwrite(p, im)
