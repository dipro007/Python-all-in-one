

num = int(input("Enter a number : "))
reverse_number = 0

while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Reversed Number : ", reverse_number)
