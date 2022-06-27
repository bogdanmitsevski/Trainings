import numpy as np;
a = np.arange(10);
#sum
res = 0;
res1 = 0;
print(a.sum());

for x in a:
    res+=x;
print(res);
#mean
print(a.mean());

i=0;
for y in a:
    res1+=y;
    i+=1;
print(res1/i);
#max
print(a.max());

res2 = 0;
for z in a:
    if(a[z] > a[z+1]):
        print(a[z]);
    else:
        print(a[z+1]);
#min
print(a.min());

a.resize(3,4);
print(a);
print(a.sum());
print(a.sum(axis = 0));
print(a.sum(axis=1));

b = np.array([-1,-2,-3,-4,-5,-6,-7,-8,-15]);
#abs
print(np.abs(b));

#amax
print(np.amax(b));

#amin
print(np.amin(b));

#round
print(np.round(0.3));

#argmax
print(np.argmax(b));

#argmin
print(np.argmin(b));

b.resize(3,4);
print(b);
print(np.amax(b,axis=0));
print(np.amin(b,axis=0));

#sin
c = np.linspace(0,np.pi,10);
print(c);
print(np.sin(c));

#cos
print(np.cos(c));

#np.random.rand
print(np.random.rand());
print(np.random.rand(5));
print(np.random.rand(3,6));

#np.random.randint
print(np.random.randint(3,5));
print(np.random.randint(5, size=4));

#np.random.seed
np.random.seed(12);
np.random.randint(10, size=10);
np.random.seed(12);
np.random.randint(10, size=10);

d = np.arange(10);
#np.random.shuffle
np.random.shuffle(d);
print(d);

#np.random.permutation
print(np.random.permutation(20));

#np.median
a1 = np.array([1,3,5,6,3,4,9,80,56,11]);
a2 = np.array([7,6,3,9,7,10,11,2,1,0]);
print(np.median(a1));

#np.var
print(np.var(a1));

#np.std
print(np.std(a1));

XY = np.vstack([a1,a2]);
print(XY);

#corrcoef
print(np.corrcoef(XY));

#correlate
print(np.correlate(a1,a2));