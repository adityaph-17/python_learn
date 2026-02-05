# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up

# Create a dictionary of Hindi words with their English translations

dict = {
    "pyaar": "love",
    "kitab": "book",
    "paani": "water",
    "ghar": "home",
    "dost": "friend",
    "school": "school"
}

# Provide user with an option to look it up
word = input("Enter a HINDI word to get its ENGLISH translation: ")

while True:
    # Take input from user
    word = input("\nEnter a Hindi word to search (or type 'exit' to quit): ").lower()

    # Exit condition
    if word == "exit":
        print("Program exited.")
        break

    # Lookup word
    if word in dict:
        print("English meaning:", dict[word])
    else:
        print("Word not found in dictionary")