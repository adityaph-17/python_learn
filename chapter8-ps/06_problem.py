# Write a python function which converts inches to cms.

def inch_to_cms(inch):
    return inch * 2.54

inch = float(input("Enter a inch that have to convert to centimeters :"))
print(inch_to_cms(inch))