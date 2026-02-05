# Demonstrating various list methods in Python
list = ["aditya", "asd", "xyz", "123", 123, 12.34, True]
print ("Original List:", list)

# 1. append() - adds an element to the end of the list
list.append("new_element")
print("\nList after append:", list)

# 2. sort() - sorts the list (only works if all elements are of the same type)
numeric_list = [5, 2, 9, 1, 5, 6]
numeric_list.sort()
print("\nSorted Numeric List:", numeric_list)

# 3. reverse() - reverses the order of the list
numeric_list.reverse()
print("\nList after reverse:", numeric_list)

# 4. insert() - inserts an element at a specified position
numeric_list.insert(2, "inserted_element")
print("\nList after insert:", numeric_list)

# 5. pop() - removes or returns the last element of the list

l1 = [1, 2, 3, 4, 5]
popped_element = l1.pop(3)  # removes the element at index 3
print("\nList after pop:", l1)
print("Popped element of index 3:", popped_element)

# 6. remove() - removes the first occurrence of a specified value
l2 = [1, 2, 3, 4, 5, 3]
l2.remove(3)  # removes the first occurrence of 3
print("\nList after remove:", l2)

# 7. count() - returns the number of occurrences of a specified value
l3 = [1, 2, 3, 4, 5, 3, 3,3,3,3,3]
count_of_3 = l3.count(3)
print("\nCount of 3 in the list:", count_of_3)



