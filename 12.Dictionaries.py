#Q. What is Dictionaries?
'''
In Python, a dictionary is a built-in data structure that stores data as key-value pairs.
It is an unordered, mutable(Changable), and indexed collection and do not allow duplicates keys.
Each key in a dictionary is unique and maps to a value.
Dictionaries are written with curly brackets, and have keys and values:
'''
#. Example : Create and print a dictionary:
student = {
    'Name' : 'John',
    'Age' : 25,
    'Branch' : 'Computer Science'
}
print(student)  #Output : {'Name': 'John', 'Age': 25, 'Branch': 'Computer Science'}



#Q. The dict() Constructor.
'''It is also possible to use the dict() constructor to make a dictionary.'''
#. Example : Using the dict() method to make a dictionary:
thisdict = dict(name = 'John', age = 25, country = 'India')
print(thisdict)  #Output : {'name': 'John', 'age': 25, 'country': 'India'}



#. Example : Store list value in dictionary and get the value.
info = {
    'Name' : 'Devid',
    'Subject' : ['C', 'C++', 'Java', 'Python', 'Swift'],
    'Dept' : 'Data Analyst'
}
print(info['Subject'])  #Output : ['C', 'C++', 'Java', 'Python', 'Swift']



'''Duplicates Not Allowed Dictionaries cannot have two items with the same key. 
Duplicate values will overwrite existing values:'''
#. Example : 
info = {
    'Name' : 'Devid',
    'Subject' : ['C', 'C++', 'Java', 'Python'],
    'Dept' : 'Data Analyst',
    'Dept' : 'Software Developer'
}
print(info) #Output :{'Name': 'Devid', 'Subject': ['C', 'C++', 'Java', 'Python'], 'Dept': 'Software Developer'}






#########################################***Dictionary Length***#####################################
'''To determine how many items a dictionary has, use the len() function.'''
#. Example : Print the number of items in the dictionary:
info = {
    'Name' : 'Devid',
    'Subject' : ['C', 'C++', 'Java', 'Python'],
    'Dept' : 'Data Analyst',
}
print(len(info))  #Output : 3






################################***Python - Access Dictionary Items***################################
#Q. Accessing Items.
'''You can access the items of a dictionary by referring to its key name, inside square brackets:'''
#. Example : Get the values of the 'Model' key : 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2025
}
print(car['Model'])  #Output : Range Rover


'''There is also a method called get() that will give you the same result:'''
#. Example : Get the values of the 'Model' key : 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2025
}
print(car.get('Model'))  #Output : Range Rover



#Q. Get Keys
'''The keys() method will return a list of all the keys in the dictionary.'''
#. Example : Get a list of the key :
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2025
}
print(car.keys())  #Output : dict_keys(['Brand', 'Model', 'Year'])



#Q. Get values
'''The values() method will return a list of all the values in the dictionary.'''
#. Example : Get the list of the values.
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2025
}
print(car.values()) #Output : dict_values(['JLR', 'Range Rover', 2025])



#Q. Get items
'''The items() method will return each item in a dictionary, as tuples in a list.'''
#. Example : Get the list of the key : value pair
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2025
}
print(car.items()) #Output : dict_items([('Brand', 'JLR'), ('Model', 'Range Rover'), ('Year', 2025)])



#Q. Check if Key Exists
'''To determine if a specified key is present in a dictionary use the 'in' keyword:'''
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2025
}
if 'Model' in car:
    print('Model is present.')
else:
    print('Model not found') #Output : Model is present.






###########################***Python - Change Dictionary Items***#############################
#Q. Change values
'''You can change the value of a specific item by referring to its key name:'''
#. Example : Change the 'year' to 2024.
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2025
}
car['Year'] = 2024
print(car) #Output : {'Brand': 'JLR', 'Model': 'Range Rover', 'Year': 2024}



#. Update Dictionary
'''The update() method will update the dictionary with the items from the given argument.
The argument must be a dictionary, or an iterable object with key:value pairs.'''
#. Example : Update the "year" of the car by using the update() method:
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
car.update({'Year' : 2025})
print(car)  #Output : {'Brand': 'JLR', 'Model': 'Range Rover', 'Year': 2025}






####################################***Python - Add Dictionary Items***################################
#Q. Adding items
'''Adding an item to the dictionary is done by using a new index key and assigning a value to it.'''
#. Example : Add a color item to the dictionary 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
car['Color'] = 'Red'
print(car) #Output : {'Brand': 'JLR', 'Model': 'Range Rover', 'Year': 2024, 'Color': 'Red'}



#Q. Update Dictionary
'''The update() method will update the dictionary with the items from a given argument. 
If the item does not exist, the item will be added.
The argument must be a dictionary, or an iterable object with key:value pairs.'''
#. Example : Add a color item to the dictionary by using the update() method:
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
car.update({'Color' : 'Red'})
print(car)  #Output : {'Brand': 'JLR', 'Model': 'Range Rover', 'Year': 2024, 'Color': 'Red'}






############################***Python - Remove Dictionary Items***##############################
#Q. Removing Items : There are several methods to remove items from a dictionary.
#1. pop() : -
'''The pop() method removes the item with the specified key name.'''
#. Example : Remove the 'Model' from car dictionary.
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
car.pop('Model')
print(car)  #Output : {'Brand': 'JLR', 'Year': 2024}


#2. popitem() : -
'''The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed 
instead).'''
#. Example : Remove the last item from car dictionary.
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
car.popitem()
print(car)  #Output : {'Brand': 'JLR', 'Model': 'Range Rover'}


#3. clear() : -
'''The clear() method empties the dictionary.'''
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
car.clear()
print(car)  #Output : {}


#4. del : -
'''The del keyword removes the item with the specified key name.'''
#. Example : Remove the 'Brand' from car 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
del car['Brand']
print(car)  #Output : {'Model': 'Range Rover', 'Year': 2024}

'''The del keyword can also delete the dictionary completely:'''
#. Example : Delete car dictionary
# car = {
#     'Brand' : 'JLR',
#     'Model' : 'Range Rover',
#     'Year' : 2024
# }
# del car
# print(car)






###############################***Python - Loop Dictionaries***#############################
#Q. Loop Through a Dictionary
'''You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to 
return the values as well.'''
#. Example : Print all key names in the dictionary, one by one:
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
for i in car:
    print(i)  #Output : Brand Model Year


'''You can use the keys() method to return the keys of a dictionary:'''
#. Example : 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
for i in car.keys():
    print(i)


#. Example : Print all values in the dictionary, one by one:
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
for i in car:
    print(car[i])  #Output : JLR Range Rover 2024


'''You can also use the values() method to return values of a dictionary:'''
#. Example : 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
for i in car.values():
    print(i)


'''Loop through both keys and values, by using the items() method:'''
#. Example : 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
for i in car.items():
    print(i)
'''
Output : 
('Brand', 'JLR')
('Model', 'Range Rover')
('Year', 2024)
'''





##########################***Python - Copy Dictionaries***##########################
#Q. Copy a Dictionary
'''You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to 
dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().'''
#. Example : Make a copy of a dictionary with the copy() method:
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
mydict = dict.copy(car)
print(mydict) #Output : {'Brand': 'JLR', 'Model': 'Range Rover', 'Year': 2024}


'''Another way to make a copy is to use the built-in function dict().'''
#.Example : 
car = {
    'Brand' : 'JLR',
    'Model' : 'Range Rover',
    'Year' : 2024
}
mydict = dict(car)
print(mydict)  #Output : {'Brand': 'JLR', 'Model': 'Range Rover', 'Year': 2024}






################################***Python - Nested Dictionaries***###############################
#Q. Nested Dictionaries
'''A dictionary can contain dictionaries, this is called nested dictionaries.'''
#. Example : Create a dictionary that contain three dictionaries:
student = {
    'Subject' : {
        'Subject_Name' : 'CS',
        'Sobject_Code' : 256
    },
    'Branch' : {
        'Dept' : 'Analyst',
        'Id' : 9
    },
    'Address' : {
        'City' : 'Patna',
        'Pin Code' : '804453'
    }
}
print(student)
'''Output : {'Subject': {'Subject_Name': 'CS', 'Sobject_Code': 256}, 'Branch': {'Dept': 'Analyst', 'Id': 9}, 
'Address': {'City': 'Patna', 'Pin Code': '804453'''

#. Or, if you want to add three dictionaries into a new dictionary:'''
Subject = {
        'Subject_Name' : 'CS',
        'Sobject_Code' : 256
}
Branch = {
        'Dept' : 'Analyst',
        'Id' : 9
}
Address = {
        'City' : 'Patna',
        'Pin Code' : '804453'
}
mydict = {
    'Subject' : Subject,
    'Branch'  : Branch,
    'Address' : Address
}
print(mydict)



#Q. Access Items in Nested Dictionaries
'''To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer 
dictionary:'''
#. Example : Print the 'City' of Address 2:
student = {
    'Subject' : {
        'Subject_Name' : 'CS',
        'Sobject_Code' : 256
    },
    'Branch' : {
        'Dept' : 'Analyst',
        'Id' : 9
    },
    'Address' : {
        'City' : 'Patna',
        'Pin Code' : '804453'
    }
}
print(student['Address']['City'])  #Output : Patna






#. Practice Question : -
'''Q1. Store following word meaning in a python dictionary.'''
mydict = {
    'table' : ["a peace of furniture", "list of fact & figure"],
    'cat' : "a small animal"
}
print(mydict)
#Output : {'table': ['a peace of furniture', 'list of fact & figure'], 'cat': 'a small animal'}


'''Q2. WAP to enter marks of 3 subject from the user and store them in a dictionary. Start with an empty
dictionary and add one by one. Use subject as key and marks as values.'''
marks = {}
Python = int(input("Enter your Python's marks : "))
SQl = int(input("Enter your SQL's marks : "))
Java = int(input("Enter your Java's marks : "))
marks.update({"Python": Python, "SQL": SQl, "Java": Java})
print(marks)
#Output : {'Python': 98, 'SQL': 70, 'Java': 30}


'''OR'''

Subject = {
    "Python" : Python,
    "SQL" : SQl,
    "Java" : Java
}
print(Subject)
#Output : {'Python': 98, 'SQL': 70, 'Java': 40}

