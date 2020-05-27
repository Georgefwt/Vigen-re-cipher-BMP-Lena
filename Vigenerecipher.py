from cv2 import cv2
import numpy as np

img=cv2.imread(r"lena512.bmp",0)
(height,width)=img.shape
#保证宽度为16的倍数
if (width%16)!=0:
    appendnum=16-width%16
    aplist=np.zeros((height,appendnum))
    img=np.append(img,aplist,axis=1)
    img=img.astype(np.int)
    width+=appendnum

keyoffsetlist=[121,43,123,32,23,13,242,45,91,40,132,81,48,10,19,188]

keylength=len(keyoffsetlist)
print(keyoffsetlist)
count=0
for i in range(width):
    for j in range(height):
        img[i][j]=(img[i][j]+keyoffsetlist[count])%256
        count+=1
        if count==16:
            count=0

cv2.imwrite(r"lennaresult.bmp",img)
