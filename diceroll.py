import random 

while True:     
     print(''' 1 - Roll the dice            2. Exit''')    
     option = int(input("what you want to do\n"))     
     if option==1:         
        dice = int(input("how many sides do you want your dice to have? "))
        number = random.randint(1,dice)         
        print(number)     
     else:         
        print("\n Thank you for using this program!")
        break