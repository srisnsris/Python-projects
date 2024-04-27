from  matplotlib import pyplot as plt
import numpy as np
x=[0,1,2,3,4]
y1=[50,30,10,40,20]
y2=[10,30,50,20,40]

plt.plot(x,y1,x,y2)
plt.show()


from  matplotlib import pyplot as plt
import numpy as np
x=[0,1,2,3,4]
y1=[50,30,10,40,20]
y2=[10,30,50,20,40]

plt.subplot(1,2,1)  #1 represets row, 2 rep columns 1 reprse index
plt.plot(x,y1)


plt.subplot(1,2,2)
plt.plot(x,y2)
plt.show()



#####

x=[0,1,2,3,4]
y1=[50,30,10,40,20]
y2=[10,30,50,20,40]
y3=[10,20,30,40,50]
y4=[50,40,30,20,10]
plt.plot(x,y1,x,y2)
plt.show()


from  matplotlib import pyplot as plt
import numpy as np
x=[0,1,2,3,4]
y1=[50,30,10,40,20]
y2=[10,30,50,20,40]

plt.subplot(2,2,1)  #2 represets row, 2 rep columns 1 reprse index
plt.plot(x,y1)
plt.subplot(2,2,2)
plt.plot(x,y2)

plt.subplot(2,2,3)
plt.plot(x,y2)

plt.subplot(2,2,4)
plt.plot(x,y2)
plt.show()



############   plt titles



from  matplotlib import pyplot as plt

x=[0,1,2,3,4]
y1=[50,30,10,40,20]
y2=[10,30,50,20,40]
y3=[10,20,30,40,50]
y4=[50,40,30,20,10]
plt.suptitle("MultiplePlots")
plt.subplot(1,4,1)  #1 represets row, 4rep columns 1 reprse index
plt.plot(x,y1)
plt.title("Plot-1")       #plots

plt.subplot(1,4,2)
plt.plot(x,y2)
plt.title("Plot-2")

plt.subplot(1,4,3)
plt.plot(x,y2)
plt.title("Plot-3")

plt.subplot(1,4,4)
plt.plot(x,y2)
plt.title("Plot-4")
plt.show()


