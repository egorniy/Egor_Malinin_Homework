d={}
def  ascii():
    i=65
    z={}
    while i<91:
        z[chr(i)] = i
        i+=1
    return z
print(ascii())