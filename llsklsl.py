from random import choice
import string
num=int(input())
l=int(input)
z=0
def create (num):
    for z in range(l):
        result = ''
        z=z+1
        for i in range (num):
            result += choice(string.ascii_letters)
            return result
print(create(num))

