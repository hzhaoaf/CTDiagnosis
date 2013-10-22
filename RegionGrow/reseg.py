# -*- coding: utf-8 -*-
import numpy as np
import math
from scipy import misc

#Since PyInstaller seems doesn't support matplot, comment them first 
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#def showImg(img):
	#'''
	#Create a figure displaying the image
	#'''
	#plt.imshow(img,cmap=cm.gray)
	#plt.show()   

class RegionGrow():
	def __init__(self,I=None,position=None):
		self._I = I
		self._p = position
		self.threshold = 60
		
	def boundshr(self,I):
		'''
		Make Bound shringe to the image
		'''
		(m,n)=I.shape
		return I[1:m-1,1:n-1].copy()

	def boundaryExpand(self,Image):
		pass
	
	def nor1(self,X):
		'''
		Normalize an image
		'''
		#if X.dtype == np.dtype('uint8'):
			#return X
		if X.max()<= pow(10,-6):
			print("All points are black,fail.")
			return None
		Y=np.double(X) / float(X.max()) * 255.0
		return Y
		
	def getRegionGrowImage(self,I,position):
		self._I = I
		self._p = position
		return self._region_gorw(self._I,self._p)
		
	def boundex(self,I):
		(m,n)=I.shape
		result = np.zeros((m+2,n+2))
		result[1:m+1,1:n+1]=I.copy()
		
		result[1:m,0] =2 * self.threshold #* np.ones((m-1,1)) #+result[1:m,0]
		result[1:m,n+1]=2 * self.threshold #* np.ones((m-1,1)) #+ result[1:m,m+1]
		result[0,1:n] = 2 * self.threshold #* np.ones((1,n-1)) #+ result[0,1:n] 
		result[m+1,1:n] = 2 * self.threshold #* np.ones((1,n-1)) #+ result[m+1,1:n]
		return result
		
	def _region_gorw(self,I,position):
		'''
		Region Growing Algorithm
		I : input image
		position: selected seed position
		'''
		assert len(I.shape) == 2
		Itermax=500000
		threshold=self.threshold#%输入阈值，1~255之间的整数
		flag=1#%have taken the pixel?
		I=self.nor1(I)
		boundexI = self.boundex(I)
		#I = norshow(boundexI)
		I=boundexI/np.max(boundexI)*255
		
		print(I.shape)
		print(I[0,1])
		I1 = np.zeros(I.shape)

		xp,yp = 0,0
		if flag:
			#Change the pos because we use diff coordinate system
			xp = round(position[1])
			yp = round(position[0])
			flag = 0
		seedrec=[xp,yp]
		seed = I[xp,yp]
		seedsum=seed
		seednum=1
		go=np.array([[-1,0],[0,-1],[1,0],[0,1]])#%directer
		#region growing
		# |0  not scaned yet
		# |1  scaned and accepted
		# |2  grown seed
		# global seed I1 I seedsum seednum xp1 yp1 seedrec
		Iter=0
		while seedrec:
			if Iter>Itermax:
				break
			xp=seedrec[0]
			yp=seedrec[1]
			del seedrec[0]
			del seedrec[0]
			I1[xp,yp]=2
			for i in range(4):
				xp1=xp+go[i,0]
				yp1=yp+go[i,1]
				#if out of bounds,continue to next iteration
				if  xp1>=I.shape[0] or xp1<0 or yp1 >= I.shape[1] or yp1 <0:
					continue
				
				
				if I1[xp1,yp1]==0:
					b=I[xp1,yp1]
					t = abs(seed-b)
					if t<=threshold:
						I1[xp1,yp1]=1
						seedsum=float(seedsum+I[xp1,yp1])
						seednum=seednum+1
						seedrec.append(xp1)
						seedrec.append(yp1)
			seed = float(seedsum / seednum)
			Iter += 1
			
		I1=self.boundshr(I1)
		I=self.boundshr(I)
		I1=self.nor1(I1)
		#xm,ym,nm=0,0,0
		#for i in range(m):
			#for j in range(n):
				#if I1[i,j]>0:
					#xm+=i
					#ym+=j
					#nm+=1
		II = np.round((I1/255.0)*I)
		II.astype('uint8')
		return II
		#showImg(II)
		
if __name__ == "__main__":
	SELECTEDPOINT= (139,149)
	img = misc.imread('3.bmp')
	if not len(img.shape) == 2:
		img= img[:,:,0] if img.shape[2] > 1 else img
	
	rg = RegionGrow()
	img = rg.getRegionGrowImage(img,SELECTEDPOINT)
	#showImg(img)
	#region_gorw(img,SELECTEDPOINT)