import cv2
import math
import numpy as np 

PI = 3.141592653589793;
PATH_IMAGE =   "images/img1.jpg";

#Find the corresponding fisheye outpout point corresponding to an input cartesian point
def findFisheye(Xe,Ye,Rr,Cfx,Cfy,He,We):
    #fisheyePoint = {}
    #theta, r, Xf, Yf; Polar coordinates

    r = Ye/He*Rr;
    theta = Xe/We*2.0*PI;
    Xf = Cfx+r*math.sin(theta);
    Yf = Cfy+r*math.cos(theta);
    fisheyePoint = (Yf,Xf);

    return fisheyePoint;

fisheyeImage = cv2.imread(PATH_IMAGE)
# int Hf, Wf, He, We;
# double R, Cfx, Cfy;

Hf = fisheyeImage.shape[0];
Wf = fisheyeImage.shape[1];
Rr = Hf/2; #The fisheye image is a square of 1400x1400 pixels containing a circle so the radius is half of the width or height size
Cfx = Wf/2; #The fisheye image is a square so the center in x is located at half the distance of the width
Cfy = Hf/2; #The fisheye image is a square so the center in y is located at half the distance of the height

He = int(Rr);
We = int(2*PI*Rr);

equirectangularImage = np.zeros((He, We, 3), dtype=np.uint8);

for Ye in range(He):
     for Xe in range(We):
        try:
            ij = findFisheye(Xe, Ye, Rr, Cfx, Cfy, He, We)
            equirectangularImage[Ye,Xe] = fisheyeImage[int(ij[0]),int(ij[1])]
        except Exception as e:
            print (e)
 
cv2.imwrite('images/equirectangularImage.jpg',equirectangularImage)