from os import access
from random import random
import cv2
import dropbox
import time
import random


startTime=time.time()

def take_snapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        imgName="img"+str(number)+".jpg"
        cv2.imwrite(imgName,frame)
        startTime=time.time
        result=False

    return imgName
    print("Snapshot Taken!!!")

    videoCaptureObject.release()
    
    cv2.destroyAllWindows()



def upload_file(imgName):
    access_token="sl.BES7fFvvRNHksxnS087A8H-H64BNIrdUnPuLTANKTF2wHPPRIktasXefLVAtj_NLhV89qXpuFM8gaooMLVADJ4x2MEdzyy6SceqJGB6TUSqjbpux9xjn8Z5gh1BPSVQ6HkjtWg4"
    file=imgName
    file_from=file
    file_to="/IMGSNAPSHOTS/"+imgName
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
    
def main():
    while(True):
        if((time.time()-startTime)>=3):
            name=take_snapShot()
            upload_file(name)

main()