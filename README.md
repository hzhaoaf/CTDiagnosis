CTdiagnosis
===========

###What is it?
This is a software of lung cancer diagnosis.As part of a computer aided diagnosis(CAD) system, 
this software aims to assist doctocs make a diagnosis of lung cancer 
by analysing the Computed Tomography(CT) images.  

- Based on the technology of Digital Image Processing and Machine Learning,we calculate(predict) the probability 
of a person suffering from lung cancer.
- All CT images are firstly pre-processed and partitioned into regions via **Region growing** algorithm,
and then **Fast Discrete Curvelet Transforms**(FDCT) Algorithm is applied to extract the most 14 distinctive 
features from the pre-processed image. Finally the extracted features ,labels together with their 
corresponding patient's info are trained by **Support Vector Machine**(SVM).Once the Lung cancer model is established,
it could tell the probability of a patient suffering from lung cancer with his info and 
CT images sequence.With the increased use of this software the prediction accuracy is improved continuously.

###Technologies

- [PyQt](http://www.riverbankcomputing.co.uk/software/pyqt/download/) 
and [Installation Guide](http://blog.csdn.net/bookeezhou/article/details/6229011)
- scikit-learn [details on github](https://github.com/scikit-learn/scikit-learn)
- [numpy](http://www.numpy.org/)


###Special Thanks

Thanks for the project of [MP View](http://qt-apps.org/content/show.php/MP+View?content=68379),
we create our ImageViewer GUI based on that.
