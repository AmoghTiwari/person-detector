""" Steps to Detect Face 
1. Load images from a given path.
2. Apply face detection algo.

"""
import os
import cv2

class Images : 
    def __init__(self, path):
        self.path = path
        print("Path = " + self.path)
    
    def load_images(self):
        print("Loading from " + self.path)
        images = []
        for image in os.listdir(path): 
            images.append(path + "/" + image)
        return images

if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier('./supporting-files/haarcascade_frontalface_default.xml')
    path="./face-images"
    I=Images(path)
    images = I.load_images()
    # print(images)
    # image_1 = cv2.imread("/home/amogh/Pictures/Webcam/2020-07-14-232018.jpg")
    image_1 = cv2.imread(path + "/" + "1.jpg")
    # image_1 = cv2.imread(images[0])
    image_1 = cv2.resize(image_1, (500, 500))
    # cv2.imshow('Image', cv2.resize(image_1, (500, 500)))
    # cv2.waitKey(2000)
    gray = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h ) in faces : 
        print("a")
        print(x,y,w,h)
        image_1 = cv2.rectangle(image_1, (x,y),(x+w, y+h), (255,0,0),2)
        # cv2.imshow("Face", cv2.rectangle(image_1, (x,y),(x+w, y+h), (255,0,0),2))
    cv2.imshow("Detected Face", image_1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
