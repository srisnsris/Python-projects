from  matplotlib import pyplot as plt
import numpy as np

marks=[90,70,50,30,10,15,35,45,5,10,15]
grade_intervals=[0,35,70,100]
plt.title("student Grade")
plt.hist(marks,grade_intervals)
plt.xticks([0,35,70,100])
plt.xlabel("Percentage")
plt.ylabel("No of students")
plt.show()

#histtype

from  matplotlib import pyplot as plt
import numpy as np

marks=[90,70,50,30,10,15,35,45,5,10,15]
grade_intervals=[0,35,70,100]
plt.title("student Grade")
plt.hist(marks,grade_intervals,histtype="bar",rwidth=0.7,facecolor="r")  #hist=bar,step,stepfilled
plt.xticks([0,35,70,100])
plt.xlabel("Percentage")
plt.ylabel("No of students")
plt.show()