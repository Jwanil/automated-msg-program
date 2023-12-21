import pywhatkit
import random


# Define an array of strings
string_array = ["apple", "banana", "orange","watermelon","guvava"]

# Assign a random string from the array to a variable

random.shuffle(string_array)

#set how many times you want to send the messages in shuffle
for i in range(4):
    #sends the shuffled string once
    for j in string_array:
        pywhatkit.sendwhatmsg_instantly("+919925228832", j, 15, True, 4)


