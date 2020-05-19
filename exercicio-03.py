#encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt

#exercice 03

age=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39",\
     "40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79",\
     "80-84","85-89","90-94","95-99","100+"]
pop=np.array([7016987,7624144,8725413,8558868,8630229,8460995,7717658,\
              6766664,6320568,5692014,4834995,3902344,3041035,2224065,\
              1667372,1090517,668623,310759,114964,31529,7247])

plt.figure(figsize=(20,20))
plt.title("Brazilian Male Population in 2010", fontsize=22)
plt.ylabel("Age Groups", fontsize=15)
plt.xlabel("Population", fontsize=15)
plt.xticks([ 0, 2000000, 4000000, 6000000, 8000000 ], \
           [ "0", "2 mi", "4 mi", "6 mi", "8 mi" ] )
plt.barh(age, pop, color="blue")
plt.show()