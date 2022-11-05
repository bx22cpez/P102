import cv2

def take_snapshot():
    #initializingcv2
    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        # this method is used to save an image to the storage device
        cv2.imwrite("newpicture1.jpg",frame)
        result=False
    #releases the camera
    videoCaptureObject.release()
    #closes all windows that are open during this process
    cv2.destroyAllWindows()


take_snapshot()