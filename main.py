a = 200
b = 33

if (b > a):
  print("b is greater than a")
else:
    print("b is not greater than a")




# Ask the user for their age
# If they are younger than 13, tell them they can only watch PG/G Movies
# If they are 13 and older but younger than 17, they can only watch PG-13/PG/G movies
# IF they are 17 or older, they can watch all movies.

age = int(input("What is your age? "))
if(age < 13):
  print("You can only watch PG/G Movies")
elif(17 > age >= 13):
  print("That means you can watch PG-13 and below movies")
else:
  print("You can watch all movies")

is_Hungry = True
is_Sleepy = False
if(is_Hungry == True):
  print("You should go eat")
if(is_Sleepy == True):
  print("You should go sleep")
if(is_Sleepy == False):
  print("wow you're well rested")

# Ask the user for a number
# Tell the user if their number is even or odd

numEO = int(input("Give me a number: "))
if(numEO % 2 == 0):
  print("Your number is even")
else:
  print("Your number is odd")