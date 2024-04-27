from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,5,1)
y1=x**2
y2=x**3

plt.plot(x,y1,x,y2)
plt.show()

from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,5,1)
y1=x**2
y2=x**3

plt.plot(x,y1,x,y2)
plt.legend(['Squares','Cubes']) #repsensts squares & cubes forlines ; above is not
plt.show()


from  matplotlib import pyplot as plt
import numpy as np

x=np.arange(0,5,1)
y1=x**2
y2=x**3
plt.plot(x,y1, label="Squares")
plt.plot(x,y2, label="Cubes")   #by giving only label fun won't dsiplay squ & cubes in plot
#only by adding legend func will dsplay plots with titles--squa, cubes
plt.legend(loc="upper right") #repsensts squares & cubes forlines ; above is not or loc =1
plt.show()


