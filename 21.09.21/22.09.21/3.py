a = int(input())
def recur_factorial(n):
      if n == 1:
              return n
      else:
              return n*recur_factorial(n-1)
num = a
if num < 0:
      print('Факториал не работает с отрицательными числами')
elif num == 0:
      print("Факториал 0 это 1")
else:
      print("Факториал",num,"это",recur_factorial(num))