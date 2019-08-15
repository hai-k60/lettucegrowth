import cv2
import numpy as np 

lowerBound=np.array([25,86,6])
upperBound=np.array([54,255,255])

img= cv2.imread('big.jpg',1)
imgHSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask=cv2.inRange(imgHSV,lowerBound,upperBound)
numpixel=cv2.countNonZero(mask)
print("numpixel mask: "+str(numpixel))
print(mask.size)
print(mask.shape)

kernelOpen=np.ones((5,5))
# kernelMiddle=np.ones((14,14))
# kernelClose=np.ones((16,16))

maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
# maskMiddle=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelMiddle)
# maskClose=cv2.morphologyEx(maskMiddle,cv2.MORPH_CLOSE,kernelClose)


# maskFinal=maskClose
conts,h=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img,conts,-1,(0,0,255),2)

cv2.fillPoly(maskOpen,pts=conts, color=(255,255,255))  
print('numpixel maskopen'+str(cv2.countNonZero(maskOpen)))

for i in range(len(conts)):
    x,y,w,h=cv2.boundingRect(conts[i])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 2)
    

cv2.imshow('mask',mask)
#cv2.imshow('maskClose',maskClose)
#cv2.imshow('maskMiddle',maskMiddle)
cv2.imshow('maskOpen',maskOpen)
cv2.imshow('image',img)
#cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()