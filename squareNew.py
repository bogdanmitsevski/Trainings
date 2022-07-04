import numpy as np;
from PIL import Image, ImageDraw;
import sys;

print(sys.getrecursionlimit);
sys.setrecursionlimit(15000);

def fillarea(pixelArray,x,y):
    if((y<=0) or (x<=0) or (x>=270) or (y>=400)):
        return 0;
    val = pixelArray[y,x];
    if val[2] == 255:
        return 0;
    pixelArray[y,x] = [0,0,255];
    area= 1;
    for Y in range(-1,2):
        for X in range(-1,2):
            area=area+fillarea(pixelArray,x+X,y+Y);
    return area;
    



im = Image.new('RGB', (270, 400), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.rectangle((10, 11, 20, 30), fill=(10, 10, 10))
draw.rectangle((80, 40, 90, 50), fill=(10, 10, 10))
_xy = (        
            (105, 150),
            (110, 250),
            (103, 750),
            (115, 758)        
      )
draw.polygon(xy=_xy, fill='red', outline=(10, 10, 10))



pixelArray = np.array(im);


count = 0;
totalarea = 0;
for y in range (im.height):
    for x in range (im.width):
        val = pixelArray[y,x];
        if (val[0]!=255 and val[1]!= 0 and val[2]!=0)or (val[0]!=255 and val[1]!= 255 and val[2]!=255):
            count+=1;
            area = fillarea(pixelArray,x,y);
            print(' i have found ',count,' figure with area = ',area); 
            totalarea+=area;

print("Total area is",totalarea);
        
im = Image.fromarray(pixelArray);
im.show();