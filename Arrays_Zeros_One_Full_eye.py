import numpy as np
a=np.array([10,20,30,40,50,60])
print(a)

print(np.shape(a))

a=np.array([[10,20,30],[40,50,60]])   #2 indices, 3 elements
print(a)

b=np.array([[10,20],[30,40],[50,60]])  #3 incises having 2 elemst
print(b) 
print(np.shape(b))

print(np.reshape(a,(3,2)))    #chnaged 3indices 2 ele

print(np.reshape(a,(2,3)))  #2 indices 3elementss


b=np.array([[10,20],[30,40],[50,60]]) 
print(b)

print(np.reshape(b,(2,3)))
print(np.reshape(b,(3,2)))

print(np.zeros((4,4)))

print(np.zeros((4,4),dtype=int))

print(np.ones((4,4),dtype=int))

print(np.ones((3,4),dtype=int))


print(np.full((3,4),10))


print(np.eye(3))

print(np.eye(3,dtype=int))
print(np.eye(3,4,dtype=int))

