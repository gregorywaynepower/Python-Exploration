# The Modern Python 3 Bootcamp

Learned that multiline comments don't exist in Python. We have the beauty of word-wrap in VS Code though.

Certain ways we should name variables. Variables must start with a letter or an underscore, NO STARTING WITH SYMBOLS. We can use letters, numbers, or underscores. STILL NO SYMBOlS. Variable names are case-sensitve. Reason why you can't assign values to symbols, is that they function as operators within Python.

Naming conventions: Most variables should be "snake_case", "CAPITAL_SNAKE_CASE" usually refers to constants (Like PI), UpperCamelCase is usually used for classes, and __double_underscored_variables__ also called __dunder__ means that you should not touch the variables.

Data Types: One thing to note, "dict" data types are similar to an "Object" in Javascript

Note on bools, the values must be "True" or "False" no lowercase.
Strings: an array of characters within single or double quotes.

What the Heck is Dynamic Typing: It allows us to change variable to different types. A note on the "None" type, to compare this to JavaScript, it would be comparable to "null". The reason that I say "null" instead of "undefined", even though the interepreter will also throw you "undefined", "None" and "null" would still be put there by the developer, unlike "undefined" which is something that exists within any Object in JavaScript.

What is statically typed then? So, an example in C++ or C, which are what Python's core is. In those languages, a variable must be assigned as a data type when they are instantiated. For example, look below:

int not_awesomeness = 5;

not_awesomeness = "cool"; <-- This would throw an error because we are trying to assign a different data type.

Double VS. Single Quotes: You can use either, just make sure you're consistent. You can use double quotes inside quotes, but you have to escape them.

Escaping quotation marks in strings "Little Billy said 'I want to get the bag one day too!' But Little Billy did not put in the hard work." As long as you switch between single within double quotes, or double quotes within single quotes.

## Escape Sequences, A.K.A Escape Characters

Note: You must put the escape characters within print().
Important one is "\n" - Which creates a newline.
Important one is "\'" - Which lets you continue on with a string, if necessary.
Example, if you use the "\b" - Which simulates a backspace in the middle of a string. If you simply call backspace, when "backspace = 'HEL\bLO"; You get 'HEL\x08LO'. If you put in print(backspace) when "backspace = 'HEL\bLO"; You get 'HELO'.

String Concatenation, adding two strings together. He also uses this as an opportunity to introduce "+=, -=, /= and *=" which let you increment, decrement, divide, or multiply by an amount after the assignment operator (equal sign). This cannot be done on literals (try assigning to a value to a variable).

## String Formatting

New way (as of Python 3.6) way to interpolate, or insert stuff into strings.
So it starts with an f and the string has double quotes, you insert variables with curly braces.

Example:

    x = 10
    formatted = f"I've told you {x} times already!"

### This is one way that you can do stuff, like calculations and then slap that shit into a string

### Older way (Python 2 to version Python 3.5) is to use the .format method

    Example:

        x = 10
        formatted = "I've told you {} times already!".format(10)

    Coding Example:

        first = "Greatest"
        last = "Ever"
        formatted = "First Name: {}, Last Name: {}".format(first, last)

### Strings and Indexes

    Colt talks about how words are just an array of characters.

### Converting Data Types

    number = 12
    type(number) --> This prints "<class 'int'>"
    8 natively, converts into an integer. But we can force it to become a string by using str().
    str(8) --> Prints '8'
    You can accidentally change str or int into variables that hold values, effectively breaking these functions if you are not careful (e.i. str = 13 would break these keywords)

### Building a Mileage Convertor with User Input

You can ask for user input by using input()

    print("How many kilometers did you struggle to bike today?")
    kms = input()
    miles = float(kms)/1.6094
    rounded_miles = round(miles, 2)
    print(f"Your {kms} kilometer ride converts to + {rounded_miles} miles.")

___

## SECTION 8: Boolean and Conditional Logic

### Section Introduction and Objectives

### Getting User Input

    input()
    prompts the user to put in information from the command line.
    The second of these two code examples is a lot cleaner and prevents errors by having everything the input be on its own line, instead of being smashed onto the end of the printed statement.
    -------------------------------------------
    data = input("What's your favorite color?")
    print("You said " + data)
    -------------------------------------------
    print("What's your favorite color?")
    data = input()
    print("You said " + data)
    -------------------------------------------

### Intro to Conditionals

Python is indentation sensitive.
Code Example:

    name = "Little Billy"
    if name == "Arya Stark":
    print("Valar Morghulis, which means 'All men will die.'")
    elif name == "Jon Snow":
    print("You know nothing.")
    else:
    print("Carry on, peasant.")

### Another Code Exercise

    # NO TOUCHING PLEASE---------------
    from random import randint
    choice = randint(1,10)
    # NO TOUCHING PLEASE---------------

    # YOUR CODE GOES HERE:
    if choice == 7:
    print("lucky")
    elif choice != 7:
    print("unlucky")

### Second Code Exercise

    # NO TOUCHING ======================================
    from random import randint
    num = randint(1, 1000) #picks random number from 1-1000
    # NO TOUCHING ======================================

    # YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

    if num%2 == 0:
        print("even")
    if num%2 == 1:
        print("odd")

    # YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

___

## Section 9: Rock, Paper, Scissors

- Go to Rock_Paper_Scissors_Game Directory
- Look into Python

___

## Section 10: Looping in Python

### 83. The Basics of For Loops

    For loops are written like this

        # for itme in iterable_object:
            # Do something with the item
    
    An iterable object ios some kind of collection of items, for instance: a list of number, a string of characters, a range, etc.

    Items: a new variable that can be called whatever you want
    "item" references the current position of our _iterator_ within the iterable. It will iterate over (run through) every item of the collection and then go away when it has visited all items.

### 88. Introducing While Loops

    We can also iterate using a while loop, which has a different format.

### 89. Introducing While Loops

___

## Section 12: Lists

### 97. Intro to Lists and Objectives

A list is a collection or grouping of items.

- Describe, create and access a list data structure
- Use built in methods tomodify and copy lists
- Iterate over lists using loops and list comprehensions
- Work with nested lists to build more complex data structures

### 98. Creating Lists

    array = []
    taskNumbers = list(range(1,4))
    Outputs: [1, 2, 3]

### 99. Code Example

    # Define my_stuff 
    my_stuff = [1.0, "is", "a", "float"]
    # Define nums 
    nums = list(range(1,100))

### 100. Accessing Data in Lists

You can use negative index values to retrieve values from the end of a list:

    friends  = ["Billy", "Cas", "James"]
    print(friends[-1]) # "James"
    print(friends[-4]) # IndexError

Seeing if a value is in a list!
You can use **in** and it will return a Boolean value.

### 101. Changing Values in Lists

    # DON'T TOUCH THIS PLEASE!
    people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
    # DON'T TOUCH THIS PLEASE!
    #Change "Hanna" to "Hanna"
    people[0] = "Hannah"
    #Change "Geoffrey" to "Jeffrey"
    people[4] = "Jeffrey"
    #Change "aparna" to "Aparna" (capitalize it)
    people[-1] = "Aparna"

### 102. Iterating Over Lists

#### For Loop Way

    array = [1, 3, 4]
    for arbitraryVariable in array:
        print(arbitraryVariable)

#### While Loop Way

    array = [1, 3, 4]
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

#### List with String Templating

    colors = ["magenta", "green", "orange", "red"]
    index = 0
    while index < len(colors):
        print(f"{index}: colors[index])
        index += 1

### 103. Coding Exercise

#### My Solution

    sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

    # Define your code below:

    result = ("".join(sounds).upper())
    print(result)

    # Outputs: "SUPERCALIFRAGILISTICEXPIALIDOCIOUS"

#### Their Solutions

##### Capitlizing Each String

    sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
    # Define your code below:
    result = ''
    for s in sounds:
        result += s.upper()

##### Add all strings to a result and capitalize it at the end

    sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
    
    # Define your code below:
    result = ''
    for s in sounds:
        result += s
    result = result.upper()

### 104. List Methods: Append, Insert, and Extend

#### Difference Between Functions and Methods

Functions are free-floating whereas methods are functions attached to an object (i.e. list, tuple, ect.)

- list.append(item) - Adds one and only one item to the end of a list.
- list.extend(item(s)) - Adds all of the items passed through the method to the list. Can be used to join to lists seamlessly.
- list.insert(index, item(s)) - Lets you seamlessly add items to list.

### Coding Exercise

    # Create a list called instructors

    # Add the following strings to the instructors list 
        # "Colt"
        # "Blue"
        # "Lisa"

    # Run the tests to make sure you've done this correctly!

    instructors = []
    instructors.extend(["Colt", "Blue", "Lisa"])
    print(instructors)

    Returns: ["Colt", "Blue", "Lisa"]

### Their Solution

    # Create a list called instructors
    instructors = []
    # Add the following strings to the instructors list 
        # "Colt"
        # "Blue"
        # "Lisa"
    
    instructors.append("Colt")
    instructors.append("Blue")
    instructors.append("Lisa")

### 106. List Methods: Clear, Pop, and Remove

- list.clear() - Removes all items from a list, leaving an empty list.
- list.pop() - Pops off the last item in a list by default, but you can pass a number and it will remove the item at the index that number is.
- list.remove() - It will remove the first item that matches what you pass. If it can't find the item you pass, then it will throw an error.

### 107. List Methods: Index, Count, Sort, Reverse, and Join

- list.index(item, start, end) - Returns the index of the specified item in the list. You can specifiy the start and end of where you want index to look for any given parameter.
- list.count(item) - Returns the number of time an item appears in a list. If an item isn't a list, it will return 0. Not crash like index()
- list.reverse(item) - Reverse the elements of the list.
- list.sort() - Sort the items of the list. You can customize the parameters (more on that later).
- "".join(list with strings) - It is more of a string method, used to combine a list of strings and return a new string. Whatever is in beteen the quotes, is inserted between each iterable in your list.

### 108. Coding Exercise

        # Create a list called instructors
    instructors = []
    # Add the following strings to the instructors list 
        # "Colt"
        # "Blue"
        # "Lisa"
    instructors.extend(["Colt", "Blue", "Lisa"])
    # Remove the last value in the list
    instructors.pop()
    # Remove the first value in the list
    instructors.pop(0)
    # Add the string "Done" to the beginning of the list
    instructors.insert(0, "Done")
    # Run the tests to make sure you've done this correctly!
    # Code passed tests.

### 109. Slices

Organized like this:

```list[start:end:step]```

Slices create new a new instance of the list, **meaning even though ```original_array == sliced_array``` will resolve to ```True```, ```original_array is sliced_array``` will resolve to  ```False```**

#### start Parameter

    python
    first_list = [1, 2, 3, 4]
    first_list[1:] = [2, 3, 4]
    # Positive slice starts from the front of the array.
    first_list[-2:] = [3, 4]
    # Negative slice starts from the back of the array, but -1 is first position, since -0 can't exist.

#### end Parameter

The slice: end parameter is exlusive, meaning we do not include the index we are counting up to.

    python
    first_list = [1, 2, 3, 4]
    first_list[:2] = [1, 2]
    first_list[:-1] = [1, 2, 3]
    # We are counting up to one element from the end.
    first_list[1:-1] = [2, 3]

#### step Parameter

The step is the number to count at a time. For example a step of 2 counts every other number.

    python
    first_list = [1, 2, 3, 4]
    first_list[::2] = [1, 3]

When step is a negative number, it means we are counting backwards.

    python
    first_list = [1, 2, 3, 4]
    first_list[::-2] = [4, 2]

#### Tricks with Slices

You can reverse lists and strings. You can also modify an existing list.

    python
    rappers = ["Kanye", "Freddie Gibbs", "J Dilla"]
    rappers[1:2] = ["MFDoom", "Common", "O.D.B"]
Here above is an example of modifying the record we are replacing "Freddie Gibbs" with "MF Doom" and adding the items "Common" and "O.D.B" after our new entry.

To add a list onto the end of an existing list ```rappers```, from our example above you would use ```rappers[len(rappers)] = ["Logic", "Logic Jr."]```, which would add your list items ```["Logic", "Logic Jr."]``` onto the end of the existing array.

### 110. Swapping Values in Lists

You can move values around lists by using the method below.

    names = ["James", "Jesse"]
    names[0], names[1] = names[1], names[0]
    print(names) = ["Jesse", "James"]

## Section 13: List Comprehensions

### 111. List Comprehension
