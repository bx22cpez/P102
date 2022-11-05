import cv2
import dropbox
import time
import random

def take_snapshot():
    #initializingcv2
    videoCaptureObject=cv2.VideoCapture(0)
    
    number=random.randint(0,100)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        image_name = "img"+str(number)+".png"
        # this method is used to save an image to the storage device
        cv2.imwrite(image_name,frame)
        result=False
    return image_name
    #releases the camera
    videoCaptureObject.release()
    #closes all windows that are open during this process
    cv2.destroyAllWindows()


def upload_file(image_name):
    access_token = 'sl.BSexy4C2HkA0peL7ksT3Is_Hn95YRiZISVrQCKGPH8LC3XcVEXLb9XUaT3z8OHVa1SQ6TXAQTtv8umiJhAOMgWsP8DA0YuhDIy0R2V2s8xWAOfvT4X-uf_LqxyxSuapp5hMh0HtjdLrS'
    file=image_name
    file_from=file
    file_to="/pics/"+image_name
    dbx=dropbox.Dropbox(access_token)


    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file Uploaded")


while(True):
    if ((time.time()-start_time)>5):
        name=take_snapshot()
        upload_file(name)