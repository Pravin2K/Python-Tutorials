#Q. What is function?
'''
A function in Python is a block of reusable code that performs a specific task.
Instead of writing the same code again and again, you put it inside a function and just “call” 
it whenever needed.
In Python a function is defined using the def keyword:
'''

#Q. Creatting a simple function.
'''In Python, you define a function with def:'''

def myFunction():
    print("HEllo from function")


#Q. Calling a Function
'''To call a function, use the function name followed by parenthesis:'''
def myFunction():
    print("Hello from function")
myFunction()  #Output: Hello from function







##########################################*****Arguments*****##########################################
#Q. What is Argument in python?
'''
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.
'''
#. Example : -
def my_Func(fname):
    print(fname)
my_Func("John")


#Q. Parameters or Arguments?
'''
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
'''


#Q. Number of Arguments.
'''
By default, a function must be called with the correct number of arguments. Meaning that if your function 
expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
If you try to call the function with 1 or 3 arguments, you will get an error:
'''
#. Example : This function expects 2 arguments, and gets 2 arguments:
def my_Func(num1, num2):
    return num1 + num2
print(my_Func(4, 3))  #Output : 7






###################################****Arbitrary Arguments, *args***###################################
'''
If you do not know how many arguments that will be passed into your function, add a * before the parameter 
name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
Arbitrary Arguments are often shortened to *args in Python documentations.
'''
#. Example : If the number of arguments is unknown, add a * before the parameter name:
def myFunc(*args):
    print(f'the youngest child is {args[2]}')
myFunc("John", "Moraya", "Devid")  #Output : the youngest child is Devid


#Q. Keyword Arguments
'''
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
'''
#. Example : 
def myFunc(c1, c2, c3):
    print(f'The youngest child is {c3}')
myFunc(c1='Max', c2='Glan', c3='Albe') #Output: The youngest child is Albe







###########################***Arbitrary Keyword Arguments, **kwargs***################################
#Q. What is Arbitrary Keyword Arguments, **kwargs?
'''
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** 
before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
'''
#. Example : If the number of keyword arguments is unknown, add a double ** before the parameter name:
def myFunc(**kid):
    print(f'His last name is {kid['lname']}')
myFunc(fname= "John", lname= 'Doe')  #Output : His last name is Doe





################################***Default Parameter Value***################################
#Q. What is default parameter value?
'''
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:
'''
#. Example : 
def myFunc(country = "Norway"):
    print(country)
myFunc()  #Output : Norway




#Q. Passing a List as an Argument.
'''
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same 
data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function:
'''
#. Example : 
def myFunc(food):
    for x in food:
        print(x)
food = ["Pizza", "Pasta", "Barger"]
myFunc(food)





###################################***Return values***#################################
#Q. What is return value?
'''
The return statement is used inside a function to send a value back to the caller.
Without return, the function will output None (by default).
A function can return any data type (numbers, strings, lists, dicts, even other functions).
'''
#. Example 1: Simple Return
def add(a, b):
    return a + b
result = add(5, 19)
print(result)


    