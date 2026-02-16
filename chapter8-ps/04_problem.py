# Write a recursive function to calculate the sum of first n natural numbers.

def sum_n(n):
    if n <= 1:
        return n
    return n + sum_n(n - 1)

n = int(input("Enter a number: "))
print("Sum is:", sum_n(n))