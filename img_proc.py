# importing OpenCV(cv2) module
import cv2
import math
import numpy as np 

FoV = math.pi
f = 1400/FoV #given focal length
img = cv2.imread('images/fisheye.png')
if(img.any()):        
    in_w=img.shape[1]
    in_h=img.shape[0]
    out_width = int(in_w*1.6)
    out_height = int(in_h*1.6)

    out_calc_x = int(out_height/2)
    out_calc_y = int(out_width/2)

    in_calc_x = int(in_h/2)
    in_calc_y = int(in_w/2)
    # this is the hardest part knowing the focal length
    f = 900/FoV
    # print(f)
    # print("x","y")
    # print(in_h,in_w)
    # print(out_height,out_width)
    M = np.zeros((out_height,out_height,3),dtype=np.uint8)
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
            if(i<0):
                # i=abs(in_h+i)
                pass
            elif(i>=in_h):
                # i=abs(in_h-i)
                pass
            i=np.uint16(i)
            if(j<0):
                # j=abs(in_w+j)
                pass
            elif(j>=in_w):
                # j=abs(in_w-j)
                pass
            j=np.uint16(j)        
                # print(i,j)
            # print (i,xp,j,yp,l)
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