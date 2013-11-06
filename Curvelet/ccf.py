# -*- coding: utf-8 -*-
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
#import matplotlib.pyplot as plt
from fdct_wrapping import *
from skimage.feature import greycomatrix
#from skimage.feature._tex
from preglcm import preglcm
from calEntropy import calEntropy

#Cx+y(k)
def cxpy(x):
    res = numpy.zeros((1,x.shape[0]+x.shape[1] - 1));
    for i in range(int(x.shape[0])):
        for j in range(int(x.shape[1])):
            res[0,i+j] += x[i,j]
    return res

#% Cx-y(k)
def cxmy(x):
    res = numpy.zeros((1,  max(x.shape[0],x.shape[1])  ))
    for i in range(int(x.shape[0])):
        for j in range(int(x.shape[1])):
            res[0,abs(i-j)] += x[i,j]
    return res

def inertia(x):
    ine = 0
    for i in range(int(x.shape[0])):
        for j in range(int(x.shape[1])):
            ine += x[i,j] * (i-j)**2
    return ine

# IDM - Inverse Difference Moment
def idm(x):
    res = 0
    for i in range(int(x.shape[0])):
        for j in range(int(x.shape[1])):
            res += x[i,j] /(1+ (i-j)**2)
    return res

def homogeneity(x):
    s = x.shape
    c,r = numpy.meshgrid(numpy.arange(1,s[0]+1),numpy.arange(1,s[1]+1))
    c = c.reshape(-1,1)
    r= r.reshape(-1,1)
    term1 = (1 + numpy.abs(r - c))
    term = x.reshape(-1,1) / term1
    hg = numpy.sum(term)
    return hg

def cluster_tendency(x):
    s = x.shape
    c,r = numpy.meshgrid(numpy.arange(1,s[0]+1),numpy.arange(1,s[1]+1))
    c = c.reshape(-1,1)
    r= r.reshape(-1,1)
    term1 = (1 + numpy.abs(r - c))
    term = x.reshape(-1,1) / term1
    hg = numpy.sum(term)
    
    mu= numpy.mean(x)*numpy.ones(x.shape)
    term1=(r+c-2*mu.reshape(-1,1))
    term = x.reshape(-1,1)* term1
    return(numpy.sum(term))

#In shell program,default value of nbangles_coarse is 8
#ccf( x, graylevel=16, is_real = 1, finest = 2, nbscales = 3, nbangles_coarse = 32)    
def ccf( x, graylevel=16, is_real = 1, finest = 2, nbscales = 3, nbangles_coarse = 8):
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
    
    MEAN,SD,ENG,INE,IDM,ENT,COR,SM,DM,SE,DE,CT,HG,MP= [],[],[],[],[],[],[],[],[],[],[],[],[],[]
    
    C = fdct_wrapping(x, is_real, finest, nbscales, nbangles_coarse)
    ANGLES = numpy.zeros((1,len(C)))
    for i in range(len(C)):
        ANGLES[0,i] = len(C[i]) #array([[  1.,  32.,   1.]])
        
    #% offsets of 4 directions of co-occurrence matrix: 0, 45, 90, 135 degree
    offset = numpy.array([[0,1],[-1,1],[-1,0],[-1,-1]])
    
    #index = 1#since we use append to MEAN,SD,ENG...， index is useless
    #% for every scale
    
    
    for i in range(len(C)):
        #% for every direction of curvelet in this scale
        for j in range(len(C[i])):
            #% calculate average co-occurrence matrix
            SI = preglcm(C[i][j],graylevel)
            #greycomatrix implemented by skimage ranges from 0~15,but SI ranges from 1~16
            #offset = [ 0 1;-1 1;-1 0;-1 -1 ];And the greycomatrix is weird,I tried it so many times.
            glcms = greycomatrix(SI - 1,[1],[0,numpy.pi*3/4,numpy.pi/4] ,levels=graylevel, symmetric=False, normed=False)
            glcm1 = glcms[:,:,0,0].astype(numpy.float)
            glcm3 = numpy.transpose(glcms[:,:,0,1]).astype(numpy.float)
            glcm4 = numpy.transpose(glcms[:,:,0,2]).astype(numpy.float)
            glcm2 = greycomatrix(numpy.fliplr(SI) - 1,[1],[numpy.pi/4] ,levels=graylevel, symmetric=False, normed=False)[:,:,0,0]
            glcm2 = numpy.transpose(glcm2).astype(numpy.float)
            
            MEAN.append(numpy.mean(SI))
            SD.append(numpy.std(SI,ddof = 1))#bug fix, use n-1 as "degree of freedom", because matlab use that!
            (M,N) = SI.shape
            p = [M*(N-1),(M-1)*(N-1),(M-1)*N,(M-1)*(N-1)]
            glcm=0.25*(glcm1/p[0]+glcm2/p[1]+glcm3/p[2]+glcm4/p[3])
            #% maginal distribution
            Cx = numpy.sum(glcm, axis=1)
            Cy = numpy.sum(glcm, axis=0)

            #% mean of maginal distribution
            ux = numpy.sum(numpy.arange(0,Cx.size) * Cx)
            uy = numpy.sum(numpy.arange(0,Cy.size) * Cy)
            
            #% standard deviation of maginal distribution
            deltax ,deltay = 0,0
            for k in range(int(Cx.size)):
                deltax += (k - ux)**2 * Cx[k]
                deltay += (k - uy)**2 * Cy[k]
            deltax = deltax**0.5
            deltay = deltay**0.5
            
            Cxpy = cxpy(glcm)   #% Cx+y(k)
            Cxmy = cxmy(glcm)    #% Cx-y(k)
            
            ENG.append(numpy.sum(glcm * glcm))#% Energy
            INE.append(inertia(glcm))#% Inertia
            IDM.append(idm(glcm))#% Inverse Difference Moment
            ENT.append(calEntropy(glcm))#% Entropy
            
            #% Correlation
            if (deltax * deltay) <= pow(10,-6):
                COR.append(0)#Set to 0 temp
            else:
                COR.append(\
                    (numpy.sum(numpy.sum(numpy.dot(numpy.dot(
                        numpy.diag(numpy.arange(0,glcm.shape[0])) , glcm) , numpy.diag(numpy.arange(0,glcm.shape[1]))
                        ))-ux * uy)) \
                    / (deltax * deltay) )
            SM.append(numpy.sum(numpy.arange(0,Cxpy.shape[1]) * Cxpy))#% Sum-mean
            DM.append(numpy.sum(numpy.arange(0,Cxmy.shape[1]) * Cxmy))#% Difference-mean
            SE.append(calEntropy(Cxpy))
            DE.append(calEntropy(Cxmy))
            CT.append(cluster_tendency(glcm))
            HG.append(homogeneity(glcm))
            MP.append(numpy.max(glcm))
            #index += 1
    return [MEAN,SD,CT,HG,MP,ENG,INE,IDM,ENT,COR,SM,DM,SE,DE,ANGLES]



if __name__ == "__main__":
    #XX = misc.imread('../data/images/result_7.bmp')
    XX = misc.imread('result_2.bmp')
    #result_7.bmp
    #path = u'C:\\Users\\Charles\\Desktop\\dcmProgram\\\u75c5\u4f8b\\\u826f\u6027\\zhang zhuo yang\\\u8f74\\result_10.bmp'
    #XX = misc.imread(path)
    #If it's a gray image, shape of XX would be 2d ,sth like (73,63)
    if len(XX.shape) == 2:
        pass
    else:
        XX= XX[:,:,0] if XX.shape[2] > 1 else XX#if RGB,only tackle R
    [MEAN,SD,CT,HG,MP,ENG,INE,IDM,ENT,COR,SM,DM,SE,DE,ANGLES] = ccf(XX)
    print([MEAN,SD,CT,HG,MP,ENG,INE,IDM,ENT,COR,SM,DM,SE,DE,ANGLES])
    
    #Uncomment this if you want to know the time efficient of the program.
    #import cProfile
    #cProfile.run("ccf(XX)")
    