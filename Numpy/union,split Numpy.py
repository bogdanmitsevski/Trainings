import numpy as np;

a = np.array([(1,2,3), (4,5,6)]);
b = np.array([(7,8,9),(10,11,12)]);
#hstack
a = np.hstack([a,b]);
print(a);

#vstack
a1 = np.array([(1,2,3), (4,5,6)]);
b1 = np.array([(7,8,9),(10,11,12)]);

b = np.vstack([a1,b1]);
print(a1);

a2 = np.fromstring("1 2 3 4", sep =" ");
b2 = np.fromstring("5 6 7 8", sep=" ");
a2 = np.vstack([a2,b2]);
print(a2);
#column_stack
a3 = np.fromstring("1 2 3 4", sep =" ");
b3 = np.fromstring("5 6 7 8", sep=" ");
print(np.column_stack([a3,b3]));
#row_stack
print(np.row_stack([a3,b3]));
#concatenate
a3.resize(3,3,3);
print(a3.shape);
print(a3);
b3.resize(3,3,3);
c0 = np.concatenate([a3,b3], axis = 0);
c1 = np.concatenate([a3,b3], axis = 1);
c2 = np.concatenate([a3,b3], axis = 2);
print(c0.shape);
print(c1.shape);
print(c2.shape);
#r_
print(np.r_[10,[1,2,3,],4,5,6,[0,0,0]]);
print(np.r_[1:10,2:10,100]);
print(np.r_[[[1,2,3],[1,2,3]], [[1,1,1]]]);
#c_
print(np.c_[[1,2,3],[2,3,4]]);
#hsplit, vsplit
arr = np.arange(10);
arr1 = np.hsplit(arr,2);
print(arr1);

print(arr);
arr2 = np.arange(10);
arr2.shape = 10,-1;
arr3 = np.vsplit(arr2,5);
print(arr3);
arr4 = np.arange(21);
arr4.resize(3,7);
arr5 = np.vsplit(arr4,3);
print(arr5);