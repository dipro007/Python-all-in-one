

def EveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

c = input("enter string: ")
print("Orginal String is ", c)

print("Printing only even index chars")
EveIndexChar(c)
