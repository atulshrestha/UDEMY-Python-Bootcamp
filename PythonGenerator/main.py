import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","#","%","$","&","(",")","*","+"]

print ("Welcome to the PyPassword Generator!")
nr_letters = int(input("How may letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

password_list = []

for char in range(1, nr_letters+1):
    random_letter = random.choice(letters)
    password_list += random_letter

for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)


password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")