# Function to remove a word from list and strip spaces
def remove_word(lst, word):   # lst = list, word = word to remove
    
    new_list = []             # Empty list to store result
    
    for item in lst:          # Loop through each item in list
        
        stripped_item = item.strip()   # Remove extra spaces
        
        if stripped_item != word:      # If item is NOT equal to word
            
            new_list.append(stripped_item)  # Add to new list
    
    return new_list            # Return final cleaned list


# Given list (with extra spaces)
lst = [" apple ", "banana ", " mango", "banana"]

# Word to remove
word = "banana"

# Calling function
result = remove_word(lst, word)

# Print result
print(result)