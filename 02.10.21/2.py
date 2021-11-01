file = input('Укажите путь к файлу')
try:
    grade = int(input('Проходной балл'))
except Exception as err:
    print('Необходимо указать целочисленное значение', err)
    quit()
try:
    f = open(file, 'r')
except Exception as err:
    print('Подобного файла не существует', err)
    quit()
print('Вы хотите узнать: 1.кто сдал  2.кто провалил ')
tt=int(input())
lines = f.readlines()
for line in lines:
    p = line.split()
    b = p[-1]
    if b == '5':
        b = 5
    elif b == '4':
        b = 4
    elif b == '3':
        b = 3
    elif b == '2':
        b = 2
    try:
        c = int(b)
    except Exception as err:
        print('Значения в файле некорректны', err)
    if tt ==1:
        if c >= grade:
            print(p [0:2], b)
    elif tt == 2:
        if c < grade:
             print(p [0:2], b)

