#Calculate the entropy of an image.
#By WangJZ 2013.9.8

import numpy
def calEntropy(I):
        '''
        E = ENTROPY(I) returns E, a scalar value representing the entropy of an
        intensity image.  Entropy is a statistical measure of randomness that can be
        used to characterize the texture of the input image.  Entropy is defined as
        -sum(p.*log2(p)) where p contains the histogram counts returned from IMHIST.
        '''   
        #Imitate im2uint8
        I = numpy.round(I *256)
        
        #% calculate histogram counts.range(256) is very important
        imhist,bins = numpy.histogram(I,bins = range(256))
        
        #% remove zero entries in hist
        imhist = imhist[imhist!=0]
        
        #% normalize p so that sum(p) is one.
        imhist = imhist.astype(numpy.float) / I.size
        E = -numpy.sum(imhist*numpy.log2(imhist))
        return E