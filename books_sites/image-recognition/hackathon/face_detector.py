# -*- coding:utf-8 -*-

import os
import cv2

def main():
    for srcpath, _, files in os.walk('photos'):
        if len(_):
            continue
        dstpath = srcpath.replace('photos', 'faces')
        os.makedirs(dstpath, exist_ok=True)
        for filename in files:
            if filename.startswith('.'):  # Pass .DS_Store
                continue
            try:
                detect_faces(srcpath, dstpath, filename)
                print(srcpath, dstpath, filename)
            except:
                continue

def detect_faces(srcpath, dstpath, filename):

    cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    image = cv2.imread('{}/{}'.format(srcpath, filename))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_image)
    # Extract when just one face is detected
    if (len(faces) == 1):
        (x, y, w, h) = faces[0]
        image = image[y:y+h, x:x+w]
        image = cv2.resize(image, (100, 100))
        cv2.imwrite('{}/{}'.format(dstpath, filename), image)

if __name__ == '__main__':
    main()
