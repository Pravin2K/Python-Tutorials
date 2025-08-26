#Q. What is set?
'''
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed(immutable).
Set items are unchangeable, but you can remove items and add new items and do not allow duplicate values..
Sets are written with curly brackets.
'''
#. Example : Create a set.
thisset = {1, 'John', 2.0}
print(thisset)  #Output : {1, 2.0, 'John'}
'''Note: Sets are unordered, so you cannot be sure in which order the items will appear.'''

'''It is also possible to use the set() constructor to make a set.'''
thisset = set((1, 'John', 2.0))
print(thisset)  #Output : {1, 2.0, 'John'}



#Q. Get the Length of a Set
'''To determine how many items a set has, use the len() function.'''
#. Example : Get the number of items in a set:
thisset = {1, 'John', 2.0}
print(len(thisset))  #Output : 3



#Q. Duplicates Not Allowed
'''Sets cannot have two items with the same value.'''
#. Example : Duplicate values will be ignored:
thisset = {1, 'John', 2.0, 'John'}
print(thisset)  #Output : {1, 2.0, 'John'}



#Q. type()
'''From Python's perspective, sets are defined as objects with the data type 'set':'''
#. Example :
thisset = {1, 'John', 2.0,}
print(type(thisset))  #Output : <class 'set'>






#################################***Python - Access Set Items***##################################
#Q. Access Items
'''You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, 
by using the in keyword.'''
#. Example : Get Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)



#. Example : Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print('banana' in thisset)  #Output : True


#. Example : Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print('banana' not in thisset)  #Output : False






#################################***Python - Add Set Items***###############################
#Q. Add Items
'''
Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method.
'''
#. Example : Add an item to a set, using the add() method:
thisset = {1, 'John', 2.0}
thisset.add('Moraya')
print(thisset)  #OUtput : {1, 2.0, 'John', 'Moraya'}



#Q. Add Sets
'''To add items from another set into the current set, use the update() method.'''
#. Example : Add elements from tropical into thisset :
thisset = {1, 'John', 2.0}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #OUtput : {1, 2.0, 'pineapple', 'mango', 'John', 'papaya'}



#Add Any Iterable
'''The object in the update() method does not have to be a set, it can be any iterable object 
(tuples, lists, dictionaries etc.).'''
#. Example : Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #OUtput : {'orange', 'kiwi', 'apple', 'banana', 'cherry'}






###############################***Python - Remove Set Items***#################################
#Q. Remove Item
'''To remove an item in a set, use the remove(), or the discard() method.'''
#. Example : Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove('banana')
print(thisset) #Output : {'apple', 'cherry'}
'''Note: If the item to remove does not exist, remove() will raise an error.'''



#Q. discard()
'''If the item to remove does not exist, discard() will NOT raise an error.'''
#. Example : Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard('banana')
print(thisset) #Output : {'apple', 'cherry'}


#. Example : Remove 'apple' by using discard() method :
thisset = {"papaya", "banana", "cherry"}
thisset.discard('apple')
print(thisset)  #Output : {'cherry', 'papaya', 'banana'}
'''Note: If the item to remove does not exist, discard() will NOT raise an error.'''



#Q. pop() : -
'''pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item 
that gets removed.'''
#. Example : Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)  #Output : {'apple', 'cherry'}



#Q. clear() : -
'''The clear() method empties the set.'''
#. Example : clear the set.
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  #Output : set()



#Q. del : -
'''The del keyword will delete the set completely:'''
#. Example : delete the set :
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)  #Output : NameError: name 'thisset' is not defined






###############################***Python - Loop Sets***##################################
#Q. Loop Items
'''You can loop through the set items by using a for loop:'''
#. Example : Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)







#########################################***Python - Join Sets***######################################
#Q. Join Sets
'''There are several ways to join two or more sets in Python.'''

#Q. union() : -
'''The union() method returns a new set with all items from both sets.'''
#. Example : Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  #Output : {1, 'c', 2, 'a', 'b', 3}


'''You can use the | operator instead of the union() method, and you will get the same result.'''
#. Example : Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)  #Output : {1, 'b', 2, 3, 'a', 'c'}



#Q. Join Multiple Sets : -
'''All the joining methods and operators can be used to join multiple sets.
When using a method, just add more sets in the parentheses, separated by commas:'''
#. Example : Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 = set1.union(set2, set3, set4)
print(set5) #Output : {1, 2, 3, 'apple', 'c', 'cherry', 'John', 'Elena', 'a', 'bananas', 'b'}

#. Example : Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 = set1 | set2 | set3 | set4
print(set5)  #Output : {1, 2, 3, 'apple', 'c', 'cherry', 'John', 'Elena', 'a', 'bananas', 'b'}


#Q. Join a Set and a Tuple
'''The union() method allows you to join a set with other data types, like lists or tuples.
The result will be a set.'''
#. Example : Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z) #Output : {1, 2, 3, 'c', 'a', 'b'}
'''Note: The  | operator only allows you to join sets with sets, and not with other data types like you can 
with the  union() method.'''



#Q. update() : -
'''The update() method inserts all items from one set into another.
The update() changes the original set, and does not return a new set.'''
#. Example : The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)  #Output : {1, 2, 3, 'b', 'c', 'a'}
'''Note: Both union() and update() will exclude any duplicate items.'''



#Q. Intersection : -
'''The intersection() method will return a new set, that only contains the items that are present 
in both sets.'''
#. Example : Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)  #Output : {'apple'}

'''You can use the & operator instead of the intersection() method, and you will get the same result.'''
#. Example : Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)  #Output : {'apple'}
'''Note: The & operator only allows you to join sets with sets, and not with other data types like you can 
with the intersection() method.'''



#Q. intersection_update() : -
'''The intersection_update() method will also keep ONLY the duplicates, but it will change the original set 
instead of returning a new set.'''
#. Example : Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  #Output : {'apple'}



#Q. difference() : -
'''The difference() method will return a new set that will contain only the items from the first set that 
are not present in the other set.'''
#. Example : Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)  #Output : {'banana', 'cherry'}

'''You can use the - operator instead of the difference() method, and you will get the same result.'''
#. Example : Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)  #Output : {'cherry', 'banana'}
'''Note: The - operator only allows you to join sets with sets, and not with other data types like you can 
with the difference() method.'''



#Q. difference_update() : -
'''The difference_update() method will also keep the items from the first set that are not in the other set, 
but it will change the original set instead of returning a new set.'''
#. Example : Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)  #Output : {'banana', 'cherry'}



#Q. symmetric_difference() : -
'''The symmetric_difference() method will keep only the elements that are NOT present in both sets.'''
#. Example : Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)  #Output : {'banana', 'cherry', 'google', 'microsoft'}

'''You can use the ^ operator instead of the symmetric_difference() method, and get the same result.'''
#. Example : Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)  #Output : {'banana', 'cherry', 'google', 'microsoft'}



#Q. symmetric_difference_update() : -
'''The symmetric_difference_update() method will also keep all but the duplicates, but it will change the 
original set instead of returning a new set.'''
#. Example : Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  #Output : {'microsoft', 'banana', 'google', 'cherry'}




#Q. Practice Question : -
'''Q1. Your are given a list of subject for students.assume 1 classroom is required for one subject.
Howmany classroom are needed by all students'''
subject = {"python", "java", "C++", "python", "javascripts", "java", "python", "java", "C++", "C"}
print(len(subject)) #Output : 5