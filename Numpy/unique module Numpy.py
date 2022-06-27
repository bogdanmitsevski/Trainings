import numpy as np;

#unique
a = np.array([1,2,3,4,1,1,2,3,5,6,7]);
setA = np.unique(a);
print(setA);
print(np.unique(a, return_counts=True));

#return_index
print(np.unique(a, return_index=True));

#return_inverse
setB, indx = np.unique(a, return_inverse=True);
print(setB);
print(setB[indx]);

x = np.array([[1,2,3,4], [1,1,2,2], [1,2,2,1], [1,1,1,1]]);
print(np.unique(x));

#np.in1d, elements form x1 to y1
x1 = np.array([0,1,2,3]);
y1 = np.array([1,2,3,4,5,6,7,8]);
print(np.in1d(x1,y1));

#np.intersect1d, the same elements from x1 and from y1
print(np.intersect1d(x1,y1));

#np.union1d, original elements from x1 and y1
print(np.union1d(x1,y1));

#np.setdiff1d, x1 elemnts from y1 elements
print(np.setdiff1d(x1,y1));
print(np.setdiff1d(y1,x1));

#np.setxor1d, elements that aren't in x1, y1 in the same time
print(np.setxor1d(x1,y1));