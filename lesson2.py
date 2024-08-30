#create a print function that prints
#out the string "Hello world"
print("Hello, World!")
# ask the user for the day of the week
# day_of_week = input ("What day of the week is it?")
# print("Today is"+ day_of_week)
# concatenation is when you add two strings together
# using a plus sign (+)
# movies_this_week = input ("What movies are you watching this week?")
# print("I am watching"+ movies_this_week + "this week")
# mood = input("How are you feeling today?")
# print("I am feeling"+ mood )

# data types for variables
# strings - text
name = "John" #this is a string data type
# whenever it is wrapped in quotes it is string
year = "2024"

# integers - whole numbers
year = 2024 # this is an integer data type
# does not need to be wrapped in quotes
yearFourFromNow = 2028
subtract = yearFourFromNow - year
print(subtract)

# floats - decimal numbers
priceBigMac = 3.99 # this is a float data type
priceDoublePounder = 4.99
totalPrice = priceBigMac + priceDoublePounder
print(totalPrice)

# booleans - True or False
isRaining = False # this is a boolean data type
print(isRaining)

# list - a collection of items
groceries = ["apples","bananas","carrots"]
print(groceries)

#challenge #1
#you and your family are going to a movie and
# dinner. You need a list of movies to choose from
# the place of the restaurant
name_of_restaraunt = "Nandos"
# the place of the restaurant
place_of_restraunt = "123 s cicero ave"
# the time of the movie
time_of_movie = "7:00PM"
# the time of the dinner
time_of_dinner= "5:00PM"
# the name of the movie
name_of_movie = "minions"
# the price of the dinner
price_of_dinner = 50.25
# check to see if the movie is playing in the evening
isEvening=True
# how many people are going
peopleGoing = input("how many people are going? ")
#type conversion converting from one data type to another
# print the entire output in one sentence
print("I am going to "+ name_of_restaraunt +
       " located at " + place_of_restraunt + 
       " at " + time_of_dinner + 
       " and afterwards heading to watch the " + name_of_movie +
         " at " + time_of_movie) 
