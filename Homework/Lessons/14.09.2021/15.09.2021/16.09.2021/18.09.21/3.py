
a= int((input()))
try:
    b=2929/a

except ZeroDivisionError as err:
    print('Тебе мама не говорила, что на ноль делить плохо?',err)
else:
    print (b)
finally:
    print('вот и славно')
