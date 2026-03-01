# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

n = random.randint(1, 100)
a= -1
guess = 1
while(a != n):
    a = int(input("guess the number betn 1 to 100 :"))
    if (a>n):
        print ("The number is lower, guess again.")
        guess +=1
    elif(a<n):
        print("The number is higher, guess the number again.")
        guess +=1

print(f"you guess the number :{n} in {guess} guesses!")

