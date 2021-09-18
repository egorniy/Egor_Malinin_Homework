
try: 
    print('Введите 3 цифры кода оператора')
    code=(input())
    a=len(code)
    if a==3:
        print('Введите 7 цифр номера')
        num= (input())
        b=len(num)
    else:
        print ('ВСЕ ПЛОХО')
    if b==7:
        num=int(num)
        code=int(code)
        b=('+7-'+str(code)+'-'+str(num))
    else:
        print ('ВСЕ ПЛОХО')
except Exception as err:
    print('Необходимо ввести 10 цифр номера',err)
else:
    print ('+7-',code,'-',num)
finally:
    print('Программа выполнена')
