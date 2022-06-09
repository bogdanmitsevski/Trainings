#set output
mySet = {"Bohdan0", 1,10, "Bohdan32"};
print(mySet);

#set size
mySet1 = {"Bohdan0", 1,10, "Bohdan32"};
print(len(mySet1));

#data type
mySet2 = {"Bohdan0", 1,10, "Bohdan32"};
print(type(mySet2));

#set constructor
mySet3 = set(("Bohdan0", 1,10, "Bohdan32"));
print(mySet3);

#check if item is in this set
mySet6 = {"Bohdan0", 1,10, "Bohdan32"};
if 1 in mySet6:
    print("Yes. This item in this set");

#add item to set
mySet7 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet7.add(False);
print(mySet7);

#update set
mySet8 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet9 = {"Bohdan", 0, 9, "Bohdan31"};
mySet8.update(mySet9);
print(mySet8);

mySet10 = {"Bohdan0", 1, 10, "Bohdan32"};
myList = ("Bohdan", 0, 9, "Bohdan31");
mySet10.update(myList);
print(mySet10);

#remove item from set;
mySet10 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet10.remove("Bohdan0");
print(mySet10);

mySet11 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet11.discard(1);
print(mySet11);

mySet12 = {"Bohdan0", 1, 10, "Bohdan32"};
x = mySet12.pop();
print(mySet12);
print(x);

#loop sets
mySet4 = {"Bohdan0", 1,10, "Bohdan32"};
for x in mySet4:
    print(x);

#join sets
mySet13 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet14 = {"ABC", 2, 5,7};
mySet15 = mySet13.union(mySet14);
print(mySet15);

mySet16 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet17 = {"ABC", 2, 5,7};
mySet16.update(mySet17);
print(mySet16);

#update items, that exist in both sets

mySet18 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet19 = {"ABC", 1, 5,7};
mySet18.intersection_update(mySet19);
print(mySet18);

mySet20 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet21 = {"ABC", 1, 5,7};
mySet22 = mySet21.intersection(mySet20);
print(mySet22);

#update items, that exist in every set
mySet23 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet24 = {"ABC", 1, 5,7};
mySet23.symmetric_difference_update(mySet24);
print(mySet23);

mySet25 = {"Bohdan0", 1, 10, "Bohdan32"};
mySet26 = {"ABC", 1, 5,7};
mySet27 = mySet26.symmetric_difference(mySet25);
print(mySet27);
