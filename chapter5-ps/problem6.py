# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = {}

for i in range(4):
    name = input("Enter your name: ")
    lang = input("Enter your favorite language: ")
    d.update({name: lang})

print("Favorite languages of friends:", d)


