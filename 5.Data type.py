#Q. What is Data Type?
'''
In Python, a data type defines what kind of value a variable holds — such as a number, text, list, etc. 
Python uses data types to know how to store and operate on data.
'''

#🔹 Basic Data Types in Python:
'''
1. int
number = 65

2. float
num = 8.1

3. str
name = 'John'

4. bool
True, False

5.None Type
None
'''

#✅ Example:

age = 25              # int
price = 19.99         # float
name = "Alice"        # str
is_online = True      # bool


#🔹 Collection Data Types:
#1.list : Ordered, changeable collection
colors = ['Red', 'Green', 'White', 'Black']
print(colors)
# Outputs : ['Red', 'Green', 'White', 'Black']

#2.Tuple : Ordered, unchangeable collection
fruits = ['Apple', "Papaya"]
print(fruits)
# Outputs : ['Apple', "Papaya"]

#3. Dict : Key-value pairs (dictionary)
dic = {'Name' : "Alice"}
print(dic)
# Outputs : {'Name': 'Alice'}

#4. Set : Unordered, no duplicates
setNum = {1, 2, 3, 1}
print(setNum)
# Outputs : {1, 2, 3}



#🧪 Check Data Type with type():
id = [1,2,3,4,5]
print(type(id))
# Output : <class 'list'>