import random
n = int(input())
k = int(input())
l = [random.randint(-n,n) for i in range(k)]
print(l)
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print (l)