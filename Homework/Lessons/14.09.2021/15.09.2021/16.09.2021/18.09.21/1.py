l=[0,1,2,3,4,5,6,7,8,9]
n=int(input())
try:
    l[n]
except IndexError as err:
    print('Неверный индекс',err)
else:
    print ('Все чики пуки')
finally:
    print('Ты молодец')