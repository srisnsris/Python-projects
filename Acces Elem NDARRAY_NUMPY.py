import numpy as np
a=np.array([10,20,30,40,50,60])   #1D
print(a)
print(a[2])
print(a[-1])

print("a[-4]=",a[-4])

b=np.array([[10,20,30,40],[50,60,70,80]])  #2 D
print(b)
print(b[1,3])
print(b[0,2])
print("b[0,1]",b[0,1])


c=np.array([[[10,20,30,40],[50,60,70,80]],[[90,100,110,120],[130,140,150,160]]])  #3D
print(c)
print(c[1,1,2])
print("c[1,1,-2]",c[1,1,-2])

