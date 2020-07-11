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
    path="./face-images"
    I=Images(path)
    images = I.load_images()
    print(images)
    image_1 = cv2.imread(images[0])
    cv2.imshow("First Image", cv2.resize(image_1, (500, 500)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
