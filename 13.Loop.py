#Q. What is loop?
'''
A loop is used to repeat a block of code multiple times until a condition is met or until all items in 
a sequence are processed.
Instead of writing the same code again and again, you can use loops.
'''


#Q. Types of Loops in Python
'''Python mainly has two types of loops:'''
#1. While loop
#2. for loop


#Q. While loop : -
'''With the help of while loop we execute the set of statement as long as a condition is true or when 
repeating until a condition is false.'''
#. Example : Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1   #Output : 1 2 3 4 5


#. Example : print the number 1 to 5.
number = 1
while i <= 5:
    print(number)
    number += 1


#. Example : print the number 5 to 1.
i = 5
while i >= 1:
    print(i)
    i -= 1    #Output :5 4 3 2 1





###############################***Practice***##############################
#Q. Print number from 1 to 100.
num = 1
while num <= 100:
    print(f'Num: {num}')
    num += 1


#Q. Print number from 100 to 1.
num = 100
while num >= 1:
    print(f'Num: {num}')
    num -= 1


#Q. Print the multiplication table of number n.
n = 1
while n <= 10:
    print(f'Table: {n*3}')
    n += 1


#Q. Print the elements of the following list using loop.
l1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(l1):
    print(l1[idx])
    idx += 1


#Q. Search for a number x in this tuple using loop.
t1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
idx = 0

while idx < len(t1):
    if x == t1[idx]:
        print("Data found")
    else: 
        print('finding')
    idx += 1
    
    