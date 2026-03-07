#  Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

# aditya@Adityas-MacBook-Air chapter13_ADV-ps % python3 -m venv adienv1

# aditya@Adityas-MacBook-Air chapter13_ADV-ps % source env1/bin/activate
# source: no such file or directory: env1/bin/activate

# aditya@Adityas-MacBook-Air chapter13_ADV-ps % source adienv1/bin/activate

# (adienv1) aditya@Adityas-MacBook-Air chapter13_ADV-ps % pip install numpy

# Collecting numpy
#   Using cached numpy-2.4.2-cp314-cp314-macosx_14_0_arm64.whl.metadata (6.6 kB)
# Using cached numpy-2.4.2-cp314-cp314-macosx_14_0_arm64.whl (5.2 MB)
# Installing collected packages: numpy
# Successfully installed numpy-2.4.2

# [notice] A new release of pip is available: 25.3 -> 26.0.1
# [notice] To update, run: pip install --upgrade pip

# (adienv1) aditya@Adityas-MacBook-Air chapter13_ADV-ps % 
# (adienv1) aditya@Adityas-MacBook-Air chapter13_ADV-ps % pip freeze > adienv1_requirements.txt
# (adienv1) aditya@Adityas-MacBook-Air chapter13_ADV-ps % 