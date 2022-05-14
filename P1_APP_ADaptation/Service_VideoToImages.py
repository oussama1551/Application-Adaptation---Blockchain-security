
# Importing all necessary libraries
import cv2
import os
import glob
from PIL import Image 

filep = ""
# Read the video from specified path

print("oussamamaamamam")
def convert():
    cam = cv2.VideoCapture(filep)

    try:
        
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')
    
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    
    # frame
    currentframe = 0
    
    while(True):
        
        # reading from frame
        ret,frame = cam.read()
    
        if ret:
            # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
    
            # writing the extracted images
            cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()



def ddeconvert():
    frameSize = (500, 500)

    out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

    for filename in glob.glob('imagetoconvert/*.jpg'):
        img = cv2.imread(filename)
        out.write(img)

    out.release()

