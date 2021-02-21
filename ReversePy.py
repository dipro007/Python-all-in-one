num = int(input("Enter number: "))

for rows in range(num, 0, -1):
    for columns in range(0, num - rows):
        print(end=" ")
    for columns in range(0, rows):
        print("*", end=" ")
    print(" ")