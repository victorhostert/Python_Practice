import random

all_characters = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
all_numbers = '0123456789'
all_letters = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    p_len = int(input("How long you want your password to be? "))
except:
    print("You must type a valid number!")
    exit()
print("You want:")
print("1 - All characters to be numbers")
print("2 - All characters to be letters")
print("3 - All characters to be random, including symbols?")
option = input("What's your option? ")
p = ""
if option == '1':
    p = p.join(random.sample(all_numbers, p_len))
    print(f"Your password is {p}")
elif option == '2':
    p = p.join(random.sample(all_letters, p_len))
    print(f"Your password is {p}")
elif option == '3':
    p = p.join(random.sample(all_characters, p_len))
    print(f"Your password is {p}")
else:
    print("Enter a valid option!")