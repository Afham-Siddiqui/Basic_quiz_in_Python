import time

true = ["T", "t", "True", "true"]
false = ["F", "f", "False", "false"]
correct = 0  # Storing the correct answers

name = input("What's your name?")  # Storing the user's name

print("\nOK, " + name + ", let's get started.")
time.sleep(2)

print("Remember, the following answers are only True or False.")
time.sleep(2)

print("\nParis is the captial of France.")
choice = input(">>> ")
if choice in true:
    correct += 1  # If correct, the user gets one point
else:
    correct += 0

print("\nEngland is an island.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\nNorthern Ireland isn't part of Great Britian.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\nAndorra is between France and Spain.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\nIran use to be part of the Perisan Empire.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\nTurkmenistan isn't a real country.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\nYou're finished, " + name + ". You got", correct, "out of 6 correct.")