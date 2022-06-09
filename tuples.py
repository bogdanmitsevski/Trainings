#tuple output

myTuple = ("Bohdan1", "Bohdan2", "Bohdan3");
print(myTuple);

#tuple length
myTuple1 = ("Bohdan1", "Bohdan2", "Bohdan3");
print(len(myTuple1));

#tuple type
myTuple2 = ("Bohdan1", "Bohdan2", "Bohdan3");
print(type(myTuple2));

#tuple constructor
myTuple3 = tuple(("Bohdan1", "Bohdan2", "Bohdan3"));
print(myTuple3);
print(len(myTuple3));

#tuple item output
myTuple4 = ("Bohdan1", "Bohdan2", "Bohdan3");
print(myTuple4[1:2]);
print(myTuple4[1]);

#negative indexing
myTuple5 = ("Bohdan1", "Bohdan2", "Bohdan3");
print(myTuple5[-1]);

#check if item exists
myTuple6 = ("Bohdan1", "Bohdan2", "Bohdan3");
if "Bohdan1" in myTuple6:
    print("'Bohdan1' exists");

#change or add tuple items;
myTuple7 = ("Bohdan1", "Bohdan2", "Bohdan3");
myList = list(myTuple7);
print(myList);
myList[0] = 1;
myTuple7 = tuple(myList);
print(myTuple7);

#delete the tuple
myTuple8 = ("Bohdan1", "Bohdan2", "Bohdan3");
del myTuple8;
print(myTuple8);

#loop tuples
myTuple9 = ("Bohdan1", "Bohdan2", "Bohdan3");
for x in myTuple9:
    print(x);

myTuple10 = ("Bohdan1", "Bohdan2", "Bohdan3");
for x in range (len(myTuple10)):
    print(myTuple10[x]);

myTuple11 = ("Bohdan1", "Bohdan2", "Bohdan3");
i = 0;
while i<len(myTuple11):
    print(myTuple11[i]);
    i+=1;

#join tuples
myTuple12 = ("Bohdan1", "Bohdan2", "Bohdan3");
myTuple13 = ("Bohdan4", "Bohdan5", "Bohdan6");
myTuple12+=myTuple13;
print(myTuple12);
myTuple12*=2;
print(myTuple12);