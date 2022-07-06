import numpy as np
from PIL import Image, ImageDraw
import sys
import os

if len (sys.argv) == 2:
    raw_path =  sys.argv[1];
    path = raw_path.replace('\\', '/').replace('"',"");
    im = Image.open(path,'r');
    (width, height) = im.size;
else:
    print("Way is not correct");

sys.setrecursionlimit(150000)

def fillarea(a,x,y):
  if (x<0) or (y<0) or (x>=a.shape[1]) or (y>=a.shape[0]):
   return 0
  val=a[y,x]
  if val[2]==255: 
    return 0
  a[y,x]=[0,0,255]; 
  area=1 
  for _y in range(-1,2):
    for _x in range(-1,2):
      area=area+fillarea(a,x+_x,y+_y)
  return area;

a = np.array(im)

count=0
totalarea=0
for y in range(im.height):
 for x in range(im.width):
  val=a[y,x]
  if val[0]==255 and val[1]==0 and val[2]==0:
    count+=1
    area=fillarea(a,x,y)
    print(' i have found ',count,' figure with area = ',area)
    totalarea+=area
print('total area is ',totalarea)


im = Image.fromarray(a)
im.show()