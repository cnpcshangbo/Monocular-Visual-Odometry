# Python script author: Bo Shang
# Python script function: 

import cv2

cap = cv2.VideoCapture('/usr/local/home/bsr8w/Downloads/P0440046.MP4')

if (cap.isOpened() == False): 
  print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
count = 0
while(True):
  ret, frame = cap.read()
  if ret == True: 
    scale_percent = 50 # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    k = cv2.waitKey(1)


    cv2.imshow('frame',resized)

    # press space key to start recording
    if k%256 == 32:
        cv2.imwrite("rgb_%05d.jpg" % count, resized) 
        count += 1
        #cv2.imwrite()
        #out.write(frame) 

    # press q key to close the program
    elif k & 0xFF == ord('q'):
        break

  else:
     break  

cap.release()
out.release()

cv2.destroyAllWindows() 
