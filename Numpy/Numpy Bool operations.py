import numpy as np;
a = np.array([1,2,3,4,5,6,7,8,9]);
i = a>5;
print(i);
b = np.array([1,2,3,4,5,6,70,80,90]);
print(a==b);
#greater
print(np.greater(a,b));
#less
print(np.less(a,b));
#equal
print(np.equal(a,b));
#array_equal
print(np.array_equal(a,b));
#any
print(np.any(a==6));
#all
print(np.all(a>7));
#a/0,infinity
print(a/0);
#isinf
print(np.isinf(a));
#isnan
print(np.isnan(b));
indx = np.isinf(b);
print(b[~indx]);
#iscomplex
print(np.iscomplex(a));
#isreal
print(np.isreal(a));
X=np.array([True,False,False,True,True]);
Y=np.array([False,True,False,True,False]);
#logical_and
print(np.logical_and(X,Y));
#logical_or
print(np.logical_or(X,Y));
#logical_not
print(np.logical_not(X));
#logical_xor
print(np.logical_xor(X,Y));
