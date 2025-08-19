#Q. What is Tuple?
'''
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
'''

#. Example : Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple) #Output : ('apple', 'banana', 'cherry')



#Q.Create Tuple With One Item
'''To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not 
recognize it as a tuple.'''
#. Example : 
thistuple = ('Apple',)
print(thistuple) #Output : ('Apple',)



#Q. Create a tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1) #Output : ('abc', 34, True, 40, 'male')



#Q. The tuple() Constructor.
'''It is also possible to use the tuple() constructor to make a tuple.'''
#. Example : Using the tuple() method to make a tuple:
thistuple = tuple(('Apple', 1, 2.0, True))
print(thistuple)  #Output : ('Apple', 1, 2.0, True)






#####################***Tuple Length***###################
#Q. Tuple Length.
'''To determine how many items a tuple has, use the len() function.'''
#. Example : Print the item of number in tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #Output : 3






##########################***Python - Access Tuple Items***########################
#Q. Access Tuple Items
'''You can access tuple items by referring to the index number, inside square brackets.'''
#. Example  : Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  #OUtput : banana



#Q. Negative Indexing
'''Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.'''
#. Example : Print the last item of the tuple:
thistuple = ('Apple', 'Banana', 'Cherry')
print(thistuple[-1]) #Output : Cherry



#Q. Range of indexed:
'''
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.
'''
#. Example : Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2 : 5]) #Output : ('cherry', 'orange', 'kiwi')


#. Example :This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[: 4]) #output : ('apple', 'banana', 'cherry', 'orange')


#. Example : This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-5 :]) #Output : ('cherry', 'orange', 'kiwi', 'melon', 'mango')



#Q. Check if item is exist.
'''To determine if a specified item is present in a tuple use the in keyword.'''
#. Example : Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if 'apple' in thistuple:
    print('Available')
else:
    print('Not found') #Output : Available







#######################***Python - Update Tuples***##########################
#Q. Change Tuple Values.
'''Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
But there are some workarounds. You can convert the tuple into a list, change the list, and convert the list
back into a tuple.'''
#. Example : Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[2] = 'Kiwi'
x = tuple(y)
print(x)  #Output : ('apple', 'banana', 'Kiwi')



#Q. Add items in tuple.
'''
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items 
to a tuple.
'''

'''1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add 
your item(s), and convert it back into a tuple.'''
#. Example : Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
thislist = list(thistuple)
thislist.append('orange')
thistuple = tuple(thislist)
print(thistuple)  #Output : ('apple', 'banana', 'cherry', 'orange')


'''2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many),
create a new tuple with the item(s), and add it to the existing tuple:'''
#. Example : Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ('orange',)
x = thistuple + y
print(x)  #Output : ('apple', 'banana', 'cherry', 'orange')



#Q. Remove items : 
'''Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used 
for changing and adding tuple items.'''
#Example : Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
thislist = list(thistuple)
thislist.pop(0)
thistuple = tuple(thislist)
print(thistuple) #Output : ('banana', 'cherry')


#. Example : The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple





#################################***Python - Unpack Tuples##################################
#Q. Unpacking a Tuple
'''When we create a tuple, we normally assign values to it. This is called "packing" a tuple:'''
#. Example : Packing a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)  #Output : ('apple', 'banana', 'cherry')


'''But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":'''
#. Example : Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(red, yellow, green) = fruits
print(red)     #Output : apple
print(yellow)  #Output : banana
print(green)   #Output : cherry
'''
Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk 
to collect the remaining values as a list.
'''


#Q. Using Asterisk*
'''If the number of variables is less than the number of values, you can add an * to the variable name and the 
values will be assigned to the variable as a list.'''
#. Example : Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)  #Output : apple
print(yellow) #Output : banana
print(red)    #Output : ['cherry', 'strawberry', 'raspberry']


'''
If the asterisk is added to another variable name than the last, Python will assign values to the variable 
until the number of values left matches the number of variables left.
'''
#. Example : Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)   #Output : apple
print(tropic)  #Output : cherry
print(red)     #Output : cherry





######################################***Python - Loop Tuples######################################
#Q. Loop Through a Tuple
'''You can loop through the tuple items by using a for loop.'''
#. Example : Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for i in thislist:
    print(i)



#Q. Loop Through the Index Numbers
'''You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.'''
#. Example : Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])



#Q. Using a while loop.
'''
You can loop through the tuple items by using a while loop.
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the 
tuple items by referring to their indexes.
Remember to increase the index by 1 after each iteration.
'''
#. Example : Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1






############################***Tuple Method***############################
#Q. count():
'''Returns the number of times a specified value occurs in a tuple'''
#. Example : Count the number of times a 'cherry' 
thistuple = ("apple", "cherry", "banana", "cherry")
print(thistuple.count("cherry"))  #Output : 2



#Q. index():
'''Searches the tuple for a specified value and returns the position of where it was found.'''
#. Example : Find the index of 'banana'.
thistuple = ("apple", "banana", "cherry")
print(thistuple.index("banana"))  #Output : 1



#Q. WAP to count the number of students with the 'A' grade in the following tuple.
student = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
print(student.count('A'))  #Output : 3


#Q. Store the above value in list and sort them from A to D.
student = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
lis1 = list(student)
lis1.sort()
student = tuple(lis1)
print(student)
