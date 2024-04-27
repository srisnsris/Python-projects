from  matplotlib import pyplot as plt
import numpy as np

x=['A','B','C','D']
y=[10,30,20,40]
plt.barh(x,y,color="red",height=0.8)
plt.show()


from  matplotlib import pyplot as plt
import numpy as np

x=['A','B','C','D']
y=[10,30,20,40]
c=["red","blue","green","black"]
plt.barh(x,y,color=c,height=0.8)
plt.xlabel("vege")
plt.ylabel("quant")
plt.show()