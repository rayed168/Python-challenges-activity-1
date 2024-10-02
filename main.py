import random as rn
import time as tt
num=rn.randint(1,100)
def guess_the_number():
    global name
    name=input("Enter your name : ")
    print("Hello",name,"Today we are going to play a game.\n I am thinking of a number between 1 and 100. guess the number.")
    if num %2==0:
        print("The number is even")
    else:
        print("The number is odd")
    tt.sleep(0.5)
    print("Go ahead. Please guess")
def pick():
    guess_taken=1
    while guess_taken<10:
        tt.sleep(0.5)
        enter=int(input("Enter the number that you guessed : "))
        if enter<=100 and enter>=0:
            if enter<num:
                print("Your guess is too low")
            if enter>num:
                print("Your guess is too high")
            if enter!=num:
                tt.sleep(0.5)
                print("Try again")
            if enter==num:
                break
        if enter>100 or enter<1:
            print("The number is not in range")
            tt.sleep
            print("Please enter a number between 1 and 100 only")
        guess_taken=guess_taken+1    
    if enter==num:
        print("Good job. The number is",num)
        print("You guessed it in",guess_taken,"guesses")
    if enter!=num:
            print("Your guesses are over. The correct number was",num)
play_again="yes"            
while play_again=="yes" or play_again=="YES" or play_again=="y" or play_again=="Y" or play_again=="Yes":
    guess_the_number()
    pick()
    play_again=input("Do you want to continue : ")
    