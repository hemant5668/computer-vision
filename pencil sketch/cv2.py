
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[36]:


#sketch generating function
def sketch(img):
    
    #converting to gray
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     
    #remove noice
    gray_blur=cv2.GaussianBlur(gray,(5,5),0)
    #seperate edges
    canny=cv2.Canny(gray_blur,-10,50)
    #sharp edges
    M=np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])
    sharp=cv2.filter2D(canny,-1,M)
    #do an invert binarise the image
    ret,mask=cv2.threshold(canny,70,255,cv2.THRESH_BINARY_INV)
    return mask

#intialise web cam
#it contains a boolean indicating if is successful(ret) 
#it also contains the images collected from web cam

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('live sketcher',sketch(frame))
    if cv2.waitKey(1)==13:                 #13 is the enter key
        break

#release camera
cap.release()
cv2.destroyAllWindows()    

