def gen_name(name,num):
    i= 1
    while i <num:
        yield name 
        i+=1


ranger= gen_name('Линдси', 40)
ranger2= gen_name('Армен', 40)
ranger3= gen_name('Инга', 40)
names= [x for x in ranger]
names2= [x for x in ranger2]
names3= [x for x in ranger3]
print(names)
print(names2)
print(names3)