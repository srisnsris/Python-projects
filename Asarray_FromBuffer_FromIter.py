
import numpy as np
a=np.array([10,20,30,40,50])
print(a)

res=np.asarray(a,dtype="float",order="C")   #chnaged to float --Assaary
print(res)

b=np.array([[10,20,30],[40,50,60]])
print(b)

res1=np.asarray(b,dtype="int",order="F")
print(res1)

for i in np.nditer(res1):
    print(i)
    
res2=np.asarray(b,dtype="int",order="C")
print(res2)

s=b"hello welcome to python"   #consider as byte b prefix; not strings
c=np.frombuffer(s,dtype="S1",count=-1,offset=0)
print(c)

s=b"hello welcome to python"   #consider as byte b prefix; not strings
c=np.frombuffer(s,dtype="S1",count=10,offset=0)
print(c)

s=b"hello welcome to python"   #consider as byte b prefix; not strings
c=np.frombuffer(s,dtype="S1",count=10,offset=6)
print(c)

list=[10,20,30,40,50]
d=np.fromiter(list,dtype="float",count=-1)   #changed to float
print(d)

d=np.fromiter(list,dtype="S1",count=-1)   #changed to float
print(d)

list=[10,20,30,40,50]
d=np.fromiter(list,dtype="float",count=2)   #changed to float
print(d)