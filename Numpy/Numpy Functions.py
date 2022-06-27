import numpy as np;
print(np.array([0]*10));
print(np.array([1]*15));
print(np.array([x for x in range (7,20)]));
#empty
print(np.empty(10));
print(np.empty((4,3), dtype="str_"));
#eye
print(np.eye(20));
#identity
print(np.identity(4));
#zeros
print(np.zeros((5,3)));
#ones
print(np.ones([4,3], dtype="int8"));
#full
print(np.full([3,3], -3));
#mat
print(np.mat('1,2,3,4'));
#diag
print(np.diag([1,2,3]));
#tri
print(np.tri(5));
#vander
print(np.vander([1,2,3]));
#arange
print(np.arange(10));
print(np.arange(1,10,0.5));
#cos
print(np.cos(np.arange(0, np.pi, 0.2)));
#linspace
print(np.linspace(0, np.pi, 10));
#logspace
print(np.logspace(1, np.pi, 10));
#geomspace
print(np.geomspace(1,16,5));
#copy
myArray = np.array([1,23,45,67]);
newArray = np.copy(myArray);
print(newArray);
#fromiter
print(np.fromiter("HELLO", dtype='<U1'));
#fromstring
print(np.fromstring(('1 2 3'), dtype="int16", sep = " "));

newArray1 = np.array([[1,2,3],[12,4,5]]);
print(newArray1.ndim);

#change dtype
f = np.array([0.1, 0.3, 0.4, 0.5, 0.7, 0.1, 0.3, 0.4, 0.5]);
print(f.dtype);
f.dtype = np.int32;
print(f.dtype);
print(f.size);
print(f.shape);
f.dtype = "float64";
print(f);
f.shape = 1,1;
print(f);
k = f;
f.shape = 3,3;
print(f);
k = f.view();
print(k);
print(f);
l = f.copy();
print(l);

array1 = np.arange(10);
print(array1);
array1.shape = 2,5;
print(array1);
array2 = array1.reshape(10);
print(array2);
print(array1);
array1.shape = 5,2;
print(array1);
#ravel
array3 = ([1,2,3,4,5,6,7,8,9]);
c = array3.ravel;
print(c);
array3.resize(100,3, refcheck=False);
print(array3);
#transparency
newArray = np.array([[1,2,3],[1,3,4],[1,6,7]]);
newArray1 = newArray.T;
print(newArray1);
x = np.arange(10);
x.shape = 1,-1;
y = x.T;
print(y);
x_test = np.arange(32).reshape(8,2,2);
print(x_test);
print(x_test.shape);
x_test4 = np.expand_dims(x_test, axis = 0);
print(x_test4.shape);
x_test4[0,0,0,0] = -100;
print(x_test4);
#append
a = np.append(x_test4, x_test4, axis=0);
print(a.shape);
b = np.delete(a,0,axis=0);
print(b.shape);
b = np.expand_dims(x_test4, axis = -2);
print(b.shape);
print(b);
#squeeze
c = np.squeeze(b);
print(c.shape);
c = np.squeeze(b, axis=2);
print(c.shape);
#newaxis
d = np.arange(1,10);
k = d[:,np.newaxis];
print(k);
k1 = d[np.newaxis,:,np.newaxis];
print(k1);