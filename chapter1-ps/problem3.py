'''installed external module pyttsx3 using pip3 install pyttsx3 command'''

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 50)   # Speed of speech
engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)

# Test message
engine.say("Hello Aditya! Your pyttsx3 installation is working perfectly.")

# Run the speech
engine.runAndWait()

print("pyttsx3 test completed ✅")