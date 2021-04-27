"""
Here are examples of code and how to use it.
"""
"""
Print Function
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
print(aString * 8, end = '') #There is no space between the quotes here, otherwise there will be 2 spaces between the last Na and Batman.
print(bString)

"""
Loops
"""
#The way this function counts, if you want 10 of something, you need to add one.
for i in range(1, 11, 1):   #range(start, stop, step)  << Feel free to change these options.
  print(i, end = ' ')
  
for i in range(1 ,11, .25): #This will step in increments of .25
  print(i, end = ' ')  #This will prevent the script from taking up too many pages.

#A while loop will go forever, if the condition can never be met.
a = 0  #assign value
while a < 100:  
  print(a, end = ' ')
  a += 1  #will increment a by your set amount
  
"""
input function
"""
aString = input("Please guess a number 1 - 10 ") # how would you stop someone from entering letters?
print(f'You entered {aString}')

"""
If, elif, else
"""
print("A - is for apple")
print("B - is for banana")
print("C - is for carrot")
yourInput = input("Please choose A, B or C:")
if yourInput == "A" or yourInput == "a":
  print("You chose apple.")
elif yourInput == "B" or yourInput == "b":
  print("You chose banana.")
elif yourInput == "C" or yourInput == "c":
  print("You chose carrot.")
else:
  print("Sorry you're not hungry.")
  
"""
Creating it as a function
"""
#A basic function
def aFunction():  #This creates the function
  print("This is a function call")  #Normal Code
  
aFuction() #This calls the function

#Passing an arguement to a function

def aFunction(someStuff):  # pass an arguement to the function
  print(someStuff)  #print the passed arguement
  
userStuff = input("Please enter some stuff: ")  #get the user input
aFunction(userStuff)  #Pass the user arguement to the function.

#When the amount of arguments is unknown
def aFunction(**someJunk):
  print("This was passed from the function call: " + someJunk["junk2"])

aFunction(junk1 = "Some Junk 1", junk2 = "Some junk 2")
