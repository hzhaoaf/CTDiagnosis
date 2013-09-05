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
from skimage.feature import greycomatrix
from preglcm import preglcm

def ccf( x, graylevel=16, is_real = 1, finest = 2, nbscales = 3, nbangles_coarse = 32):
    #% curvelet decomposition
    #%   C           Cell array of curvelet coefficients.
    #%               C{j}{l}(k1,k2) is the coefficient at
    #%                   - scale j: integer, from finest to coarsest scale,
    #%                   - angle l: integer, starts at the top-left corner and
    #%                   increases clockwise,
    #%                   - position k1,k2: both integers, size varies with j
    #%                   and l.
    #%               If is_real is 1, there are two types of curvelets,
    #%               'cosine' and 'sine'. For a given scale j, the 'cosine'
    #%               coefficients are stored in the first two quadrants (low
    #%               values of l), the 'sine' coefficients in the last two
    #%               quadrants (high values of l).      
    C = fdct_wrapping(x, is_real, finest, nbscales, nbangles_coarse)
    ANGLES = numpy.zeros((1,len(C)))
    for i in range(len(C)):
        ANGLES[0,i] = len(C[i]) #array([[  1.,  32.,   1.]])
        
    #% offsets of 4 directions of co-occurrence matrix: 0, 45, 90, 135 degree
    offset = numpy.array([[0,1],[-1,1],[-1,0],[-1,-1]])
    
    index = 1
    #% for every scale
    
    for i in range(len(C)):
        #% for every direction of curvelet in this scale
        for j in range(len(C[i])):
            #% calculate average co-occurrence matrix
            SI = preglcm(C[i][j],graylevel)
            #greycomatrix implemented by skimage ranges from 0~15,but SI ranges from 1~16
            #offset = [ 0 1;-1 1;-1 0;-1 -1 ];And the greycomatrix is weird,I tried it so many times.
            glcms = greycomatrix(SI - 1,[1],[0,numpy.pi*3/4,numpy.pi/4] ,levels=graylevel, symmetric=False, normed=False)
            glcm1 = glcms[:,:,0,0]
            glcm3 = glcms[:,:,0,1]
            glcm4 = glcms[:,:,0,2]
            glcm2 = greycomatrix(numpy.fliplr(SI) - 1,[1],[numpy.pi/4] ,levels=graylevel, symmetric=False, normed=False)[:,:,0,0]

            pass
    return C

if __name__ == "__main__":
    XX = misc.imread('test1.jpg')
    XX= XX[:,:,0] if XX.shape[2] > 1 else XX#if RGB,only tackle R
    
    ccf(XX)
    
    #Uncomment this if you want to know the time efficient of the program.
    #import cProfile
    #cProfile.run("ccf(XX)")
    