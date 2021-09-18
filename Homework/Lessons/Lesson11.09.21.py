from random import choice
import string
num=int(input())
k=0
def create (num):
    result = ''
    for i in range (num):
        result += choice(string.ascii_letters)
    return result


