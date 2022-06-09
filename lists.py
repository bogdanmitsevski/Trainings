#Lists

#list output
myList = ["Bohdan", True, 1,2,3];
print(myList);

#list size
myList1 = [True, False, "new", 1,2,3];
print(len(myList1));

#list type
myList2 = [False, "new1", 2,5,10];
print(type(myList2));

#constructor of the list
myList3 = list(("Bohdan2", "Misha", "Kostya"));
print(myList3);

#special item output
myList4 = [1,2,3,9];
print(myList4[2]);
print(myList4[-2]);

#return several elements from list
myList5 = [True, 5,6,-9];
print(myList5[1:2]);
print(myList5[:3]);
print(myList[2:]);

#check if item is in list
myList6 = [1,2,3,4,5,6,7,8,9,10, "Bohdan", "Mitsevskyi"];
if 10 in myList6:
    print("10 is in List");

#add new item in array
myList7 = [1,2,3,4,5,6,7,8];
myList7[1] = "Bohdan";
print(myList7);
myList7.insert(2,1);
print(myList7);

#add item to the end of the list
myList8 = [4,5,8,12,13,45];
myList8.append("Bohdan");
print(myList8);

#add elements from 1 array to another
myList9 = [1,2,3];
myList10 = [4,5,6];
myList9.extend(myList10);
print(myList9);

#add elements from tuple to the list
myList11 = [1,2,3,4,5];
myTuple = (6,7,8,9);
myList11.extend(myTuple);
print(myList11);

#remove elements
myList12 = [1,2,3,4,5,6,7,8,9];
myList12.remove(3);
print(myList12);
myList12.pop(1);
print(myList12);
del myList12[5];
print(myList12);

#clear list
myList13 = [1,2,3,4,5,6,7,8,9,10];
myList13.clear();
print(myList13);

#Loop List
myList14 = ["a", "b", "c", "d", "e", "f"];
for x in myList14:
    print(x);

for x in range (len(myList14)):
    print(myList14[x]);

i = 0;
while i<(len(myList14)):
    print(myList14[i]);
    i+=1;

#add list items with some letters in new list
myList16 = ["Bohdan", "Car", "SKF"];
myList17 = [];
for x in myList16:
    if "a" in x:
        myList17.append(x);
print(myList17);

#sort list alphabetically
myList18 = ["Bohdan", "Car", "Automate","Cars"];
myList18.sort();
print(myList18);

#sort reverse
myList19 = ["Bohdan", "Car", "Automate","Cars"];
myList19.sort(reverse = True);
print(myList19);

#closest numbers to 50
myList20 = [65,70,120,50,51];
def myFunc(n):
    return abs(n-50);
myList20.sort(key=myFunc);
print(myList20);


#sort reverse
myList21 = ["A","B","C","D","E","F"];
myList21.reverse();
print(myList21);

#copy lists
myList22 = [1,2,3,4,5];
myList23 = [];
myList23 = myList22.copy();
print(myList23);

#add list 1 to list 2

myList24 = [1,2,3,4,5,6,7];
myList25 = [8,9,10];
myList24+=myList25;
print(myList24);


