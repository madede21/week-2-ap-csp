
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it


# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.

# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."

##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

# print the length of the summary
# upper case the entire summary
# print the summary
# print the summary in lowercase
# replace the word blue with red
# print the summary
# string index the word beetle and print it out
# print the last word of the summary
# print the summary in reverse


##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.




# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it

# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.

print("Name: Joshua")
print("Name: Mateo")
print("Name: Alexandre")
print(f"date: 10/31/25")
favorite_movie = input("what is your favorite movie?")
print (f"my favorite movie is {favorite_movie}")   
# Print your name and age on separate lines using a single print() function.

print("Name: Joshua 17")
print("Name: Mateo 16")
print("Name: Alexandre 15")




# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."

##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print(f("In 10 years "))
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


# Movie Summary Challenge
blue_beetle_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."

# Print the length of the summary
print(len(blue_beetle_summary))

# Uppercase the entire summary
print("Uppercase:", blue_beetle_summary.upper())

# Print the summary
print(blue_beetle_summary)

# Print the summary in lowercase
print("Lowercase:", blue_beetle_summary.lower())

# Replace the word Blue with Red
new_beetle_summary = blue_beetle_summary.replace('Blue', 'Red')
print(new_beetle_summary)

# String index practice
print("First character:", blue_beetle_summary[0])
print("Last character:", blue_beetle_summary[-1])

# Print the last word of the summary
last_word = blue_beetle_summary.split()[-1]
print("Last word:", last_word)

# Print the summary in reverse
reversed_beetle_summary = blue_beetle_summary[::-1]
print(reversed_beetle_summary)

########################## Input Practice #############################################

# Input Practice #1
learning = input("What are you learning today? ")
print("You are learning:", learning)

# Input Practice #2
place = input("Where are you from? ")
print("You are from:", place)

# Input Practice #3
first_name = input("What is your name? ")
surname = input("What is your surname? ")
print("Your full name is:", first_name, surname)

# Exercise
name = input("What is your name? ")
fav_color = input("What is your favorite color? ")
print("Hello", name + "!", "Your favorite color is", fav_color + ".")






