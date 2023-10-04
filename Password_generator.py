import random

number_of_lets = int(input("Please specify the number of letters to be included in password: "))
number_of_symbs = int(input("Please specify the number of symbols to be included in password: "))
number_of_numbs = int(input("Please specify the number of numbers to be included in password: "))

lets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQRSTUVWXYZ"
nums = "0123456789"
symbs = "~!@34%^&*()-+=:[}{[<>?/*"

passwrd = []

for i in range(number_of_lets):
    passwrd += random.choice(lets)
for i in range(number_of_symbs):
    passwrd += random.choice(symbs)
for i in range(number_of_numbs):
    passwrd += random.choice(nums)

random.shuffle(passwrd)
if len(passwrd) <= 12:
    print(''.join(passwrd))
else:
    print("Password too long")