from  matplotlib import pyplot as plt
import numpy as np

x=[1,2,3,4,5,6]
y=[10,60,20,50,30,40]
color=["red","green","blue","brown","black","orange"]
plt.scatter(x,y,color=color)
plt.show()

from  matplotlib import pyplot as plt
import numpy as np

x=[1,2,3,4,5,6]
y=[10,60,20,50,30,40]
#color=["red","green","blue","brown","black","orange"]
size=[10,20,30,40,50,60]
plt.scatter(x,y, s=size,alpha=1,cmap="viridis") #alpha=transp
plt.show()


from  matplotlib import pyplot as plt
import numpy as np

x=[1,2,3,4,5,6]
y=[10,60,20,50,30,40]
color=["red","green","blue","brown","black","orange"]
size=[10,20,30,40,50,60]
plt.scatter(x,y,s=size,alpha=1,c=c)

x=[1,2,3,4,5,6]
y=[20,50,30,10,60,35]
color=["red","green","blue","brown","black","orange"]
size=[10,20,30,40,50,60]
plt.scatter(x,y,s=size,alpha=1,c=c)
plt.show()

#first plot, second plot diffent color; no need all colours


from  matplotlib import pyplot as plt
import numpy as np

x=[1,2,3,4,5,6]
y=[10,60,20,50,30,40]
#color=["red","green","blue","brown","black","orange"]
size=[10,20,30,40,50,60]
plt.scatter(x,y,s=size,alpha=1,color="green",label="2019")

x=[1,2,3,4,5,6]
y=[20,50,30,10,60,35]
#color=["red","green","blue","brown","black","orange"]
size=[10,20,30,40,50,60]
plt.scatter(x,y,s=size,alpha=1,color="blue",label="2020")  #we can "label"--legend
plt.legend()
plt.title("scatter plot")
plt.show()