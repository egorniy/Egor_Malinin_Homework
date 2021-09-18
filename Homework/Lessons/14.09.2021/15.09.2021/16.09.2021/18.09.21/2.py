
a= str((input()))
try:
    b=a+3

except TypeError as err:
    print('Ты должен должен был сделать вввод циферок, а не буковок',err)
else:
    print (a+3)
finally:
    print('вот и славно')