# Input marks from the user
marks = int(input("Enter the marks (0-100): "))

# Check grade based on given scheme
if marks >= 90 and marks <= 100:
    grade = "Ex"
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 60 and marks < 70:
    grade = "C"
elif marks >= 50 and marks < 60:
    grade = "D"
else:
    grade = "F"

# Output
print("Grade:", grade)