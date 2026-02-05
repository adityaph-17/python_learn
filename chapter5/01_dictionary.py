# dictionary example

marks = {
    "a":85,
    "b":90,
    "c":78,
    "d":92,
    "e":88,
    "f":76,
    "list": (1,2,3,4,5)
      }

print("Marks of students:", marks) # print the entire dictionary
print(marks.items()) # print all key-value pairs as tuples
print("Type of marks:", type(marks)) # print the type of marks

print (marks["list"]) # print the value of key "list"




# keys are unique in a dictionary
print(marks.keys()) # print all keys in the dictionary

# values are not unique in a dictionary
print(marks.values()) # print all values in the dictionary

# upadating value of a key
marks["a"] = 95
print("Updated Marks of students:", marks)

# adding a new key-value pair
marks["g"] = 80
print("Updated Marks of students after adding g:", marks)

# updating and adding using update() method
marks.update({"b": 100, "h": 70})
print("Marks of students after update():", marks)

# get() method to access value
print(marks.get("c")) # prints value of key "c"
print(marks["c"]) # prints value of key "c" but will raise KeyError if key not found


# # Accessing values using keys
# print("Marks of student a:", marks["a"])
# print("Marks of student d:", marks["d"])

# # Adding a new key-value pair
# marks["g"] = 80
# print("Updated Marks of students:", marks)

# # Modifying an existing value
# marks["b"] = 95
# print("Modified Marks of students:", marks)

# # pop() method to remove a key-value pair

removed_mark = marks.pop("f")
print("Removed mark of student f:", removed_mark)

print("Marks of students after removing f:", marks)

# # popitem() method to remove the last inserted key-value pair
last_item = marks.popitem()
print("Removed last item:", last_item)
print("Marks of students after popitem():", marks)




# empty dictionary
# s = {}
# print("Empty dictionary:", s)
