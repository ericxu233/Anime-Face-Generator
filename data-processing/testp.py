import cv2
import sys
import os
import os.path

def detect(filename, iter, path, cascade_file = "lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (128, 128))
    for (x, y, w, h) in faces:
        img = image[y:y+h, x:x+w]
        rimg = cv2.resize(img, (128, 128))
        outp = path + "/" + "pp" + str(iter) + ".jpg"
        cv2.imwrite(outp, rimg)
        iter += 1
    return iter


path = "ztestresults"
orig = "yuz"
i = 0
final = 1979
count = 0

while i <= 1979:
    name = orig + "/" + orig + str(i) + ".jpg"
    count = detect(name, count, path)
    i += 1
