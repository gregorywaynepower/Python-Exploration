# print("Hello!")

# Below code emits sounds, little rabbit hole from having found out about the "ASCII Bell" character, which should emit an alert. I couldn't get that to work, so we have lines 5 through 12, which work.

# import winsound
# import time
# duration_short = 100  # milliseconds
# duration_long = 300  # milliseconds
# freq = 400  # Hz

# winsound.Beep(freq, duration_short)
# winsound.Beep(freq, duration_long)
# winsound.Beep(freq, duration_short)



# Learned that multiline comments don't exist in Python. We have the beauty of word-wrap in VS Code though.

# Certain ways we should name variables. Variables must start with a letter or an underscore, NO STARTING WITH SYMBOLS. We can use letters, numbers, or underscores. STILL NO SYMBOlS. Variable names are case-sensitve. Reason why you can't assign values to symbols, is that they function as operators within Python.

# Naming conventions: Most variables should be "snake_case", "CAPITAL_SNAKE_CASE" usually refers to constants (Like PI), UpperCamelCase is usually used for classes, and __double_underscored_variables__ also called __dunder__ means that you should not touch the variables.

# Data Types: One thing to note, "dict" data types are similar to an "Object" in Javascript

# Note on bools, the values must be "True" or "False" no lowercase.
# Strings: an array of characters within single or double quotes.

#What the Heck is Dynamic Typing: It allows us to change variable to different types. A note on the "None" type, to compare this to JavaScript, it would be comparable to "null". The reason that I say "null" instead of "undefined", even though the interepreter will also throw you "undefined", "None" and "null" would still be put there by the developer, unlike "undefined" which is something that exists within any Object in JavaScript.

#What is statically typed then? So, an example in C++ or C, which are what Python's core is. In those languages, a variable must be assigned as a data type when they are instantiated. For example, look below:
#int not_awesomeness = 5;
#not_awesomeness = "cool"; <-- This would throw an error because we are trying to assign a different data type.

# Double VS. Single Quotes: You can use either, just make sure you're consistent. You can use double quotes inside quotes, but you have to escape them.
# Escaping quotation marks in strings "Little Billy said 'I want to get the bag one day too!' But Little Billy did not put in the hard work." As long as you switch between single within double quotes, or double quotes within single quotes.

# Escape Sequences, A.K.A Escape Characters!
# Note: You must put the escape characters within print().
# Important one is "\n" - Which creates a newline.
# Important one is "\'" - Which lets you continue on with a string, if necessary.
# Example, if you use the "\b" - Which simulates a backspace in the middle of a string. If you simply call backspace, when "backspace = 'HEL\bLO"; You get 'HEL\x08LO'. If you put in print(backspace) when "backspace = 'HEL\bLO"; You get 'HELO'.

# String Concatenation, adding two strings together. He also uses this as an opportunity to introduce "+=, -=, /= and *=" which let you increment, decrement, divide, or multiply by an amount after the assignment operator (equal sign). This cannot be done on literals (try assigning to a value to a variable).

# String Formatting
# New way (as of Python 3.6) way to interpolate, or insert stuff into strings.
# So it starts with an f and the string has double quotes, you insert variables with curly braces.
# Example:
    # x = 10
    # formatted = f"I've told you {x} times already!"
# This is one way that you can do stuff, like calculations and then slap that shit into a string.
# Older way (Python 2 to version Python 3.5) is to use the .format method
    # Example:
        # x = 10
        # formatted = "I've told you {} times already!".format(10)
    # Coding Example:
        # first = "Greatest"
        # last = "Ever"
        # formatted = "First Name: {}, Last Name: {}".format(first, last)

# Strings and Indexes
    # Colt talks about how words are just an array of characters.

# Converting Data Types
    # number = 12
    # type(number) --> This prints "<class 'int'>"
    # 8 natively, converts into an integer. But we can force it to become a string by using str().
    # str(8) --> Prints '8'
    # You can accidentally change str or int into variables that hold values, effectively breaking these functions if you are not careful (e.i. str = 13 would break these keywords)

# Building a Mileage Convertor with User Input
    # You can ask for user input by using input()
# print("How many kilometers did you struggle to bike today?")
# kms = input()
# miles = float(kms)/1.6094
# rounded_miles = round(miles, 2)
# print(f"Your {kms} kilometer ride converts to + {rounded_miles} miles.")

# SECTION 8: Boolean and Conditional Logic
    # Section Introduction and Objectives
    
    # Getting User Input:
        # input() prompts the user to put in information from the command line.
        # The second of these two code examples is a lot cleaner and prevents errors by having everything the input be on its own line, instead of being smashed onto the end of the printed statement.
        # -------------------------------------------
        # data = input("What's your favorite color?")
        # print("You said " + data)
        # -------------------------------------------
        # print("What's your favorite color?")
        # data = input()                              
        # print("You said " + data)
        # -------------------------------------------

    # Intro to Conditionas:
        # Python is indentation sensitive.
        # Code Example:
            # name = "Little Billy"
            # if name == "Arya Stark":
            #     print("Valar Morghulis, which means 'All men will die.'")
            # elif name == "Jon Snow":
            #     print("You know nothing.")
            # else:
            #     print("Carry on, peasant.")

        # Another Code Exercise:
            # # NO TOUCHING PLEASE---------------
            # from random import randint
            # choice = randint(1,10)
            # # NO TOUCHING PLEASE---------------

            # # YOUR CODE GOES HERE:
            # if choice == 7:
            #     print("lucky")
            # elif choice != 7:
            #     print("unlucky")

        # Another Code Exercise:
            # # NO TOUCHING ======================================
            # from random import randint
            # num = randint(1, 1000) #picks random number from 1-1000
            # # NO TOUCHING ======================================



            # # YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

            # if num%2 == 0:
            #     print("even")
            # if num%2 == 1:
            #     print("odd")

            # # YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # Section 9: Rock, Paper, Scissors

    # Section 10: Looping in Python:
        #83. The Basics of For Loops:
            # For loops are written like this

                # for itme in iterable_object:
                    # Do something with the item
            
            # An iterable object ios some kind of collection of items, for instance: a list of number, a string of characters, a range, etc.
            # Items: a new variable that can be called whatever you want
            # "item" references the current position of our _iterator_ within the iterable. It will iterate over (run through) every item of the collection and then go away when it has visited all items.

# for x in range(1, 10):
#     print(x)

# for letter in "coffee":
#     print(letter*3)
        
        #84. Exploring Ranges in Depth
            # ranges are typically used in for loops. A range is a slice of the number line.
                # range(7) goes up to 0 to 6 inclusive
                # range(1,8) will give you integers from 1 to 7
                # range(1, 10, 2) will give you odds from 1 to 10 the third parameter is the "step" meaning how many to skip. Also, which way to count up + or down -.
                # Introduces "list()", which prints the array, instead of just printing every individiual number.
        #84 Quiz:
            # Printing rnage doe snot print out all the numbers in the range. We have to iterate over the range with a loop to print the numbers.
                # numbs = range(1,5)
                # print(nums)
                    # >>> range(1,5)
        # 85. Solution
# # Add up all odd numbers between 10 and 20
# # Store the result in x:
# x = 0

# # YOUR CODE GOES HERE:

# for i in range(11,21,2):
#         x += i

# ====== ALTERNATE SOLUTION =============

# # Add up all odd numbers between 10 and 20
# # Store the result in x:
# x = 0
 
 
# # YOUR CODE GOES HERE:
# for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
#     if n % 2 != 0:
#         x += n

        # 86. Screaming Repeating
            # My Code Example

# print("How many times do I have to tell you?")
# x = input()
# print("Clean your room!\n"*int(x))

#             # Another Solution

# times = input("How many times to I have to tell you? ")
# times = int(times)

# for time in range(times):
#     print(f"{time+1}th Time I said: Clean up your room!")

        # 87. Exercise: Unlucky Numbers
# for i in range(20):
#     i = i+1
#     if i == 4:
#         print(str(i) + " is Unlucky!")
#     elif i == 13:
#         print(str(i) + " is Unlucky!")
#     elif i%2 == 0:
#         print(str(i) + " is even!")
#     elif i%2 == 1:
#         print(str(i) + " is odd!")

#         # Another Solution
# for num in range(1,21):
#     if num == 4 or num == 13:
#         state = "unlucky"
#     elif num % 2 == 0 :
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{num} is {state}!")

        # 88. Introducing While Loops

        # We can also iterate using a while loop, which has a different format

# # 102. 

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# # Define your code below:

# result = ("".join(sounds).upper())
# print(result)

# 104. List Methods: Append, Insert and Extend

# Create a list called instructors

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

# Run the tests to make sure you've done this correctly!

instructors = []
instructors.extend(["Colt", "Blue", "Lisa"])
print(instructors)