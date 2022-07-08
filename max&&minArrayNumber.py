
def maxArrayNumber(arr1):
 newArr = [int(x) for x in arr1];
 res = newArr[0];
 count = 0;
 while(count<len(newArr)):
  
    if(res<=newArr[count]):
        res = newArr[count];
    count+=1;
 return 'Max ArrayNumber is',res;

def minArrayNumber(arr1):
 newArr = [int(x) for x in arr1];
 res = newArr[0];
 count = 0;
 while(count<len(newArr)):
  
    if(res>=newArr[count]):
        res = newArr[count];
    count+=1;
 return 'Min ArrayNumber is',res;


myFile = open("text.txt");
FileContent = myFile.read();
print(type(FileContent));
arr1 = FileContent.split(',')
print("Do you want to find MIN or MAX number in Array? Enter 'Min' or 'Max'" );

a = input();

if a == "min" or a == "MIN" or a =="Min":
 maxArrayNumber(arr1);

elif a == "max" or a == "MAX" or a == "Max":
    minArrayNumber(arr1);