d={'один':1,'два':2,'три':3}
k=str(input())
def values(d,k):
    if k in d.keys():
        return d[k]
    else: 
        return 'Fuck!'
d['единица']=1
d['нуль']=0
a={'четыре':4,'пять':5,'шесть':6}
d.update(a)
print(d.keys())
print(d.values())
print('Запрос по ключу:',values(d,k))