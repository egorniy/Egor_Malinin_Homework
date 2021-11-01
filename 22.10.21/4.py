import time 
import random
import matplotlib.pyplot as plt
import numpy as np
t=time.time()
times,ns=[],[]
#li = [0, 5, 8, 4, 9, 3]
def bubble(li):
    n = len(li)
    for j in range(0,n-1):
        for i in range(0,n-j-1):
             if li[i] < li[i+1]:
                  li[i],li[i + 1] = li[i + 1], li[i]

for k in range (100,9999,100):
    elements=[random.randrange(0,k) for _ in range(k)]
    t=time.time()
    bubble(elements)
    work_time = time.time()-t
    times.append(work_time)
    ns.append(k)
    print(k)
plt.plot(ns,times)
plt.show()


