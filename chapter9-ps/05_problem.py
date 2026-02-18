# Repeat program 4 for a list of such words to be censored.

words = ["donkey", "bad", "dirty"] #first list censord words 

with open ("txt_files/05_demo.txt", "r") as f : # then open the file and take in content variable
    content = f.read()

for word in words : #use loop and use replace function to replace with censord words 
    content = content.replace(word , "#" * len(word) )

with open ("txt_files/05_demo.txt", "w") as f : # now write file with chnages (content)
    f.write (content)



