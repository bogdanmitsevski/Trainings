
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20};
arr1 = list(my_dict.items());
count = 0;
res_key1 = 0;
res_key2 = 0;
res_key3 = 0;
maxElemRes = 0;
index1 = 0;
index2 = 0;
maxElem = arr1[0][1];
index1 = arr1.index(maxElem);
print(index1);
print(maxElem.index);
while(count < len(arr1)):
    if(maxElem<=arr1[count][1]):
      maxElem = arr1[count][1];
      maxElemRes = arr1[count][1];
      res_key1 = count;
      index1 = arr1.index(arr1[res_key1]);
    count+=1;
count = 0;
maxElem = arr1[0][1];
while(count < len(arr1)):
   if(maxElem<=arr1[count][1] and arr1[count][1]<=arr1[res_key1][1] and arr1[count]!=arr1[index1]):
      maxElem = arr1[count][1];
      maxElemRes = arr1[count][1];
      res_key2 = count;
      index2 = arr1.index(arr1[res_key2]);
   count+=1;
count = 0;
maxElem = arr1[0][1];
while(count < len(arr1)):
    if(maxElem<=arr1[count][1] and arr1[count][1]<=arr1[res_key2][1] and arr1[count]!=arr1[index1] and arr1[count]!=arr1[index2]):
      maxElem = arr1[count][1];
      maxElemRes = arr1[count][1];
      res_key3 = count;
    count+=1;
print("Max First element is",arr1[res_key1],"\n","Max Second element is", arr1[res_key2], "\n","Max Third element is", arr1[res_key3]);



