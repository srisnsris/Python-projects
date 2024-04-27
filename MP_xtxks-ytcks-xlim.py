from  matplotlib import pyplot as plt
import numpy as np

x=[10,20,30,40,50]
y=[100,200,300,400,500]
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.xticks(x,["a","b","c","d","e"])  #labels chnaged--ticks
plt.yticks(y,["0-100","100-200","200-300","300-400","400-500"])#y l ticks changed
plt.show()

#limit

from  matplotlib import pyplot as plt
import numpy as np

x=[10,20,30,40,50]
y=[100,200,300,400,500]
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.xlim([10,100])
plt.ylim([10,1000])  #y=10,20,100,200
plt.title("Demonstartion of Xlim,YlimXtixks,Yticks,Xlabel,Ylabel")
plt.show()
