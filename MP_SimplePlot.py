from  matplotlib import pyplot as plt
import numpy as np
x=[0,1,2,3,4,5]
y=[0,10,20,30,40,50]
plt.plot(x,y)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show() 




from  matplotlib import pyplot as plt
x=[0,1,2,3,4,5]
y=[i**2 for i in x]
plt.plot(x,y)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show() 


#if we didn't mention x axis; default show x ais numers
plt.plot([100,200,300,400,500])
plt.show()


x=np.arange(0,10,2)
y=[i**2 for i in x]
print(x,y)
plt.plot(x,y)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show() 

