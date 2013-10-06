
import numpy

#preprocess with GRAYCOMATRIX Create gray-level co-occurrence matrix.
#WangJZ 2013.9.5

def preglcm(I,NL):
        #% Scale I so that it contains integers between 1 and NL.
        if I.max()-I.min() <= pow(10,-6):
                return numpy.ones(I.shape)
        else:
                minN = I.min()
                maxN = I.max()
                slope = (NL-1) / (maxN- minN)
                intercept = 1 - (slope*(minN))
                SI = numpy.round(slope * I + intercept).astype(numpy.int)
                return SI