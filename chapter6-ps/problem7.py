# Input post from the user
post = input("Enter the post: ")

# Convert to lowercase for case-insensitive check
post = post.lower()

# Check if 'harry' is present
if "harry" in post:
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")