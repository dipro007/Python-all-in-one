n = input("Enter a text value: ")
nl =0
nd =0
nw = 0

for x in n:
    x.lower()
    if x >= 'a' and x <= 'z':
        nl = nl + 1
    elif x >= '0' and x <= '9':
        nd = nd + 1
    elif x == ' ':
        nw = nw + 1

print("Number of letters: ", nl)
print("Number of digits: ", nd)
print("Number of words: ", nw+1)

