# Recursion is a process where a function calls itself repeatedly until a certain condition is satisfied.

# Every recursive function must have two main parts:

# Base Case
# The condition where the function stops calling itself
# Prevents infinite recursion

# Recursive Case
# The part where the function calls itself
# Works toward the base case


def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n-1)  # Recursive call
n = int(input("enter a number for factorial :"))
print(f"Factorial of {n} is {factorial(n)}")

# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120

