#Q. If else Statement.
'''
An if-else statement is a fundamental control structure in programming used to make decisions. 
It allows a program to execute different blocks of code depending on whether a condition is true or false.

Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.
'''

#Q. What is if statement:
'''Code to run if condition is True'''
#. Example :
a = 33
b = 200
if b > a:
    print('b is grater') #Output : b is grater




#Q. What is Elif?
'''
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
'''
#. Example : 
a = 22
b = 22
if a > b:
    print('a is grater than b.')
elif a == b:
    print('a is equal of b.') 
'''In this example a is equal to b, so the first condition is not true, but the elif condition is true, 
so we print to screen that "a and b are equal".'''




#Q. What is else ?
'''The else keyword catches anything which isn't caught by the preceding conditions or 
Code to run if condition is False'''
#. Example :
a = 200
b = 22
if b > a:
    print('b is grater than a.')
elif a == b:
    print('a is equal of b.')
else: 
    print('a is grater than b.') #Output : a is grater than b.



#. Example :Grade students marks.
marks = int(input("Enter your marks : "))
if marks >= 90:
    print('Grade : A')
elif marks >= 80 and marks <= 89:
    print('Grade : B')
elif marks >= 70 and marks <= 79:
    print("Grade : C")
else:
    print('Grade : D')


#. Check a number entered by the user os odd or even.
number = int(input('Enter number : '))
if number % 2 == 0:
    print("Even number")
else:
    print('Odd  number')


#. Find the greatest of 3 numbers entered by the users.
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))
n3 = int(input('Enter 3rd number : '))
if n1 > n2 and n1 > n3:
    print('N1 is grater')
elif n2 > n1 and n2 > n3:
    print('N2 is greater')
else:
    print('N3 is greater')




#Q. What is nested if ?
'''A nested if statement in Python means placing one if statement inside another. It allows you to check a 
secondary condition only if the first one is true.'''
#. Example : 
age = 20
has_id = True
if age >= 18:
    if has_id:
        print('You can inter the club.')
    else:
        print('You need an id to enter the club.')
else:
    print('You are too young to enter the club.') #Output : You can inter the club.


