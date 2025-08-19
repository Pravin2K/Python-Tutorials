#Q. What is string?
'''
In Python, a string is a sequence of characters used to represent text. 
a string is an immutable sequence of Unicode characters. 
the sequence of characters is included within single, double or triple quotes in its literal representation
'''

#. You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("My name is John, i'm from US.")


#. You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#. Since strings are arrays, we can loop through the characters in a string, with a for loop.
fruit = 'Banana'
for i in fruit:
    print(i)


#. To get the length of a string, use the len() function.
name = 'John Cena'
print(len(name))  #Output : 9


#. To check if a certain phrase or character is present in a string, we can use the keyword in.
story= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print('tempor' in story)  #Output : True


#. To check if a certain phrase or character is present in a string, we can use the keyword in.
#Check if "free" is present in the following text:
txt = 'The best thing in life are free!'
if 'free' in txt:
    print(True)
else:
    print(False)  #Output : True




#########################################**Slicing**#########################################
#Q. What is Slicing in string?
'''
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
'''
#. Example : Get the characters from position 2 to position 5 (not included):
#Note: The first character has index 0.
var = "Hello, World!"
print(var[2 : 5]) #Output : llo


#. Get the characters from the start to position 5 (not included):
var1 = 'Hello, World!'
print(var1[0 : 5]) #or
print(var1[0 : 5]) #Output : Hello


#. Get the characters from position 2, and all the way to the end:
var2 = 'Hello, World!'
print(var2[2 : ]) #Output : llo, World!


#. Use negative indexes to start the slice from the end of the string:
var3 = 'Hello, World!'
print(var3[-5 : -2]) #Output : orl
'''
Index:  0  1  2  3  4  5  6  7  8  9 10 11 12
Letter:  H  e  l  l  o  ,     W  o  r  l  d  !
NegIdx: -13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
Slicing: b[-5:-2]
This uses negative indices to slice the string.

-5 corresponds to the character at index 8: 'o'
-2 corresponds to the character at index 11: 'd'
So b[-5:-2] extracts characters from index 8 to index 10 (not including index 11):

Index 8: 'o'
Index 9: 'r'
Index 10: 'l'
Result: 'orl'
'''



############################***Modify Strings***###########################
#Q. upper(): The upper() method returns the string in upper case.
a = "Hello, World!"
print(a.upper())  #Output : HELLO, WORLD!


#Q. lower(): The lower() method returns the string in lower case.
b = "Hello, World!"
print(b.lower()) #Output : hello, world!


#Q. How to remove whitespace?
'''
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
The strip() method removes any whitespace from the beginning or the end:
'''
#. Example :
c = " Hello, World! "
print(c.strip()) #Output : "Hello, World!"


#Q. Replace string:
'''The replace() method replaces a string with another string:'''
#. Example : Replace "World" to "John"
d = "Hello, World!"
print(d.replace("World", "John"))  #Output : Hello, John!


#Q. Split String : 
'''The split() method returns a list where the text between the specified separator becomes the list items.'''
#Example: The split() method splits the string into substrings if it finds instances of the separator:
e = 'Hello World!'
print(e.split(",")) #Output : ['Hello World!']





###########################***String Concatnation***#########################
#Q. String Concatenation : 
'''String concatenation in Python is the operation of joining two or more strings together.
To concatenate, or combine, two strings you can use the + operator.'''
#. Example : Merge variable x with variable y into variable z:
x = 'Hello'
y = 'India!'
z = x + y
print(z) #Output : HelloIndia!

#. Example : To add a space between them, add a " ":
x = 'Hello'
y = 'India!'
z = x + " " + y
print(z) #Output : Hello India!





#####################***String Format***#########################
#Q. String Formating : 
'''
String formatting in Python is the process of building a string representation dynamically by inserting the 
value of numeric expressions in an already existing string. Python's string concatenation operator doesn't 
accept a non-string operand. Hence, Python offers following string formatting techniques −

Using % operator
Using format() method of str class
Using f-string
Using String Template class
'''
#. As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
'''age = 36
txt = "My name is John, I am " + age
print(txt)
But we can combine strings and numbers by using f-strings or the format() method!
'''
#. Example : Create an f-string:
age = 29
print(f"my name is John, i am {age}") #Output : my name is John, i am 29


