from  matplotlib import pyplot as plt
import numpy as np

student_performance=["Excellent","Good","AVer","Poor"]
student_values=[15,25,12,8]
plt.pie(student_values,labels=student_performance)
plt.show()


from  matplotlib import pyplot as plt
import numpy as np

student_performance=["Excellent","Good","AVer","Poor"]
student_values=[15,25,12,8]
plt.pie(student_values,labels=student_performance,startangle=90) #if no angle starts from x -axis
#angle=90,180, 0=x axis
plt.show()



from  matplotlib import pyplot as plt
import numpy as np

student_performance=["Excellent","Good","AVer","Poor"]
student_values=[15,25,12,8]
plt.pie(student_values,labels=student_performance,startangle=90,explode=[0.2,0,0,0]) #if no angle starts from x -axis
#angle=90,180, 0=x axis explode=portion out of circle
#0.2,0.1,0.3,0.4,, explode
plt.show()

#shadow
from  matplotlib import pyplot as plt
import numpy as np

student_performance=["Excellent","Good","AVer","Poor"]
student_values=[15,25,12,8]
plt.pie(student_values,labels=student_performance,startangle=0,explode=[0.2,0,0,0],shadow=True) #if no angle starts from x -axis
#angle=90,180, 0=x axis explode=portion out of circle
#0.2,0.1,0.3,0.4,, explode
plt.show()

#colours
from  matplotlib import pyplot as plt
import numpy as np

student_performance=["Excellent","Good","AVer","Poor"]
student_values=[15,25,12,8]
plt.figure(figsize=(8,10))
plt.pie(student_values,labels=student_performance,startangle=0,explode=[0.2,0,0,0],shadow=True,colors=["green","blue","yellow","red"]
        ,autopct="%2.1f%%") #if no angle starts from x -axis
#angle=90,180, 0=x axis explode=portion out of circle
#0.2,0.1,0.3,0.4,, explode
plt.legend(title="performances") #display righ side labels
plt.show()

