n = int(input())
m = int(input())
def f(n,m):
    print(n)
    if n>m:
        f(n-1,m)
print (f(n,m))