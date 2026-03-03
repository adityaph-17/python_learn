# Type definitions mean telling Python what type of data a variable should store.
# Python is dynamically typed, but we can give type hints.

name: str = "Aditya"
age: int = 20
price: float = 99.5
is_pass: bool = True

print(f"{type(name)}\n{type(age)}\n{type(price)}\n{type(is_pass)}\n")
# They do NOT stop wrong values at runtime
# They are mainly for: Readability, IDE help , Static type checking

# Function Type Definitions:
def add(a: int, b: int) -> int:
    return a + b

print(f"sum is : {add(5,3)}")