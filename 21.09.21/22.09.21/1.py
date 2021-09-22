def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def dividers(n, div=1, all_divs=[]):
    if n == div:
        all_divs.append(div)
        return all_divs
    if n == div/2:
        return n
    elif div < n:
        if n % div == 0:
            all_divs.append(div)
        return dividers(n, div=div+1, all_divs=all_divs)
    else:
        print('Ошибка n')
def order(n):
    res = [int(x) for x in str(n)]
    return res
def order1(n):
    if len(n) == 1:
        return 1
    else:
        print(-n)
        order1(n-1)
        print(n)

print(order(6789))