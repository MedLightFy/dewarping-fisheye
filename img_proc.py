# importing OpenCV(cv2) module
import cv2
import math
import numpy as np 

FoV = math.pi
f = 1400/FoV #given focal length
img = cv2.imread('images/fisheye.png')
if(img.any()):        
    in_w=img.shape[1] #1280
    in_h=img.shape[0] #960
    out_width = int(in_w*1.6) #2048
    out_height = int(in_h*1.6) #1536

    out_calc_x = int(out_height/2) #1028
    out_calc_y = int(out_width/2) #728

    in_calc_x = int(in_h/2) #640
    in_calc_y = int(in_w/2) #480
    # this is the hardest part knowing the focal length
    f = 900/FoV
    M = np.zeros((out_height,out_width,3),dtype=np.uint8)
    xp=1
    for x in M:
        yp=1
        for y in x:
            Rp=((xp-out_calc_x)**2)+((yp-out_calc_y)**2)
            Rp=math.sqrt(Rp)
            l=(Rp/f)
            if l==0:
                l=1
            i=in_calc_x+((xp-out_calc_x)/l)*math.atan(l)+1
            j=in_calc_y+((yp-out_calc_y)/l)*math.atan(l)+1

            i=np.uint16(i)

            j=np.uint16(j)      
            try:
                M[xp,yp] = img[i,j]
            except:
                pass
            yp += 1
        k=xp/out_height
        print (f"image is {k:.2%} processed",end="\r")
        xp+=1
    cv2.imwrite('images/no_fisheye.png',M)
    print (f"the image has finished processing")
else:
    print("image not found")