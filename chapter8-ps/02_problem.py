# Write a python program using function to convert Celsius to Fahrenheit.

def c_to_f(c):
    return (c * 9/5) + 32

c = float(input("Enter Celsius: "))
f = c_to_f(c)
print(f"{c}°C = {f:.2f}°F")