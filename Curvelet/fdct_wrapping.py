# -*- coding: utf-8 -*- 

'''
% fdct_wrapping.m - Fast Discrete Curvelet Transform via wedge wrapping - Version 1.0
%
% Inputs
%   x           M-by-N matrix
%
% Optional Inputs
%   is_real     Type of the transform
%                   0: complex-valued curvelets
%                   1: real-valued curvelets
%               [default set to 0]
%   finest      Chooses one of two possibilities for the coefficients at the
%               finest level:
%                   1: curvelets
%                   2: wavelets
%               [default set to 2]
%   nbscales    number of scales including the coarsest wavelet level
%               [default set to ceil(log2(min(M,N)) - 3)]
%   nbangles_coarse
%               number of angles at the 2nd coarsest level, minimum 8,
%               must be a multiple of 4. [default set to 16]
%
% Outputs
%   C           Cell array of curvelet coefficients.
%               C{j}{l}(k1,k2) is the coefficient at
%                   - scale j: integer, from finest to coarsest scale,
%                   - angle l: integer, starts at the top-left corner and
%                   increases clockwise,
%                   - position k1,k2: both integers, size varies with j
%                   and l.
%               If is_real is 1, there are two types of curvelets,
%               'cosine' and 'sine'. For a given scale j, the 'cosine'
%               coefficients are stored in the first two quadrants (low
%               values of l), the 'sine' coefficients in the last two
%               quadrants (high values of l).  
%
% See also ifdct_wrapping.m, fdct_wrapping_param.m
%
% By Laurent Demanet, 2004
'''
import math
import scipy,numpy
from numpy.fft import fft2,ifftshift,fftshift

def  fdct_wrapping(x, is_real , finest, nbscales, nbangles_coarse):
    print(math.sqrt(x.size))
    X = fftshift(fft2((ifftshift(x))))/(math.sqrt(x.size)) #fft2 transform
    N1,N2 = X.shape
    
    #------------Initialization: data structure-------------
    
    #numpy.arrange类似于python的range：起始，终值，步长来创建数组，注意数组不包括终值
    tempCeil = numpy.ceil( (nbscales - numpy.arange(nbscales,2-1,-1) )  / 2.0 )
    nbangles = numpy.insert(nbangles_coarse*2**tempCeil,0,1.0)
    if finest == 2 : nbangles[nbscales - 1]= 1
    
    # initialize C
    C = [[] for i in range(nbscales)] 
    for j in range(nbscales):
        C[j] = [[] for i in range(int(nbangles[j]))]
        
    # Loop: pyramidal scale decompositions
    M1 = N1/3;
    M2 = N2/3;        
    return 0
    