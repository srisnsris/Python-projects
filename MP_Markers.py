from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y)
plt.show()


from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker="P",ms="15")   #_, X,>
plt.show()


from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y)
plt.show()


from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker=".",ms="15",mec="y")   #_, X,p>  #mec=colour
plt.show()


from  matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x**2
print(x,y)
plt.plot(x,y,marker=".",ms="15",mec="y",mfc="k")   #_, X,p>  #mec=colour #inside circle colour mffc
plt.show()
