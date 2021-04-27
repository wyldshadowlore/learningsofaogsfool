"""
Here are examples of code and how to use it.
"""

#Standard print function
print("This is a note")  

#Define a string
aString = "This is a string"
print(aString)

#To add notes to the same line.
aString = "This is the start of a string, "
bString = "and this continues it."

print(aString)
print(bString) # you see these are on separate lines...

print(aString, end = ' ') #The end function will prevent a new line from being created.
print(bString) # This should be appended to the previous string.

#Printing the same message more than once.
aString = "Na "
bString = "Batman."
print(aString * 8, end = ' ')
print(bString)
