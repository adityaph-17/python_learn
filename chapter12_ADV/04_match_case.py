# MATCH CASE
# Introduced in Python 3.10
# It is like switch-case in other languages

day = int(input("enter a day:"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")