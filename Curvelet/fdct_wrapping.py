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
from numpy.fft import fft2,ifftshift,fftshift,ifft2
from fdct_wrapping_window import fdct_wrapping_window
from memory_profiler import profile

#@profile
numpy.set_printoptions(threshold='nan',linewidth='nan')
def  fdct_wrapping(x, is_real , finest, nbscales, nbangles_coarse):
    print(math.sqrt(x.size))
    X = fftshift(fft2((ifftshift(x))))/(math.sqrt(x.size)) #fft2 transform
    N1,N2 = X.shape
    
    #------------Initialization: data structure-------------
    
    #numpy.arrange类似于python的range：起始，终值，步长来创建数组，注意数组不包括终值
    tempCeil = numpy.ceil( (nbscales - numpy.arange(nbscales,2-1,-1) )  / 2.0 )
    nbangles = numpy.insert(nbangles_coarse*2**tempCeil,0,1.0)
    if finest == 2 : nbangles[nbscales - 1]= 1
    
    # initialize C,C is a python list ,like cells of matlab
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
        coord_1 = numpy.linspace(0, 1, window_length_1 + 1)#numpy.linspace(start, stop, num=50, endpoint=True, retstep=False)
        coord_2 = numpy.linspace(0, 1, window_length_2 + 1)
        #if You write the code below , there maybe occur an error 
        #coord_2 = numpy.arange(0,1+1.0/window_length_2,1.0/window_length_2)
        #Document says ->End of interval does not include this value, 
        #except in some cases where step is not an integer and floating point round-off affects the length of out.
        
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
        
        #使用整数序列进行的下标索引和原数据不共享内存地址，所以……
        Xhi[ : ,Xlow_index_2[0]:Xlow_index_2[-1]+1][Xlow_index_1[0]:Xlow_index_1[-1]+1, : ] = Xhi[ : ,Xlow_index_2][Xlow_index_1, : ] * hipass
        C[nbscales-1][0] = fftshift(ifft2((ifftshift(Xhi)))) * (math.sqrt(Xhi.size)) #ifft2 transform
        if is_real: C[nbscales-1][0]  = numpy.real(C[nbscales-1][0] )
    for j in range(nbscales - 1,2-1,-1):
        M1 = M1 / 2.0
        M2 = M2 / 2.0
        window_length_1 = math.floor(2.0 * M1) - math.floor(M1) - 1
        window_length_2 = math.floor(2.0 * M2) - math.floor(M2) - 1
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
        
        Xhi = Xlow.copy()#% size is 2*floor(4*M1)+1 - by - 2*floor(4*M2)+1
        #matlab Xlow_index_1 is [18,19,...,50] but here [17,18,...,49]
        Xlow_index_1 = numpy.arange(-math.floor(2.0 * M1),math.floor(2.0 * M1) + 1) + math.floor(4.0 * M1)
        Xlow_index_1 = Xlow_index_1.astype(int)#类型转换，不理解为什么arange函数不能设置类型
        Xlow_index_2 = numpy.arange(-math.floor(2.0 * M2),math.floor(2.0 * M2) + 1) + math.floor(4.0 * M2)
        Xlow_index_2 = Xlow_index_2.astype(int)#-1 is not necessary here: because we pretend miss +1 at the fomer line
        Xlow = Xlow[ : , Xlow_index_2][Xlow_index_1, : ]
        Xhi[ : ,Xlow_index_2[0]:Xlow_index_2[-1]+1][Xlow_index_1[0]:Xlow_index_1[-1]+1, : ] = Xlow * hipass
        Xlow = Xlow * lowpass #% size is 2*floor(2*M1)+1 - by - 2*floor(2*M2)+1
        
        #% Loop: angular decomposition
        lll = 0
        nbquadrants = 2 + 2 *( not is_real )
        nbangles_perquad = int(nbangles[j-1] / 4.0)
        for quadrant in range(1,nbquadrants+1):
            M_horiz = M2 * ((quadrant % 2)==1) + M1 * ((quadrant % 2)==0);
            M_vert = M1 * ((quadrant % 2)==1) + M2 * ((quadrant % 2)==0);                
            if nbangles_perquad % 2 == 0:
                step = 1.0/(2.0*nbangles_perquad)
                wedge_ticks_left = numpy.round(numpy.arange(0,0.5+step,step) * 2 * math.floor(4.0 * M_horiz) + 1)
                wedge_ticks_right = 2.0 * math.floor(4.0 * M_horiz) + 2 - wedge_ticks_left
                wedge_ticks = numpy.concatenate((wedge_ticks_left,wedge_ticks_right[-2::-1]))#从倒数第二个数依次向前
            else:
                step = 1.0/(2.0*nbangles_perquad)
                wedge_ticks_left = numpy.round(numpy.arange(0,0.5+step,step) * 2 * math.floor(4.0 * M_horiz) + 1)
                wedge_ticks_right = 2.0 * math.floor(4.0 * M_horiz) + 2 - wedge_ticks_left
                wedge_ticks = numpy.concatenate((wedge_ticks_left,wedge_ticks_right[-1::-1]))#从倒数第一个数依次向前
            wedge_endpoints = wedge_ticks[1:-1:2] #%integers
            wedge_midpoints = (wedge_endpoints[0:-1] + wedge_endpoints[1:] ) / 2.0 #% integers or half-integers
            #% Left corner wedge
            lll+=1
            first_wedge_endpoint_vert = round(2.0 * math.floor(4.0 * M_vert) / (2.0 * nbangles_perquad) + 1)
            length_corner_wedge = math.floor(4.0 * M_vert) - math.floor(M_vert) + math.ceil(first_wedge_endpoint_vert / 4.0)
            Y_corner = numpy.arange(1,length_corner_wedge + 1)
            XX,YY = numpy.meshgrid(numpy.arange(1,(2 * math.floor(4.0 * M_horiz) + 2)) ,Y_corner)
            width_wedge = wedge_endpoints[1] + wedge_endpoints[0] - 1
            slope_wedge = (math.floor(4.0 * M_horiz) + 1 - wedge_endpoints[0]) / math.floor(4.0 * M_vert)
            left_line = numpy.round(2 - wedge_endpoints[0] + slope_wedge * (Y_corner - 1))#% integers                
            wrapped_data = numpy.zeros((length_corner_wedge,width_wedge))
            wrapped_data = wrapped_data.astype(numpy.complex)
            #if not convert data type,->ComplexWarning: Casting complex values to real discards the imaginary part
            
            wrapped_XX = numpy.zeros((length_corner_wedge,width_wedge))
            wrapped_YY = numpy.zeros((length_corner_wedge,width_wedge))
            first_row = math.floor(4.0 * M_vert) + 2 - math.ceil((length_corner_wedge + 1) / 2) + \
                ((length_corner_wedge+1) % 2) * ((quadrant-2) == (quadrant-2) % 2)                
            first_col = math.floor(4.0 * M_horiz) + 2 - math.ceil((width_wedge + 1) / 2) + \
                ((width_wedge+1) % 2) * ((quadrant-3) == (quadrant-3)%2)
            #% Coordinates of the top-left corner of the wedge wrapped
            #% around the origin. Some subtleties when the wedge is
            #% even-sized because of the forthcoming 90 degrees rotation               
            for row in Y_corner:
                cols = left_line[int(row) - 1] + numpy.mod((numpy.arange(0,width_wedge) -  (left_line[int(row) - 1] - first_col)  ),width_wedge)
                admissible_cols = numpy.round(1.0 / 2.0 * (cols + 1 + numpy.abs(cols - 1)))
                admissible_cols = admissible_cols.astype(int) - 1#类型转换
                new_row = 1 + (row - first_row) %  length_corner_wedge
                wrapped_data[new_row - 1, : ] = Xhi[row - 1,admissible_cols] * (cols > 0)#all zero?
                
                wrapped_XX[new_row - 1,:] = XX[row - 1,admissible_cols]#Needn't to copy,yeah? yeah!
                wrapped_YY[new_row - 1,:] = YY[row - 1,admissible_cols]
                
            slope_wedge_right = (math.floor(4.0 * M_horiz) + 1 - wedge_midpoints[0] ) / math.floor(4.0 * M_vert)
            mid_line_right = wedge_midpoints[0] + slope_wedge_right * (wrapped_YY - 1)#% not integers in general
            coord_right = 0.5 + math.floor(4.0 * M_vert) / (wedge_endpoints[1] - wedge_endpoints[0]) * \
                (wrapped_XX - mid_line_right) / (math.floor(4.0 * M_vert) + 1 - wrapped_YY)
            C2 = 1.0 / (1.0 / (2.0 * math.floor(4.0 * M_horiz) / (wedge_endpoints[0] - 1) - 1) + \
                        1.0 / (2.0 * math.floor(4 * M_vert) / (first_wedge_endpoint_vert - 1) - 1))
            C1 = C2 / (2.0 * math.floor(4.0 * M_vert) / (first_wedge_endpoint_vert - 1) - 1)
            #用布尔数组索引数组，会改变原数组的值，但是文章中提到用这种方式不共享内存，矛盾！
            wrapped_XX[(wrapped_XX - 1) / math.floor(4.0 * M_horiz) +  (wrapped_YY-1) / math.floor(4 * M_vert) ==2 ] = \
                wrapped_XX[(wrapped_XX - 1) / math.floor(4.0 * M_horiz) + (wrapped_YY - 1) / math.floor(4.0 * M_vert) == 2] + 1
            coord_corner = C1 + C2 * ((wrapped_XX - 1) / math.floor(4.0 * M_horiz) - (wrapped_YY - 1) / math.floor(4.0 * M_vert)) / \
                (2 - ((wrapped_XX - 1)/math.floor(4.0 * M_horiz) + (wrapped_YY - 1) / math.floor(4.0 * M_vert)))
            wl_left = fdct_wrapping_window(coord_corner)[0]#returns tuple and we need the first item
            wl_right,wr_right = fdct_wrapping_window(coord_right)
            wrapped_data = wrapped_data * (wl_left * wr_right)
            if is_real:
                wrapped_data = numpy.rot90(wrapped_data,-(quadrant - 1))
                x = fftshift(ifft2(ifftshift(wrapped_data))) * math.sqrt(wrapped_data.size)
                C[j - 1][lll - 1] = math.sqrt(2) * numpy.real(x)
                C[j - 1][int(lll+nbangles[j - 1] / 2 - 1)] = math.sqrt(2) * numpy.imag(x)
            else:
                wrapped_data = numpy.rot90(wrapped_data,-(quadrant - 1))
                C[j - 1][lll - 1] = fftshift(ifft2(ifftshift(wrapped_data))) * math.sqrt(wrapped_data.size)
            #% Regular wedges
            length_wedge = math.floor(4*M_vert) - math.floor(M_vert)
            Y = numpy.arange(1,length_wedge + 1)
            first_row = math.floor(4.0 * M_vert) + 2 - math.ceil((length_wedge + 1) / 2.0) + \
                ((length_wedge+1) % 2) * (quadrant-2 == ((quadrant-2) % 2))            
            for subl in range(2,nbangles_perquad):
                lll += 1
                width_wedge = wedge_endpoints[subl] - wedge_endpoints[subl-2] + 1
                
                slope_wedge = ((math.floor(4.0 * M_horiz) + 1) - wedge_endpoints[subl - 1])/math.floor(4.0 * M_vert)
                left_line = numpy.round(wedge_endpoints[subl-2] + slope_wedge * (Y - 1))
                wrapped_data = numpy.zeros((length_wedge,width_wedge),dtype=numpy.complex)
                #wrapped_data = wrapped_data.astype(numpy.complex)
                wrapped_XX = numpy.zeros((length_wedge,width_wedge))
                wrapped_YY = numpy.zeros((length_wedge,width_wedge))
                first_col = math.floor(4.0 * M_horiz)+2-math.ceil((width_wedge+1) / 2.0) + \
                    ((width_wedge+1) % 2) * (quadrant-3 == ((quadrant-3) % 2))
                for row in Y:
                    row = int(row)
                    cols = left_line[row - 1] + numpy.mod(numpy.arange(0,width_wedge)-(left_line[row-1]-first_col) , width_wedge)
                    cols = cols.astype(int)
                    new_row = int((row - first_row)  % length_wedge)
                    wrapped_data[new_row,:] = Xhi[row - 1,cols-1]
                    wrapped_XX[new_row,:] = XX[row - 1,cols - 1]
                    wrapped_YY[new_row,:] = YY[row - 1,cols - 1]
                slope_wedge_left = ((math.floor(4.0 * M_horiz)+1) - wedge_midpoints[subl-2]) / math.floor(4.0 * M_vert)
                mid_line_left = wedge_midpoints[subl-2] + slope_wedge_left * (wrapped_YY - 1)
                coord_left = 0.5+ math.floor(4.0 * M_vert)/(wedge_endpoints[subl - 1] - wedge_endpoints[subl - 2]) * \
                    (wrapped_XX - mid_line_left) / (math.floor(4.0 * M_vert)+1 - wrapped_YY)
                slope_wedge_right = ((math.floor(4.0 * M_horiz)+1) - wedge_midpoints[subl - 1]) / math.floor(4.0 * M_vert)
                mid_line_right = wedge_midpoints[subl - 1] + slope_wedge_right * (wrapped_YY - 1)
                
                coord_right = 0.5 + math.floor(4.0 * M_vert)/(wedge_endpoints[subl] - wedge_endpoints[subl - 1]) * \
                    (wrapped_XX - mid_line_right) / (math.floor(4.0 * M_vert)+1 - wrapped_YY)
                wl_left = fdct_wrapping_window(coord_left)[0]
                wl_right , wr_right = fdct_wrapping_window(coord_right)
                wrapped_data = wrapped_data * (wl_left * wr_right)
                if is_real:
                    wrapped_data = numpy.rot90(wrapped_data,-(quadrant-1))
                    x = fftshift(ifft2(ifftshift(wrapped_data))) * math.sqrt(wrapped_data.size)
                    C[j - 1][lll - 1] = math.sqrt(2) * numpy.real(x)
                    C[j - 1][int(lll+nbangles[j - 1] / 2 - 1)] = math.sqrt(2) * numpy.imag(x)
                else:
                    wrapped_data = numpy.rot90(wrapped_data,-(quadrant-1))
                    C[j - 1][lll - 1] = fftshift(ifft2(ifftshift(wrapped_data))) * math.sqrt(wrapped_data.size)
                    
            #% Right corner wedge
            lll += 1
            width_wedge = 4 * math.floor(4.0 * M_horiz) + 3 - wedge_endpoints[-1] - wedge_endpoints[-2]
            slope_wedge = ((math.floor(4.0 * M_horiz) + 1) - wedge_endpoints[-1])/math.floor(4.0 * M_vert)
            left_line = numpy.round(wedge_endpoints[-2] + slope_wedge * (Y_corner - 1))

            wrapped_data = numpy.zeros((length_corner_wedge,width_wedge),dtype=numpy.complex)
            wrapped_XX = numpy.zeros((length_corner_wedge,width_wedge))
            wrapped_YY = numpy.zeros((length_corner_wedge,width_wedge))
            first_row = math.floor(4.0 * M_vert)+2-math.ceil((length_corner_wedge+1) / 2.0) + \
                ((length_corner_wedge+1) % 2) * (quadrant-2 == ((quadrant-2) % 2))
            first_col = math.floor(4.0 * M_horiz)+2-math.ceil((width_wedge+1) / 2.0) + \
                ((width_wedge+1) % 2) * (quadrant-3 == ((quadrant-3) % 2))
            
            for row in Y_corner:
                cols = left_line[int(row) - 1] + numpy.mod((numpy.arange(0,width_wedge) -  (left_line[int(row) - 1] - first_col)  ),width_wedge)
                admissible_cols = numpy.round(1.0 / 2.0 * (cols + 2*math.floor(4.0*M_horiz) + \
                                                           1 - numpy.abs(cols - (2 * math.floor(4 * M_horiz)+1))))
                admissible_cols = admissible_cols.astype(int) - 1#类型转换
                new_row = 1 + (row - first_row) %  length_corner_wedge
                wrapped_data[new_row - 1, : ] = Xhi[row - 1,admissible_cols] * (cols <= (2 * math.floor(4 * M_horiz) + 1))
                wrapped_XX[new_row - 1,:] = XX[row - 1,admissible_cols]#Needn't to copy,yeah? yeah!
                wrapped_YY[new_row - 1,:] = YY[row - 1,admissible_cols]
            slope_wedge_left = ((math.floor(4.0 * M_horiz)+1) - wedge_midpoints[-1])/math.floor(4.0 * M_vert)
            mid_line_left = wedge_midpoints[-1] + slope_wedge_left * (wrapped_YY - 1)
            coord_left = 0.5 + math.floor(4.0 * M_vert) / (wedge_endpoints[-1] - wedge_endpoints[-2]) * \
                (wrapped_XX - mid_line_left) / (math.floor(4.0 * M_vert) + 1 - wrapped_YY)
            C2 = -1.0 / (2.0 * math.floor(4.0 * M_horiz) / (wedge_endpoints[-1] - 1) - 1 + \
                         1.0 / (2.0 * math.floor(4 * M_vert) / (first_wedge_endpoint_vert - 1) - 1))                
            C1 = -C2 * (2.0 * math.floor(4.0 * M_horiz) / (wedge_endpoints[-1] - 1) - 1)
            wrapped_XX[(wrapped_XX - 1) / math.floor(4.0 * M_horiz) ==  (wrapped_YY-1) / math.floor(4 * M_vert)] = \
                wrapped_XX[(wrapped_XX - 1) / math.floor(4.0 * M_horiz) == (wrapped_YY - 1) / math.floor(4.0 * M_vert)] - 1
            coord_corner = C1 + C2 * (2 - ((wrapped_XX - 1) / math.floor(4.0 * M_horiz) + (wrapped_YY - 1) / math.floor(4.0 * M_vert))) / \
                (((wrapped_XX - 1)/math.floor(4.0 * M_horiz) - (wrapped_YY - 1) / math.floor(4.0 * M_vert)))
            
            wl_left = fdct_wrapping_window(coord_left)[0]#returns tuple and we need the first item                
            wl_right,wr_right = fdct_wrapping_window(coord_corner)
            wrapped_data = wrapped_data * (wl_left * wr_right)
            if is_real:
                wrapped_data = numpy.rot90(wrapped_data,-(quadrant-1))
                x = fftshift(ifft2(ifftshift(wrapped_data))) * math.sqrt(wrapped_data.size)
                C[j - 1][lll - 1] = math.sqrt(2) * numpy.real(x)
                C[j - 1][int(lll+nbangles[j - 1] / 2 - 1)] = math.sqrt(2) * numpy.imag(x)
            else:
                wrapped_data = numpy.rot90(wrapped_data,-(quadrant-1))
                C[j - 1][lll - 1] = fftshift(ifft2(ifftshift(wrapped_data))) * math.sqrt(wrapped_data.size)
            if quadrant < nbquadrants : Xhi = numpy.rot90(Xhi)
    #% Coarsest wavelet level
    C[0][0] = fftshift(ifft2(ifftshift(Xlow))) * math.sqrt(Xlow.size)
    if is_real == 1 : C[0][0]= numpy.real(C[0][0])#seems Real is correct but image is not
    return C