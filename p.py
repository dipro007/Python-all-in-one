
n = int(input("Enter a number: "))

def p(n):
   for m in range(0, n):
      for n in range(0, m+1):
         print("* ",end="")
      print(" ")

p(n)