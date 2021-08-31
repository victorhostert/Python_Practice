import random

while True:
    number = random.randint(1, 100)
    user_correct = False
    print("This script will generate a random number from 1 to 100")
    print("Try to guess it! You'll have 5 chances!")
    for i in range (0, 5):
        user = int(input("What's your guess? "))
        if user == number:
            user_correct = True
            print("Congratulations! You guessed correctly in", i, "tries!")
        elif user > number:
            print("Your number was too big! My number is smaller")
        else:
            print("Your number was too small! My number is bigger")
    if not user_correct:
        print(f"Oops, you failed! My number was {number}")