# 1. Create two virtual environments, install few packages in the first one. How do you
# create a similar environment in the second one?

# Shortcut (Better Method – Python built-in)
# Since you are using Python 3.14, you can create venv without installing virtualenv:

# python3 -m venv env1

# Activate it (macOS/Linux):
# source env1/bin/activate

# Install Some Packages
# pip install numpy
# pip install requests

# Export Installed Packages
# Create a requirements file:

# pip freeze > requirements.txt
# requirements.txt:
# numpy==2.0.0
# requests==2.31.0

# Step 4: Create Second Virtual Environment
# python3 -m venv env2
# Activate it:
# source env2/bin/activate
# Step 5: Install Same Packages in env2
# pip install -r requirements.txt
# Now env2 will have the same packages as env1.

