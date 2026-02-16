# in this we using write function to perform write operation 

# To write in a file, we use mode "w".

f = open("demo_write.txt", "w")
f.write("Hello Aditya")

str = " hi i am aditya learning python language\n"
f.write(str)
f.close()

# If file exists Old data is deleted
# If file does not exist New file is created 

