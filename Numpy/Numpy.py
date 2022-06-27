import numpy as np;

def ArrayFunc():
    a = np.array([[1,2,3,4], [10,11,0,5]]);
    for x in a:
        for y in x:
            print(x,y);
#ArrayFunc();

#b = np.zeros(2000);
#print(b);

#c = np.empty(2);
#print(c);

#d = np.linspace(0,15, num = 5);
#print(d)
#print(c.ndim);

#newArray = np.array([1,2,3,4,5,6,7,8]);
#print(newArray);
#newArray.reshape(4,3);
#print(newArray);

#N = 3;
#M = 2;
#A = [];
#for i in range (N):
#    A.append(0*M);
#    print(A);
myArray = np.arange(1,10,2);
print(myArray)

b = np.array([1,2,3,4,5], dtype="str_");
print(b);

c = np.int8(b);
print(c);

d = np.array([[1,2,3], [4,5,6], [7,8,9], [1,1,1]]);
print(d);

e = np.array([[[1,2,3],[3,4,5],[6,7,8], [1,2,3],[3,4,5],[6,7,8]], [[1,2,3],[3,4,5],[6,7,8], [1,2,3],[3,4,5],[6,7,8]], [[1,2,3],[3,4,5],[6,7,8], [1,2,3],[3,4,5],[6,7,8]]])
print(e);
print(e[0,1]);

