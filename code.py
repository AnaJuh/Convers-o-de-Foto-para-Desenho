from matplotlib.image import imsave
import cv2
import matplotlib.pyplot as plt
import random
import numpy as np
import glob

arq = "/caminho/*"
images1 = []
images2 = []
images3 = []

for img in glob.glob("/caminho/*.JPG"):
    n = cv2.imread(img)
    m = cv2.imread(img,0)
    c = cv2.imread(img,0)
    images1.append(n)
    images2.append(m)
    images3.append(c)
for img in glob.glob("/caminho/*.jpg"):
    n = cv2.imread(img)
    m = cv2.imread(img,0)
    c = cv2.imread(img,0)
    images1.append(n)
    images2.append(m)
    images3.append(c)
    
img8 = cv2.imread("/caminho/img43.jpeg")

from random import randint
cont = 1
for i in range(768):
  for j in range(1024):
        imggg[i][j]= img[i][j]
for a in range(768):
  for b in range(1024):
    for k in range(3):
          if imggg[a][b][k] !=  0:
            imggg[a][b][k] = images1[46][a][b][k]
plt.imshow(mask)
plt.show()      
cv2. imwrite("/caminho/img9.jpeg",imggg)

print(len(images2))

for i in range(291):
  img = cv2.adaptiveThreshold(images2[i], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C  , cv2.THRESH_BINARY, 41,3)      
  texto = "/caminho/3121"+str(i)+".jpg"
  print(texto)
  cv2.imwrite(str(texto),img) 
  plt.imshow(img)
  plt.show()
  
 img8 = cv2.imread("//caminho/img43.jpeg")

from random import randint
cont = 1
for i in range(768):
  for j in range(1024):
        imggg[i][j]= img[i][j]
for a in range(768):
  for b in range(1024):
    for k in range(3):
          if imggg[a][b][k] !=  0:
            imggg[a][b][k] = images1[46][a][b][k]
plt.imshow(imggg)
plt.show()      
cv2. imwrite("/caminho/img9.jpeg",imggg)

img8 = cv2.imread("/caminho/img43.jpeg")

from random import randint
cont = 1
for i in range(768):
  for j in range(1024):
        imggg[i][j]= img[i][j]
for a in range(768):
  for b in range(1024):
    for k in range(3):
          if imggg[a][b][k] !=  0:
            imggg[a][b][k] = images1[4][a][b][k]
plt.imshow(imggg)
plt.show()      
cv2. imwrite("/caminho/img9.jpeg",imggg)
