# importing OpenCV(cv2) module
import cv2
import math
import numpy as np 
# Pour vidéos entrantes in_h*in_w   720*1280 (lignes*colonnes) ratio 16/9
# Vidéos sortantes : out_height*out_width   1152*2048

FoV = math.pi
f = 1400/FoV
#create an zeros array of 1152*2048

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('bunny.mp4')
in_w=int(cap.get(3))
in_h=int(cap.get(4))
out_width = int(cap.get(3)*1.6)
out_height = int(cap.get(4)*1.6)
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (out_width,out_height))
# Check if video opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

out_calc_x = int(out_height/2)
out_calc_y = int(out_width/2)

in_calc_x = int(in_h/2)
in_calc_y = int(in_w/2)

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, vidFrame = cap.read()
    # print(type(vidFrame[0,0,0]))
    #print(vidFrame[0,0],vidFrame[0,0,0],vidFrame[0,0,1],vidFrame[0,0,2])
    M = np.zeros((out_height,out_height,3),dtype=np.uint8)
    if ret:
        xp=0
        for x in M:
            yp=0
            for y in x:
                Rp=(((xp-out_calc_x)**2)+((yp-out_calc_y)**2))**(0.5)
                l=(Rp/f)
                try :
                    i=int(abs(in_calc_x+((xp-out_calc_x)/l)*math.atan(l)))+1
                except:
                    i=0
                try:
                    j=int(abs(in_calc_y+((yp-out_calc_y)/l)*math.atan(l)))+1
                except:
                    j=0
                # print (i,xp,j,yp,l)
                try:
                    M[xp,yp,0] = vidFrame[i,j,0]
                    M[xp,yp,1] = vidFrame[i,j,1]
                    M[xp,yp,2] = vidFrame[i,j,2]
                except:
                    i=in_h-1
                    M[xp,yp,0] = vidFrame[i,j,0]
                    M[xp,yp,1] = vidFrame[i,j,1]
                    M[xp,yp,2] = vidFrame[i,j,2]
                yp += 1
            xp+=1
        # print(M)
        out.write(M)
    #     cv2.imshow('Frame',M)
    # # Press Q on keyboard to stop recording
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # Break the loop
    else: 
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
# cv2.destroyAllWindows()


# # Save image in set directory
# # Read RGB image
# img = cv2.imread('coffee.jpg') 
  
# # Output img with window name as 'image'
# cv2.imshow('image', img) 
  
# # Maintain output window utill
# # user presses a key
# cv2.waitKey(0)        
  
# # Destroying present windows on screen
# cv2.destroyAllWindows() 