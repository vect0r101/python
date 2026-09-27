#01_printing string and number in one print statement:

#a_wrong way
x = 5
y = "John"
print(x + y)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

#b_right way
x = 5
y = "John"  
print(x, y)




#02_Variable names are not case-sensitive.
a = 5  
# is not the same as 
A = 5




#03_to check the type of a variable, we can use the type() function:
x = 5
print(type(x))  # Output: <class 'int'>




#04_to convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)  # Output: 1.0
print(b)  # Output: 2
print(c)  # Output: 1+0j

print(type(a))  # Output: <class 'float'>
print(type(b))  # Output: <class 'int'>
print(type(c))  # Output: <class 'complex'>





#05_Python does not have a built-in method for making a random number, but we can import the built-in random module to work with random numbers:
import random
print(random.randrange(1, 10))  # Output: a random number between 1 and 9 (inclusive)





#06_The input from the user is treated as a string, we can convert the input into a number with the float() function:

x = float(input("Enter a number: "))
print(x)  # Output: the number entered by the user





#07_finding the square root of a number:
import math

x = input("Enter a number:")

y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")





#08_The Python math module has a set of methods and constants that we can use to perform mathematical tasks:
import math

print(math.pi)  # Output: 3.141592653589793





#09_to round up and round down numbers, we can use the math.ceil() and math.floor() methods:
import math

x = 1.4
y = 1.7

print(math.ceil(x))  # Output: 2
print(math.floor(y))  # Output: 1




#10_different ways to write something power something else:
x = 2
y = 3
print(x ** y)  # Output: 8
print(pow(x, y))  # Output: 8





#11_Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

#a_right way
number = 15
if number > 0:
  print("The number is positive") # Output: The number is positive

"""
#b_wrong way
number = 15
if number > 0:
print("The number is positive") 
"""
# IndentationError: expected an indented block after 'if' statement on line 2





#12_The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".


#13_Else is when the thing from the if statement isn't true, Elif is like a second if statement




#14_Both elif and else are reached only when the previous condition(s) were false, but there's a key difference:
"""
elif checks another condition.
else doesn't check any condition; it just runs if everything above failed.
So elif means "otherwise, check this condition", while else means "otherwise, do this no matter what"
"""



#15_Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

#16_The else statement must come last. You cannot have an elif after an else.





#17_Logical operators are used to combine conditional statements. Python has three logical operators:

#and - Returns True if both statements are true
#or - Returns True if one of the statements is true
#not - Reverses the result, returns False if the result is true




#18_Like many other popular programming languages, strings in Python are arrays of unicode characters.

#However, Python does not have a character data type, a single character is simply a string with a length of 1.

#Square brackets can be used to access elements of the string.




#19_You can assign a multiline string to a variable by using three double quotes Or three single quotes:




#20_Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)



#21_To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt) 
# Output: True




#22_The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) 
# returns "Hello, World!"




#23_The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']






#24_To add a space between them, add a " ":

a = "Hello"
b = "World"
print(a + " " + b) 
# Output: Hello World






#25_we cannot combine strings and numbers like this:age = 36
#txt = "My name is John, I am " + age
#print(txt)
#This will produce an error because Python does not know how to concatenate a string and an integer.

#But we can combine strings and numbers by using f-strings or the format() method!
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.





#26_A placeholder can contain variables, operations, functions, and modifiers to format the value.

#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:




#27_A placeholder can contain Python code, like math operations:





#28_len() function also count spaces, punctuation, and special characters as part of the string.





#29_The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"



#30_With the while loop we can execute a set of statements as long as a condition is true.


