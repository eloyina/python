import cv
import math

def quantize(img, order):
	div = 255/order
	for i in range(img.rows):
		for j in range(img.cols):
			val = cv.Get2D(img, i, j)
			newval = (int(val[0]/div))*div
			#imprime el valor nuevo
			if newval>255:
				newval = 255-1
			cv.Set2D(img, i, j, (newval))
	cv.ShowImage("Quantize", img)
	cv.WaitKey(0)
	return img

def compute_glcm(img, d):
	order = 8
	newimg = quantize(img, order)
	glcm = cv.CreateMat(order,order,cv.CV_8UC1)
	normglcm = cv.CreateMat(order, order, cv.CV_32FC1)
	cv.SetZero(glcm)
	
	div = 255/order
	for i in range(img.rows-d):
		for j in range(img.cols-d):
			val1 = cv.Get2D(newimg, i, j)
			val2 = cv.Get2D(newimg, i+d, j+d)
			p = int(val1[0]/div)
			q = int(val2[0]/div)
			if p>=order:
				p = order -1
			if q>=order:
				q = order -1
			#print p, q
			val3 = cv.Get2D(glcm, p, q)
			cv.Set2D(glcm, p, q, (val3[0]+1))
			
	tot = cv.Sum(glcm)
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val3 = cv.Get2D(glcm, i , j)
			val = 1.0*val3[0]/tot[0]
			cv.Set2D(normglcm, i, j, (val))
			#print round(float(cv.Get2D(normglcm, i, j)[0]), 3), 
		#print "\n"
		
	return normglcm
	
def angmom(glcm):
	f1 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			f1 += val[0]**2
	print " ",f1
	return f1

def autosim (glcm):
	f7 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			
			f7 += val[0]
	print ";",f7	

def contrast(glcm):
	f2 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			f2 += ((i-j)**2)*val[0]
	print ";",f2

def homogeneity(glcm):
	f1 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			
			f1 += val[0]/(1+abs(i-j))
	print ";",f1

def alcuadrado(glcm):
	f5 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			
			f5 += val[0]/((1+abs(i-j)**2))
	print ";",f5

def def14(glcm):
	f5 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			
			f5 += (1/(1+(i-j)**2))*val[0]
	print ";",f5


def disimilitud(glcm):
	f6 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			
			f6 += val[0]*abs(i-j)
	print ";",f6

def entropy(glcm):
	f1 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			if val[0]==0:
				continue
			f1 += val[0]*math.log(val[0])/math.log(2)
	f1 = -f1
	print ";",f1

def sumentropy(glcm):
	f4 = 0
	for i in range(glcm.rows):
		for j in range(glcm.cols):
			val = cv.Get2D(glcm, i, j)
			if val[0]==0:
				continue
			f4 += val[0]*math.log(val[0])/math.log(2)
	f4 = -f4
	print ";",f4


	
name = raw_input("	ingrese images:")

img = cv.LoadImageM(name, 0)
newimg = cv.CreateMat(400, 400, img.type)
cv.Resize(img, newimg)
dist = int(raw_input("ingrese dist:"))

name = raw_input("ingrese images")

img1 = cv.LoadImageM(name, 0)
newimg1 = cv.CreateMat(400, 400, img1.type)
cv.Resize(img1, newimg1)
dist1 = int(raw_input("ingrese dist:"))

name = raw_input("ingrese images:")

img2 = cv.LoadImageM(name, 0)
newimg2 = cv.CreateMat(400, 400, img2.type)
cv.Resize(img2, newimg2)
dist2 = int(raw_input("ingrese dist:"))

name = raw_input("ingrese images:")

img3 = cv.LoadImageM(name, 0)
newimg3 = cv.CreateMat(400, 400, img.type)
cv.Resize(img3, newimg3)
dist3 = int(raw_input("ingrese distancia:"))

name = raw_input("ingrese images:")

img4 = cv.LoadImageM(name, 0)
newimg4 = cv.CreateMat(400, 400, img.type)
cv.Resize(img4, newimg4)
dist4 = int(raw_input("ingrese distancia:"))

normglcm = compute_glcm(newimg, dist)
angmom(normglcm)
contrast(normglcm)
entropy(normglcm)
homogeneity(normglcm)
alcuadrado(normglcm)
disimilitud(normglcm)
autosim(normglcm)
def14(normglcm)

normglcm = compute_glcm(newimg1, dist)
angmom(normglcm)
contrast(normglcm)
entropy(normglcm)
homogeneity(normglcm)
alcuadrado(normglcm)
disimilitud(normglcm)
autosim(normglcm)
def14(normglcm)

normglcm = compute_glcm(newimg2, dist)
angmom(normglcm)
contrast(normglcm)
entropy(normglcm)
homogeneity(normglcm)
alcuadrado(normglcm)
disimilitud(normglcm)
autosim(normglcm)
def14(normglcm)

normglcm = compute_glcm(newimg3, dist)
angmom(normglcm)
contrast(normglcm)
entropy(normglcm)
homogeneity(normglcm)
alcuadrado(normglcm)
disimilitud(normglcm)
autosim(normglcm)
def14(normglcm)

normglcm = compute_glcm(newimg4, dist)
angmom(normglcm)
contrast(normglcm)
entropy(normglcm)
homogeneity(normglcm)
alcuadrado(normglcm)
disimilitud(normglcm)
autosim(normglcm)
def14(normglcm)


#compute_glcm(img, dist)



