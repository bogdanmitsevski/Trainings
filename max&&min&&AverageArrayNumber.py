import math;
def averageArrayNumber(arr1):
 newArr = [int(x) for x in arr1];
 nextArr = [];
 sum= 0;
 for x in newArr:
    sum+=x;
 res =sum/len(newArr);
 count = 0;
 while(count<len(newArr)):
    nextArr.insert(count,abs(res-newArr[count]));
    count+=1;
 count1 = 0;
 res1 = nextArr[0];
 while(count1<len(nextArr)):
  
    if(res1>=nextArr[count1]):
        res1 = nextArr[count1];
    count1+=1;
 index1 = nextArr.index(res1);
 return("Average Number in Array is", newArr[index1]);

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
print("Do you want to find MIN or MAX or AVERAGE number in Array? Enter 'Min' or 'Max' or 'Average'" );

a = input();

if a == "min" or a == "MIN" or a =="Min":
 maxArrayNumber(arr1);

elif a == "max" or a == "MAX" or a == "Max":
    minArrayNumber(arr1);

elif a == "average" or a =="AVERAGE" or a == "Average":
    averageArrayNumber(arr1);
