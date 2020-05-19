#encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
#exercice 02

age=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39",\
     "40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79",\
     "80-84","85-89","90-94","95-99","100+"]
pop=np.array([6779171,7345231,8441348,8432004,8614963,8643419,\
             8026854,7121915,6688796,6141338,5305407,4373877,3468085,\
             2616745,2074264,1472930,998349,508724,211594,66806,16989])

plt.figure(figsize=(20, 20))
plt.title("Brazilian Female Population in 2010", fontsize=22)
plt.ylabel("Population", fontsize=15)
plt.yticks([ 0, 2000000, 4000000, 6000000, 8000000 ], \
           [ "0", "2 mi", "4 mi", "6 mi", "8 mi" ] )
plt.xlabel("Age Groups", fontsize=15)
plt.bar(age, pop, color="red")
plt.show()