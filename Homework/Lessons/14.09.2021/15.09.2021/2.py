set_1={1,2,3,4,5,6}
set_2={4,5,6,7,8,9}
print(set_1.isdisjoint(set_2)) #если есть общие, то ложь
print (len(set_1)) #число элементов
print (set_1==set_2) #Если все элементы одного принадлежат всем другого то правда
print (set_1.issubset(set_2))#принадлежат ли все элементы первого второму
print(set_1.union(set_2))#объединение
print(set_1.intersection(set_2)) #Пересечение
print(set_1.difference(set_2))#Значения из 1 не принадлежащие 2
print(set_1.symmetric_difference(set_2))#Числа, которые есть в одном, но нет в другом
print(set_1.copy()) #копия множества
print(set_1.update(set_2))  #объединение.
print(set_1.intersection_update(set_2))#пересечение.
print(set_1.difference_update(set_2))#  вычитание.
print(set_1.symmetric_difference_update(set_2))# множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
print(set_1.add(2))# добавляет элемент в множество
#print(set_1.remove(77)) # удаляет элемент из множества.
print(set_1.discard(3)) #- удаляет элемент, если он находится в множестве.
print(set_1.pop()) #- удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
print(set_1.clear()) #- очистка множества.