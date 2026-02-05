# in this file, we will explore basic string operations in Python

# Creating a string
name = "aditya"
print("Original String:", name)

# slicing in a string
sliced_name = name[0:4] # slices the string from index 0 to 3 it will not include index 4 and gives 'adi'
print("Sliced String (0 to 4):", sliced_name)

A = name[2:5] # slices the string from index 2 to 4 it will not include index 5 and gives 'ity'
print("Sliced String (2 to 5):", A)
B = name[:5] # slices the string from index 0 to 4 it will not include index 5 and gives 'adity'
print("Sliced String (:5):", B)
C = name[3:] # slices the string from index 3 to end (length) of the string and gives 'tya'
print("Sliced String (3:):", C)



# negative slicing in a string which is used to slice from the end of the string
neg_sliced_name = name[-4:-1] # slices the string from index -4 to -2 it will not include index -1 and gives 'ity'
print("Negative Sliced String (-4 to -1):", neg_sliced_name)
# # we can use corresponding positive index to understand negative slicing
# neg_sliced_name_1 = name[1:4] # slices the string from index 3 to 5 it will not include index 6 and gives 'ity'
# print("Corresponding Positive Sliced String (1 to 4):", neg_sliced_name_1)

skip = "0123456789"
#slicing with step skip
step_sliced_name = skip[0:6:2] # slices the string from index 0 to 5 with a step of 2 and gives '024'
print("Step Sliced String (0 to 6 with step 2):", step_sliced_name) # output: 024



