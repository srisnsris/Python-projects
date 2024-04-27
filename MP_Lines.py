from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y) 
plt.show()


x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker=".",ls="None") 
plt.show()


x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker=".")   #soli line
plt.show()


x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker=".",c="r") #colour
plt.show()


x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker=".",c="g",lw="7",ls="dotted") 
plt.show()


x=np.arange(0,10,2)
y1=x**2
y2=x**3
print(x,y)
plt.plot(x,y1) 
plt.plot(x,y2) 
plt.show()


x=np.arange(0,10,2)
y1=x**2
y2=x**3
plt.plot(x,y1,x,y2) 
plt.show()


