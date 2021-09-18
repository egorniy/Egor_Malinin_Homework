import re
text=str(input())

d={}

def yaustal(text):
    text1= re.sub("[!|?|.|...|:|;|,]","",text)
    k=text1.lower()
    k= k.split()
    l=set(k)    
    set_words = set()

    
print( yaustal(text))


