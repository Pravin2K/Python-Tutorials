#Q. What is List?
'''
In Python, a list is a built-in data type used to store a different data types of collection of items in a 
single variable(like numbers, strings, or even other lists). Lists are ordered, changeable (mutable), and 
allow duplicate values.
'''
#. Example : Create a simple list.
l1 = ['fruits', 1, True, 2.0]
print(l1) #Output: ['fruits', 1, True, 2.0]

fruits = ['Apple', 'Banana', 'Cherry']
print(fruits) #output : ['Apple', 'Banana', 'Cherry']




#############################***Access List Items***##########################
#Q. Python - Access List Items.
'''List items are indexed and you can access them by referring to the index number.'''
#. Example : Print the second item of the list:
l1 = ['fruits', 1, True, 2.0]
print(l1[1])     #Output : 1
#Note: The first item has index 0.


#Q. Negative Indexing : 
'''Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.'''
#. Example : Print the last item of the list:
l1 = ['fruits', 1, True, 2.0]
print(l1[-1])  #Output : 2.0


#Q. Range of Indexes :
'''You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.'''
#Example : Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2 : 5]) #Output : ['cherry', 'orange', 'kiwi']

'''
Note: The search will start at index 2 (included) and end at index 5 (not included).
Remember that the first item has index 0.
By leaving out the start value, the range will start at the first item:
'''

#. Example : This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[: 4])  #Output : ['apple', 'banana', 'cherry', 'orange']

#. Example : This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2 :]) #Output : ['cherry', 'orange', 'kiwi', 'melon', 'mango']


#Q. Range of Negative Indexes.
'''Specify negative indexes if you want to start the search from the end of the list.'''
#. Example : This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4 : -1]) #Output : ['orange', 'kiwi', 'melon']


#Q. Check if Item Exists
'''To determine if a specified item is present in a list use the in keyword.'''
#. Example : Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if 'apple' in thislist:
    print('apple is exist in this list.')
else:
    print('Not Found.')  #Output : apple is exist in this list.





####################***Python - Change List Items***#####################
#Q. Change Item Value.
'''To change the value of a specific item, refer to the index number.'''
#. Example : Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = 'Papaya' 
print(thislist) #Output : ['apple', 'Papaya', 'cherry']



#Q. Change a Range of Item Values
'''To change the value of items within a specific range, define a list with the new values, and refer to the 
range of index numbers where you want to insert the new values.'''
#Example : Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1 : 3] = ['blackcurrant', 'watermelon']
print(thislist) #Output : ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


'''If you insert more items than you replace, the new items will be inserted where you specified, and the 
remaining items will move accordingly.'''
#. Example : Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1 : 2] = ['blackcurrant', 'watermelon']
print(thislist) #Output : ['apple', 'blackcurrant', 'watermelon', 'cherry']



'''If you insert less items than you replace, the new items will be inserted where you specified, and the 
remaining items will move accordingly:'''
#. Example : Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1 : 3] = ['Watermelon']
print(thislist)  #Output : ['apple', 'Watermelon']





##########################***Python - Add List Items***##########################
#Q. Append Items
'''To add an item to the end of the list, use the append() method.'''
#. Example : Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append('papaya')
print(thislist) #Output : ['apple', 'banana', 'cherry', 'papaya']


#Q. Insert Items
'''To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index.'''
#. Example : Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, 'blackcurrant')
print(thislist) #Output : ['apple', 'blackcurrant', 'banana', 'cherry']


#Q. Extend List :
'''To append elements from another list to the current list, use the extend() method.'''
#. Example : Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  #Output : ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


#Q. Add Any Iterable
'''The extend() method does not have to append lists, you can add any iterable object 
(tuples, sets, dictionaries etc.).'''
#. Example : Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #Output : ['apple', 'banana', 'cherry', 'kiwi', 'orange']





########################***Remove Specified Item***#######################
#Q. removes the specified item.
'''The remove() method removes the specified item.'''
#. Example : Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove('apple')
print(thislist)  #Output : ['banana', 'cherry']


'''If there are more than one item with the specified value, the remove() method removes the first occurrence'''
#. Example : Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove('banana')
print(thislist)  #Output : ['apple', 'cherry', 'banana', 'kiwi']



#Q. Remove Specified Index
'''The pop() method removes the specified index.'''
#. Example : Remove the second item:
thislist = ["apple", "banana", "cherry", "kiwi"]
thislist.pop(1)
print(thislist) #Output : ['apple', 'cherry', 'kiwi']


'''If you do not specify the index, the pop() method removes the last item.'''
#. Example : Remove the last item:
thislist = ["apple", "banana", "cherry", "kiwi"]
thislist.pop()
print(thislist)  #Output : ['apple', 'banana', 'cherry']



#Q. The del keyword also removes the specified index:
#. Example : Remove the first item:
thislist = ["apple", "banana", "cherry", "kiwi"]
del thislist[0]
print(thislist)  #Output : ['banana', 'cherry', 'kiwi']


'''The del keyword can also delete the list completely.'''
#. Example : Delete the entire list:
thislist = ["apple", "banana", "cherry", "kiwi"]
del thislist


#Q. Clear the List
'''The clear() method empties the list.
The list still remains, but it has no content.'''
#. Example : Clear the list content:
thislist = ["apple", "banana", "cherry", "kiwi"]
thislist.clear()
print(thislist) #Output : []





##############################***Python - Loop Lists***##############################
#Q. Loop Through a List.
'''You can loop through the list items by using a for loop:'''
#. Example : Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry", "kiwi"]
for i in thislist:
    print(i)


#Q. Loop Through the Index Numbers.
'''You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
'''
#. Example : Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry", "kiwi"]
for i in range(len(thislist)):
    print(thislist[i])


#Q. Using a While Loop
'''You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, then start at 0 and loop your way through the 
list items by referring to their indexes.
Remember to increase the index by 1 after each iteration.'''
#. Example : Print all items, using a while loop to go through all the index numbers.
thislist = ["apple", "banana", "cherry", "kiwi"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1




#####################***Python - Sort Lists***###########################
#Q. Sort List Alphanumerically
'''List objects have a sort() method that will sort the list alphanumerically, ascending, by default.'''
#. Example : Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  #Output : ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


#. Example : Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  #Output : [23, 50, 65, 82, 100]


#Q. Sort Descending
'''To sort descending, use the keyword argument reverse = True.'''
#. Example : Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)  #Output : ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


#Q. Reverse Order.
'''What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.'''
#. Example : Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)  #Output : ['cherry', 'Kiwi', 'Orange', 'banana']


#Q. WAP to ask the user to enter name of their 3 favourite movies & store them in a list.
user1 = input("Enter the 1st movies name : ")
user2 = input("Enter the 2nd movies name : ")
user3 = input("Enter the 3rd movies name : ")
movies = [user1, user2, user3]
print(movies)
print(type(movies))  #Output : ['Dhoom', 'Dhol', 'Golmal']



#Q. WAP to check the given list is palindrom or not.
palindrom = [1,2,3,2,1]
if palindrom[::-1] == palindrom:
    print('Palindrom')
else:
    print('not palindrome')  #Output : Palindrom