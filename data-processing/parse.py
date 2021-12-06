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
                                     minNeighbors = 8,
                                     minSize = (128, 128))
    for (x, y, w, h) in faces:
        img = image[y:y+h, x:x+w]
        rimg = cv2.resize(img, (128, 128))
        outp = path + "/" + "er" + str(iter) + ".jpg"
        cv2.imwrite(outp, rimg)
        iter += 1
    return iter


namelist = ["kpa"]
listsize = [4029, 2639]
path = "aData/assem3"
count = 0

for dir in namelist:
    for filename in os.listdir(dir):
        if filename.endswith(".jpg"):
            pic = os.path.join(dir, filename)
            print(pic)
            count = detect(pic, count, path)


