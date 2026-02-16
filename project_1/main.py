import random

# Computer choice
computer = random.choice(["snake", "water", "gun"])

# User choice
user = input("Enter your choice (snake, water, gun): ").lower()

print("Computer chose:", computer)

# Game logic
if user == computer:
    print("It's a Draw!")

elif user == "snake" and computer == "water":
    print("User Wins")

elif user == "snake" and computer == "gun":
    print("Computer Wins")

elif user == "water" and computer == "snake":
    print("Computer Wins")

elif user == "water" and computer == "gun":
    print("User Wins")

elif user == "gun" and computer == "snake":
    print("User Wins")

elif user == "gun" and computer == "water":
    print("Computer Wins")

else:
    print("Invalid input! Please enter snake, water, or gun.")