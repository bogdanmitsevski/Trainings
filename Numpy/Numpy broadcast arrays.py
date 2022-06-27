import numpy as np;

a= np.arange(1,10);
b = np.arange(2,3);
print(a*b);

a1 = np.arange(1,10).reshape(3,3);
b1 = np.array([1,2,3]);
print(a1+b1);

a3 = np.arange(6).reshape(3,1,2);
b3 = np.ones(4).reshape(2,2);
res = a3+b3;
print(res);
res.shape;

x = np.array([1,2,3]);
y = np.array([4,5]);
z = np.array([6,7,8,9,10]);
x.shape = 1,1,-1;
y.shape = 1,-1,1;
z.shape = -1,1,1;

res1 = x*y+z;
print(res1);
print(res1.shape);

x = np.array([1,2,3]);
y = np.array([4,5]);
z = np.array([6,7,8,9,10]);
print(x,y,z);

xn,yn,zn = np.ix_(x,y,z);
print(xn,yn,zn);

xn.shape;
yn.shape;
zn.shape;

res2 = xn*yn+zn;
print(res2);