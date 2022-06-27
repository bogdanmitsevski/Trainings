import numpy as np
a = np.arange(10);
print(a[1:2]);
print(a.size);
print(a[4:]);
a[4:] = [1,2,3,4,5,6];
print(a);
for x in a:
    print(x);
x = np.array([(1,2,3), (2,3,4), (4,5,6)]);
print(x);
print(x[1,1]);
for row in x:
    for val in row:
        print(val, end=" ");

for val in x.flat:
    print(val, end=" ");
a1 = np.arange(1,14);
print(a1);
print(a1[[0]]);
indx = np.array([1,1,1,1,1,2,2,3]);
print(a1[indx]);
bIndx = [True, True, False, True, False, True, False, True, True, False, True, False, True];
print(a1[bIndx]);
a2 = np.arange(1,10);
i = np.array([(1,2,3),(4,5,6)]);
print(a2[i]);
a3 = np.arange(10)
print(a3)
a3 = a3.reshape(-1, 2)
print(a3)