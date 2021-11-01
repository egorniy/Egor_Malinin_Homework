#Вывести  все цифры числа в том порядке, в котором они есть в виде списка
n = int(input())
def order1 (n):
    if n < 10:
        return [n]
    return order1(n // 10) + [n % 10]
k=n//10
print(order1(n))