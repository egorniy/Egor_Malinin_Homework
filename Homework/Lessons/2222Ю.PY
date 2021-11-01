import time
import random
import matplotlib.pyplot as pt

def bubble(inp_list):
    for i in range(len(inp_list)):
        for k in range(len(inp_list)-1-i):
            if inp_list[k] > inp_list[k+1]:
                inp_list[k], inp_list[k+1] = inp_list[k+1], inp_list[k]

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n>q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


time_list, n_list = [], []
time_list_2, n_list_2 = [], []
for n in range(100, 1001, 100):
    elements = [random.randrange(0, n) for _ in range(n) ]
    elements_2 = elements.copy()
    t = time.time()
    bubble(elements)
    work_time = time.time() - t
    time_list.append(work_time)
    n_list.append(n)
    t_2 = time.time()
    quicksort(elements_2)
    work_time = time.time() - t_2
    time_list_2.append(work_time)
    n_list_2.append(n)

    print(n)
fig, ax = pt.subplots()
ax2 = ax.twinx()
ax.plot(n_list, time_list, label='Bubble', color='b')
ax2.plot(n_list_2, time_list_2, label='Быстрая сортировка', color='yellow')
pt.show()