
import cv2
from config import cfg 
import os
import sys
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np

#import image_parser

from PIL import Image
from collections import Counter
import prettytable

class detector:
    #def __init__(self):
    #    self.img_path = ''
        
    def detect(img):
        #self.img_path = list(paths.list_images(loc))[0]
        #img_path = img_path
        #img = Image.open(img_path)
        countb = 0
        countg = 0
        countw = 0
        listb = []
        listg = []
        listw = []
        rev_listb = []
        rev_listg = []
        rev_listw = []
        counts = {}

        #size = w, h = img.size
        baseIm = Image.new('RGBA', (225, 225), 'black')
        img = img.resize((225,225))
        w = baseIm.width
        h = baseIm.height
        data = img.load()

        #plt.imshow(img)
        #plt.show()

        for i in range(w):
            for j in range(h):

                # getting the RGB pixel value.
                r, g, b = img.getpixel((i, j))

                # Apply formula of grayscale:
                grayscale = (0.299*r + 0.587*g + 0.114*b)

                # setting the pixel value.
                data[i, j] = (int(grayscale), int(grayscale), int(grayscale))

        # Saving the final output
        # as "grayscale.png":
        img.save("grayscale", format="png")

        #plt.imshow(img)
        #plt.show()

        number_of_white_pix = np.sum(img == 255)      # extracting the white pixels 
        number_of_black_pix = np.sum(img == 0)          # extracting the black pixels 
        #number_of_gray_pix = np.sum(0 < img < 255)      # extracting the gray pixels

        from itertools import product

        for pos in product(range(h), range(w)):
            pixel = img.getpixel(pos)
            #print(pixel)
            #print(pos)
            if( 0 < pixel[0] < 70 ):
                countb += 1
                listb.append(pos)
            elif( 70 < pixel[0] < 170):
                countg += 1
                listg.append(pos)
            elif( 170 < pixel[0] < 255):
                countw += 1
                listw.append(pos)

        counts['b'] = countb
        counts['g'] = countg
        counts['w'] = countw


        #print(number_of_white_pix)
        #print(number_of_black_pix)
        #print(number_of_gray_pix)
        #print(countb)
        #print(countg)
        #print(countw)
        #print(img)
        #print(listb)
        #print(counts)

        #contours, h = cv2.findContours(listb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if min(counts, key=counts.get) == 'b':
            x1 = min(listb)[0]
            x2 = max(listb)[0]
            #y1 = min(listb)[1]
            #y2 = max(listb)[1]

            listb.sort(key=lambda x:x[1])
            rev_listb = listb
            ##print(new_listb)
            y1 = rev_listb[0][1]
            y2 = rev_listb[-1][1]

        elif min(counts, key=counts.get) == 'g':
            x1 = min(listg)[0]
            x2 = max(listg)[0]

            listg.sort(key=lambda x:x[1])
            rev_listg = listg
            ##print(new_listg)
            y1 = rev_listg[0][1]
            y2 = rev_listg[-1][1]

        elif min(counts, key=counts.get) == 'w':
            x1 = min(listw)[0]
            x2 = max(listw)[0]

            listw.sort(key=lambda x:x[1])
            rev_listw = listw
            ##print(new_listw)
            y1 = rev_listw[0][1]
            y2 = rev_listw[-1][1]


        #print(x1)
        #print(x2)
        #print(y1)
        #print(y2)
        ##print(new_listb[0][1])
        ##print(new_listb[-1][1])

        from PIL import ImageDraw

        Drawer = ImageDraw.Draw(img)
        Drawer.rectangle((x1, y1, x2, y2), fill=None, outline="red", width=3)

        #plt.imshow(img)
        #plt.show()

        crack_w = x2 - x1
        crack_h = y2 - y1
        #print(" The dimensions of the crack are ----- ", crack_w, "*", crack_h, "pix")
        ##shape = [(x1 - 10, y1), (x2, y2 + 10)]
        ##Drawer.line(shape, fill= "red", width=3)

        ##plt.imshow(img)
        ##plt.show()
        
        return img
