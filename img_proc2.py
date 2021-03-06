import cv2
import math
import numpy as np 

PI = np.pi
PATH_IMAGE = "images/img1.jpg"
INNER_RADIUS_RATIO = 0.2

#Find the corresponding fisheye outpout point corresponding to an input cartesian point
def findFisheye(Xe,Ye,Rr1,Rr2,Cfx,Cfy,He,We):
    #fisheyePoint = {}
    #theta, r, Xf, Yf; Polar coordinates

    r = Ye/He*(Rr1-Rr2)+Rr2
    theta = Xe/We*2.0*PI
    Xf = Cfx+r*math.sin(theta)
    Yf = Cfy+r*math.cos(theta)
    fisheyePoint = (Yf,Xf)

    return fisheyePoint

def findEquirectangularImage(FishEyeImage):
    Hf = FishEyeImage.shape[0]
    Wf = FishEyeImage.shape[1]
    Rr1 = Hf/2 #The fisheye image is a square of 1400x1400 pixels containing a circle so the radius is half of the width or height size
    Rr2 = MOH_FACTOR*Rr1
    Cfx = Wf/2 #The fisheye image is a square so the center in x is located at half the distance of the width
    Cfy = Hf/2 #The fisheye image is a square so the center in y is located at half the distance of the height

    He = int((Rr1-Rr2))
    We = int(2*PI*((Rr1+Rr2)/2))

    equirectangularImage = np.zeros((He, We, 3), dtype=np.uint8);

    for Ye in range(He):
     for Xe in range(We):
        try:
            ij = findFisheye(Xe, Ye, Rr1, Rr2, Cfx, Cfy, He, We)
            equirectangularImage[Ye,Xe] = FishEyeImage[int(ij[0]),int(ij[1])]
        except :
            pass
    
    return equirectangularImage

fisheye_Image = cv2.imread(PATH_IMAGE)
 
cv2.imwrite('images/equirectangularResult.jpg',findEquirectangularImage(fisheye_Image))
