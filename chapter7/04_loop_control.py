# Loop Control Statements

# break – stops the loop

for i in range(1, 6):
    if i == 3:
     break #break – stops the loop
    print(i)

print('\n')
# continue – skips current iteration
for i in range(1, 6):
    if i == 3:
     continue #continue – skips current iteration
    print(i)

print('\n')
# pass – does nothing (placeholder)
for i in range(11):
   pass