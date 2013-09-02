# -*- coding: utf-8 -*- 
'''
% fdct_wrapping.m - Fast Discrete Curvelet Transform via wedge wrapping - Python
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
% By JZ 2013
'''
import math
import scipy,numpy
from numpy.fft import fft2,ifftshift,fftshift
from fdct_wrapping_window import fdct_wrapping_window

#numpy.set_printoptions(threshold='nan')

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
    M1 = N1/3.0;
    M2 = N2/3.0;
    
    if finest == 1:
        # Initialization: smooth periodic extension of high frequencies
        pass#I find that fineset is always 2
    
    else:
        M1 = M1/2.0
        M2 = M2/2.0     
        window_length_1 = math.floor(2*M1) - math.floor(M1) - 1
        window_length_2 = math.floor(2*M2) - math.floor(M2) - 1 
        coord_1 = numpy.arange(0,1+1.0/window_length_1,1.0/window_length_1)
        coord_2 = numpy.arange(0,1+1.0/window_length_2,1.0/window_length_2)
        wl_1,wr_1= fdct_wrapping_window(coord_1)
        wl_2,wr_2 = fdct_wrapping_window(coord_2)
        lowpass_1 = numpy.concatenate((wl_1 , numpy.ones(2*math.floor(M1)+1) , wr_1))
        lowpass_2 = numpy.concatenate((wl_2 , numpy.ones(2*math.floor(M2)+1) , wr_2))
        #transpose的操作依赖于shape参数,对于一维的shape,转置是不起作用的.
        lowpass_1 = lowpass_1.reshape(-1,1)#变成1-column vector
        lowpass_2 = lowpass_2.reshape(1,-1)#变成1-row vector
        lowpass = numpy.dot(lowpass_1,lowpass_2)
        hipass = numpy.sqrt(1.0 - lowpass**2)
        
        Xlow_index_1 = numpy.arange(-math.floor(2.0*M1),math.floor(2.0*M1)+1) + math.ceil((N1+1)/2.0)
        Xlow_index_1 = Xlow_index_1.astype(int) - 1#类型转换，不理解为什么arange函数不能设置类型
        Xlow_index_2 = numpy.arange(-math.floor(2.0*M2),math.floor(2.0*M2)+1) + math.ceil((N2+1)/2.0)
        Xlow_index_2 = Xlow_index_2.astype(int) - 1#-1 is necessary: matlab starts with 1 ,while python starts with 0
        Xlow = (X[ : , Xlow_index_2][Xlow_index_1, : ] ) * lowpass
        Xhi = X.copy()
        temp = Xhi[ : ,Xlow_index_2][Xlow_index_1, : ] * hipass
        
        #使用整数序列进行的下标索引和原数据不共享内存地址，所以……
        Xhi[ : ,Xlow_index_2[0]:Xlow_index_2[-1]+1][Xlow_index_1[0]:Xlow_index_1[-1]+1, : ] = temp
        
    return 0
    