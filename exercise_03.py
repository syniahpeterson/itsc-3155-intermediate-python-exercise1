# Syniah Peterson

from collections import Counter
# Creates a function that keeps count of each letter in the string after making all the letters lowercase and removing any spaces
def dictionary(string):
    lower_letters = []
    letters = list(string)
    for i in letters:
        lower_letters.append(i.lower())
        if i == ' ':
            lower_letters.remove(i)
    userDictionary = Counter(lower_letters)
    return userDictionary

userString = input("Enter a string: ")
user_dictionary = dictionary(userString)
print("Dictionary: " + str(user_dictionary))