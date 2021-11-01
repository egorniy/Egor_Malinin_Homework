#6
f = open('d:\\Project\\Homework\\24.09.21\\egor.txt','r')
t = f.readlines()
print(t)
t = [line[:-1] for line in t]
d = {t[0]:t[1], t[2]:t[3]}
print(d)