import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['~', '!', '@', '#', '$', "%", '^', '&', '*']

letters_count = int(input())
symbols_count = int(input())
numbers_count = int(input())
password = []
new_password = []

for index in range(0, letters_count):
    password.append(random.choice(alphabets))

for index in range(0, symbols_count):
    password.append(random.choice(symbols))

for index in range(0, numbers_count):
    password.append(random.choice(numbers))

random.shuffle(password)
# for index in range(0, len(password)):
#     new_password.append(random.choice(password))

print("".join(password))