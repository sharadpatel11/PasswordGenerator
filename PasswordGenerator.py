import random

print("Welcome to the PyPassword Generator!")

length = int(input("How many charcters do you want in your password?\n"))
numSym = int(input("How many symbols would you like?\n"))
numNum = int(input("How many numbers would you like?\n"))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = []

for l in range(0, length):
    if numSym > 0:
        password.append(random.choice(symbols))
        numSym -= 1
    elif numNum > 0:
        password.append(random.choice(numbers))
        numNum -= 1
    else: 
        password.append(random.choice(letters))
        
mixPassword = random.sample(password, length)

newPassword = ""

for l in range(0, length):
    newPassword += mixPassword[l]

print(f"Here is your password: {newPassword}")