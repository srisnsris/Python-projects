from  matplotlib import pyplot as plt
import numpy as np

years=["2017","2018","2019","2020"]
placements=[150,200,300,350]
plt.title("Placement Comparision")
plt.bar(years,placements,width=0.4)
plt.show()

#branch wise
#vertical
from  matplotlib import pyplot as plt
import numpy as np

years=["2017","2018","2019","2020"]
placements=[150,200,300,350]
cse=[50,80,100,100]
it=[50,80,100,150]
ece=[50,40,100,100]

ece_start=[cse[i]+it[i]for i in range(len(cse))]
plt.title("Placement Comparision")
plt.bar(years,cse,width=0.4,color="black")   #we can't give bottom here as it's bottom
plt.bar(years,it, bottom=cse,width=0.4,color="green")
plt.bar(years,ece,bottom=ece_start,width=0.4,color="red")
plt.ylim(0,300)

plt.show()
#horizontal   replace width with height

from  matplotlib import pyplot as plt
import numpy as np

years=["2017","2018","2019","2020"]
placements=[150,200,300,350]
cse=[50,80,100,100]
it=[50,80,100,150]
ece=[50,40,100,100]

ece_start=[cse[i]+it[i]for i in range(len(cse))]
plt.title("Placement Comparision")
plt.barh(years,cse,height=0.4,color="black")   #we can't give bottom here as it's bottom
plt.barh(years,it, left=cse,height=0.4,color="green")
plt.barh(years,ece,left=ece_start,height=0.4,color="red")
plt.xlabel("placements")
plt.ylabel("years")
plt.show()