import numpy as np;

#np.dot
a = np.arange(1,10).reshape(3,3);
b = np.arange(10,19).reshape(3,3);
print(a);
print(b);
a*b;
print(np.dot(a,b));

#matmul
print(np.matmul(a,b));

a1 = np.arange(1,10);
b1 = np.ones(9);
print(np.dot(a1,b1));

#inner
print(np.inner(a1,b1));

#outer,@
print(np.outer(a,b));
print(a@b);

#перемноження матриці на вектор
a2 = np.arange(1,4);
b2 = np.arange(4,10).reshape(3,2);
print(a2);
print(b2);
print(np.dot(a2,b2));

a3 = np.arange(1,3);
b3 = np.arange(4,10).reshape(3,2);
print(a3);
print(b3);
print(np.dot(b3,a3));

#np.linalg.matrix_rank
a4 =np.array([(1,2,3), (1,4,9), (1,8,27)]);
print(np.linalg.matrix_rank(a4));
print(a4);
#np.linalg.solve
a5 = np.arange([10,20,30]);
print(np.linalg.solve(a4,a5));

#np.linalg.inv
invA = np.linalg.inv(a4);
print(invA);
print(invA @ a5);