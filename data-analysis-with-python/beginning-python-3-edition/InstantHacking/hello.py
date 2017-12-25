__author__ = 'ibmdev'
# Import of library cmath to manage Complex Numbers
import cmath

print('Hello, World')
x = cmath.sqrt(-5)
print("The square root of -5 yields : " + str(x))
# Supply a value and assign it to a variable
# firstname = input("What is your firstname ? ")
# print("Your firstname is : " + firstname)
# input("Thanks, click <enter> to finish the program")
# Representation of strings with simple and double quotes
print('My first string with simple quotes')
print("My first string with double quotes")
print('My second "string" with a quote into my sentence')
# When we add a backslash character before a single/double quote, Python understands that the middle single quote is a character in the string and not the end of the string.
print('My third string with an backslash character and simple quotes let\'s go ')
print('My fourth string with an backslash character and double quotes \"Hello, World\" ')
print('Let\'s say "Hello World" to Cozmo Robot"')
# Concatenation of strings
print('Let\'s say ' + '"Hello World" to Cozmo Robot')
# Functions str and repr
line1 = str('Hello,\n' + 'World')
line2 = repr('Hello \n' + 'World')
print('line 1 :  ' + line1)
print('line 2 : ' + line2)
# The next tutorial : Long Strings, Raw Strings, and bytes
