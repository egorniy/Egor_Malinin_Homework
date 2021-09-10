name = [ 'Malinin Egor Nik', 'Oshepcova Reg Max']
def initials(name):
    l = name.split()
    return l[0] +' ' + l[1][0:1] + '. ' + l[2][0:1] + '.'
def initials_more(names):
    result=[]
    for name in names:
        new_name=initials(name)
        result.append (new_name)
    return result
print(initials_more(name))