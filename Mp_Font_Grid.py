
--pip install -U scikit-learn




from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x*10
plt.plot(x,y) 
f1={'family':'arial','color':'red','size':15}
f2={'family':'calibri','color':'green','size':15}
plt.title("Multiples of 10",fontdict=f1)
plt.xlabel("X - Values",fontdict=f2)
plt.ylabel("X Multiply 10",fontdict=f2)
plt.show()


x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.plot(x,y)
plt.grid()
plt.show()


x=[1,2,3,4,5]
y=[10,50,20,40,30]
plt.plot(x,y)
plt.grid(axis="both",ls="dotted",lw=1,c="r")
plt.show() 