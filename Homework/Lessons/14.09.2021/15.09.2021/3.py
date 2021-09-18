a=list(input())
b=list(input())
def unique(a):
    c=set(a)
    l=set(b)
    d= c.intersection(l)
    return list(d)
print(unique(a))
