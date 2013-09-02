'''
% ccf.m - Curvelet Co-occurrence Features Extraction by Fast Discrete Curvelet Transform via wedge wrapping - Version 1.0
%
% Inputs
%   x           M-by-N matrix
%
% Optional Inputs
%   graylevel   8, 16, 64, or 256
%   is_real     Type of the transform
%                   0: complex-valued curvelets
%                   1: real-valued curvelets
%               [default set to 1]
%   finest      Chooses one of two possibilities for the coefficients at the
%               finest level:
%                   1: curvelets
%                   2: wavelets
%               [default set to 2]
%   nbscales    number of scales including the coarsest wavelet level
%               [default set to 3]
%   nbangles_coarse
%               number of angles at the 2nd coarsest level, minimum 8,
%               must be a multiple of 4. [default set to 8]
%
% Outputs
%   MEAN - MEAN;    SD - Standard Deviation;    CT - Cluster tendency;
%   HG - Homogeneity;   MP - Maximum probability;
%   ENG - Energy;   INE - Inertia;      IDM - Inverse Difference Moment;
%   ENT - Entropy;  COR - Correlation;  SM - Sum-mean;
%   DM - Difference-mean;   SE - Sum-Entropy;   DE - Difference-Entropy.
%   ANGLES - number of angles or sub-band matrice at each level
%
% By Kasperl Zhang, 2009

'''
from scipy import misc
import matplotlib.pyplot as plt
from fdct_wrapping import *
def ccf( x, graylevel=16, is_real = 1, finest = 2, nbscales = 3, nbangles_coarse = 8 ):
    C = fdct_wrapping(x, is_real, finest, nbscales, nbangles_coarse)
    return C

if __name__ == "__main__":
    XX = misc.imread('test1.jpg')
    XX= XX[:,:,0] if XX.shape[2] > 1 else XX#if RGB,only tackle R
    
    print(ccf(XX))
    
    #plt.imshow(X)
    #plt.show()

    
    
    
    