d={}
def  ascii(l):
    i=65
    z={}
    while i<91:
        z[chr(i)] = l.count(chr(i))
        i+=1
    return z
    
l=input()
print(ascii(l))