import numpy

def calEntropy(I):
        I = numpy.round(I *256)#Imitate im2uint8
        imhist,bins = numpy.histogram(I,256,normed=True)
        imhist = numpy.round(imhist).astype(numpy.int)
        return imhist
