# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if (a>b and a>c):
        return f"a is greater then b and c :{a}"
    elif(b>a and b>c):
        return f"b is greater then a and c :{b}"
    else:
        return f"c is gerater than a and b :{c}"
    
print(greatest(3,6,7))


