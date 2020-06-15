import string
import random

#call function to get password
def passwordMaker(length):
    password = ''
    characters = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits
    for i in range(length):
        chooser = random.randint(0,2)
        if chooser == 0:
            password = password + str(characters[random.randint(0, len(characters)-1)])
        elif chooser == 1:
            password = password + str(symbols[random.randint(0, len(symbols)-1)])
        elif chooser == 2:
            password = password + str(numbers[random.randint(0, len(numbers)-1)])
        else:
            print("bruh moment")
    return password


