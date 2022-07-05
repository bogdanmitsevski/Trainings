from turtle import width
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

a = np.array(im);

count=0
for y in range(im.height):
 for val in a[y]:   #every point in y row (x)
  if (val[0]!=255): #check just R from RGB (it is enough)
   count+=1
print('area =',count)



