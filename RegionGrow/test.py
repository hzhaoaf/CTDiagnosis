from scipy import misc
import matplotlib.pyplot as plt
import numpy as np


def norShow(X):
    if X.max()<= pow(10,-6):
        print("All points are black,fail.")
        return
    
    Y=np.round(X / X.max() * 255)
    imgplot = plt.imshow(Y)
    print(123)
    #imshow(Y)

if __name__ == "__main__":
    #XX = misc.imread('../data/images/123.png')
    XX = misc.imread('../data/images/201309011030_001_001.png')
    
    #If it's a gray image, shape of XX would be 2d ,sth like (73,63)
    if len(XX.shape) == 2:
        pass
    else:
        XX= XX[:,:,0] if XX.shape[2] > 1 else XX#if RGB,only tackle R
    norShow(XX)
    