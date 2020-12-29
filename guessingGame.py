import random
x=[1,2,3,4,5,6,7,8,9]
number=random.choice(x)
print("Guess a number between 1 and 9 :")

chances=0
while chances < 5:

   
    numberInput = int(input("Enter your guess:- "))

   

    if (numberInput == number):
     
        print("Congratulation YOU WON!!!")
        break

    
    elif (numberInput < number):
        print("Your guess was too low: Guess a number higher than", numberInput)

    else:
        print("Your guess was too high: Guess a number lower than", numberInput)

 
    chances += 1

if(chances>=5 & numberInput!=number):
    print("YOU LOSE! THE NUMBER WAS",numberInput)