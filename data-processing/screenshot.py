import cv2
import os
import time

def get_frames(inputFile,outputFolder,step,count):

  '''
  Input:
    inputFile - name of the input file with directoy
    outputFolder - name and path of the folder to save the results
    step - time lapse between each step (in seconds)
    count - number of screenshots
  Output:
    'count' number of screenshots that are 'step' seconds apart created from video 'inputFile' and stored in folder 'outputFolder'
  Function Call:
    get_frames("test.mp4", 'data', 10, 10)
  '''

  #initializing local variables
  step = step
  frames_count = count

  currentframe = 0
  frames_captured = 0

  #creating a folder
  try:  
      # creating a folder named data 
      if not os.path.exists(outputFolder): 
          os.makedirs(outputFolder) 
    
  #if not created then raise error 
  except OSError: 
      print ('Error! Could not create a directory') 
  
  #reading the video from specified path 
  cam = cv2.VideoCapture(inputFile) 


  #reading the number of frames at that particular second
  frame_per_second = cam.get(cv2.CAP_PROP_FPS)

  while (True):
      ret, frame = cam.read()
      if ret:
          if currentframe > (step*frame_per_second):  
              currentframe = 0
              #saving the frames (screenshots)
              name = './data/frame' + str(frames_captured) + '.jpg'
              print ('Creating...' + name) 
              
              cv2.imwrite(name, frame)       
              frames_captured+=1
              
              #breaking the loop when count achieved
              if frames_captured > frames_count-1:
                ret = False
          currentframe += 1           
      if ret == False:
          break
  
  #Releasing all space and windows once done
  cam.release()
  cv2.destroyAllWindows()

i = 1

get_frames("F:\BaiduNetdiskDownload\anime\20120007\[SumiSora][120007][01][GB][720p].mp4", "imgs", 1, 1000)

exit()

while i < 23:
    pstr = "F:\BaiduNetdiskDownload\anime\20120007\[SumiSora][120007][" + str(i) + "][GB][720p].mp4"
    get_frames(pstr, "imgs", 1, 1000)
    i += 1

