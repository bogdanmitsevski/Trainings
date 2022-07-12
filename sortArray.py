def BubbleMethodDown(arr1):
 newArr = [int(x) for x in arr1];
 for i in range(0,len(newArr)-1): #number of cycle iteration
  for x in range(0,len(newArr)-1-i): #sort unsorted pairs in array
    if(newArr[x+1]<newArr[x]):
        newArr[x+1],newArr[x] = newArr[x],newArr[x+1];
 return("Array downs",newArr);

def BubbleMethodUp(arr1):
  newArr = [int(x) for x in arr1];
  for i in range(0, len(newArr)-1): #number of cycle iteration
    for x in range(0,len(newArr)-1-i): #sort unsorted pairs in array
     if(newArr[x+1]>newArr[x]):
        newArr[x+1], newArr[x] = newArr[x], newArr[x+1];
  return("Array ups",newArr);  
myFile = open("text.txt");
FileContent = myFile.read();
print(type(FileContent));
arr1 = FileContent.split(',')
BubbleMethodDown(arr1);
BubbleMethodUp(arr1);


