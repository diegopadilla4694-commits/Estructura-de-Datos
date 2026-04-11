import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

print("WELCOME CREATE A PASSWORD")
print("-----------------------------------------------------")
key_letters = int(input("Enter letters to create your password?\n"))
key_numbers = int(input("Enter numbers to create your password?\n"))
key_symbols = int(input("Enter symbols to create your password?\n"))

password_list = []

for char in range(1, key_letters + 1):
    password_list.append(random.choice(letters))


for char in range(1, key_numbers + 1):
    password_list.append(random.choice(numbers))


for char in range(1, key_symbols + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += str(char) 

print(f"Your Password is:{password}")






