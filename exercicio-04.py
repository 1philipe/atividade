#encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

#exercice 04

age=["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39",\
     "40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79",\
     "80-84","85-89","90-94","95-99","100+"]

male_pop=np.array([7016987,7624144,8725413,8558868,8630229,8460995,7717658,\
              6766664,6320568,5692014,4834995,3902344,3041035,2224065,\
              1667372,1090517,668623,310759,114964,31529,7247])

fem_pop=np.array([6779171,7345231,8441348,8432004,8614963,8643419,\
             8026854,7121915,6688796,6141338,5305407,4373877,3468085,\
             2616745,2074264,1472930,998349,508724,211594,66806,16989])



fig, axes = plt.subplots(ncols=2, sharey=True, sharex=False)
axes[0].barh(age, male_pop, align='center', color='blue')
axes[1].barh(age, fem_pop, align='center', color='red')
axes[0].invert_xaxis()
axes[0].yaxis.tick_right()
axes[0].set(title="Male Population")
axes[1].set(title="Female Population")
plt.sca(axes[0])
plt.xticks([ 0, 2000000, 4000000, 6000000, 8000000 ], \
           [ "0", "2 mi", "4 mi", "6 mi", "8 mi" ] )
plt.sca(axes[1])
plt.xticks([ 0, 2000000, 4000000, 6000000, 8000000 ], \
           [ "0", "2 mi", "4 mi", "6 mi", "8 mi" ] )
graph=plt.figure(1)
graph.suptitle("Brazilian Population per Sex and Age Group", fontsize=15)
fig.tight_layout()
fig.subplots_adjust(wspace=0.09)
plt.show()