#Q. What is Comment?
'''
In Python, a comment is a piece of text in the code that is not executed by the interpreter. 

Comments are used to:
Explain code logic for better readability.
Temporarily disable code (for debugging).
Add documentation (like docstrings).
'''

#Q. Types of Comments in Python
'''
1. Single-Line Comments (#)
Starts with # and continues till the end of the line.

Used for short explanations or disabling a line.
Example:

python
# This is a single-line comment
print("Hello")  # This prints "Hello"
Output: Hello
'''


'''
2. Multi-Line Comments (Using ''' or """)
Python does not have a dedicated syntax for multi-line comments, but triple-quoted strings (unassigned) are 
commonly used. 
Works like a comment if not assigned to a variable.

Example:
'''
This is a multi-line comment.
It spans multiple lines.
Python ignores it since it's not assigned.
'''


This is another way
to write multi-line comments.
"""
print("World")
#Output : World
