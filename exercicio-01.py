#encoding: utf-8

import numpy as np

#exercice 01

s1=np.array((168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 323, 106, 1055, 170))
print(f"Serie 1 = {s1}")
s2=np.array((168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258,
242, 331, 251, 180, 106, 1055, 200))
print(f"Serie 2 = {s2}")
#Euclidean Distance
dist=np.linalg.norm(s1-s2)
print(f"Euclidean Distance between S1 and S2 = {dist}")
#Mean
s_mean=np.mean(np.array([s1,s2]), axis=0)
print(f"Mean between S1 and S2 = {s_mean}")
#Max
s_max=np.fmax(s1,s2)
print(f"Maximum values per instant in S1 and S2 = {s_max}")
#Min
s_min=np.fmin(s1,s2)
print(f"Minimum values per instant in S1 and S2 = {s_min}")


