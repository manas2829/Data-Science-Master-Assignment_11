#!/usr/bin/env python
# coding: utf-8

# # Assignment_12-02-2023

# ## 1. What is the exception in python ? Write the different between Exception or Syntax Error.
# 
# ### Ans:-
#       In Python, an exception is an error that occurs during the execution of a program, and can be handled by the program.
#          
#       Syntax errors, on the other hand, occur when the Python interpreter is unable to understand the code due to incorrect
#       syntax, such as a missing bracket or semicolon.
#          
#       The main difference between exceptions and syntax errors is that syntax errors occur before the program is executed,
#       whereas exceptions occur during the execution of the program. Syntax errors must be fixed before the program can be
#       run, while exceptions can be handled by the program to prevent it from crashing.
#       

# ## 2. What happens when an exception is not handled ? Explain with Example.
# 
# ### Ans:-
#            When an exception is not handled in Python, it will result in an error message being displayed, 
#            and the program will terminate or crash.
#        

# In[1]:


## Here is an Example:-
try:
    a=10/0
except ValueError as r:
    print("This is a value error",r)


# ### 
#      In this example, the program attempts to divide 10 by 0, which will raise a ZeroDivisionError. However, there is no 
#      except block to handle this specific error, so the program will crash with an error message that includes information
#      about the error
#      
#      If we add an except block to handle the ZeroDivisionError, the program can continue running without crashing.
# 

# In[2]:


## Here is an Example:- as proper exception error msg
try:
    a=10/0
except ZeroDivisionError as r:
    print("This is a value error",r)


# ### 
#         In this above example, the except block catches the ZeroDivisionError and prints a message, allowing the program to 
#         continue running without crashing.

# ## 3. Which python statements are used to catch and handle exception?Explain with Example.
# 
# ### Ans:-
#      In Python, the try and except statements are used to catch and handle exceptions. The try block contains the code 
#      that might raise an exception, and the except block handles the exception if it occurs.
#      
#      Here is an example in mention below of how to use try and except statements to catch and handle an exception:

# In[3]:


## Example:-
try:
    a=10/0
except ZeroDivisionError as r:
    print("This is a value error",r)


# ### 
#     In this example, the try block contains the code that might raise an exception (in this case, dividing 1 by 0 will 
#     raise a ZeroDivisionError). The except block catches the ZeroDivisionError and prints a message, allowing the program 
#     to continue running without crashing.
#     
#     We can also use multiple except blocks to catch different types of exceptions: shown example in below.

# In[4]:


## Example of multiple except method:-
try:
    x=int("Manas")
    a=10/0
    
except ValueError:
    print("This is a value error")
    
except ZeroDivisionError:
    print("This is a ZeroDivisin error")


# ### 
#     In this example, the try block contains two lines of code that might raise different exceptions (converting a string to
#     an integer will raise a ValueError, while dividing by zero will raise a ZeroDivisionError). The first except block 
#     catches the ValueError and prints a message, if first except sucessfully then while the second except block not catches
#     the ZeroDivisionError and not prints a different message.

# ## 4. Explain with an Example
# 
# ### a. try and else
# ### b. finally
# ### c. raise
# 
# ### Ans:-
# 

# ### a. try and else
#         The try and else statements in Python are used to define a block of code that is executed if no exceptions are 
#         raised in the try block.

# In[5]:


try:
    x=5/2
except ZeroDivisionError:
    print("You can't divide by Zero")
else:
    print("The result is",x)


# ### 
#        In this example, the try block attempts to divide 5 by 2, which will not raise any exceptions. The else block is 
#        executed, and prints the result of the division.

# ### b. Finally
#               The finally statement in Python is used to define a block of code that is always executed, regardless of \
#               whether an exception was raised or not.

# In[6]:


## Finally exampel:-
try:
    with open("Manas.txt",'r') as m:
        m.read()
finally:
    m.close()


# ### 
#       In this example, the try block attempts to open a file, and then executes some code that might raise an exception. 
#       The finally block is always executed, and closes the file, regardless of whether an exception was raised or not.

# ### c. Raise
#              The raise statement in Python is used to raise an exception.

# In[7]:


## Raise exampel:-

try:
    x=int(input("Enter a Number: "))
    if x<0:
        raise ValueError("The number can't be Negative ")
except ValueError as f:
    print(f)


# ### 
#         In this example, the try block attempts to convert user input to an integer, and then checks whether the integer is
#         negative. If the integer is negative, the raise statement is used to raise a ValueError with a custom error message.
#         The except block catches the ValueError and prints the error message.

# ## 5. What is custom Exceptions in python? Why do you need custom exceptions? Explain with Example.
# 
# ### Ans:-
#         In Python, custom exceptions are user-defined exceptions that can be used to handle specific errors in a program. 
#         Custom exceptions are created by defining a new class that inherits from the built-in Exception class or one of its
#         subclasses.
#         
#         Custom exceptions are useful when the built-in exceptions are not specific enough to handle a particular error or 
#         when you want to group a set of related errors under a single exception.
# 

# In[8]:


## Example how to create and use a custom exception in python.

class invaild_input_Error(Exception):
    pass
def process_input(Value):
    if value< 0 or value > 100:
        raise invaild_input_Error("The value must be  between 0 and 100")
try:
    value= int(input("Enter the value between 0 and 100 "))
    process_input(value)
except invaild_input_Error as e:
    print(e)


# ### 
#     In this example, we define a custom exception called InvalidInputError by creating a new class that inherits from the 
#     built-in Exception class. We then define a function called process_input that raises the InvalidInputError if the input
#     value is outside the range of 0 to 100.
# 
#     In the try block, we attempt to get user input and process it using the process_input function. If the InvalidInputError 
#     is raised, the except block catches the error and prints the error message.
#     
#     Custom exceptions can make code more readable and easier to maintain by providing clear and specific error messages for
#     specific types of errors, and by grouping related errors under a single exception.

# ## 6.Create a custom exception class. Use this class to handle an exception.
# 
# ### Ans:-
# 

# In[9]:


class customexception(Exception):
    def __init__(manas,message):
        manas.message = message
try:
    n=int(input("Enter the number greater than 10"))
    if n <= 10:
        raise customexception("Number must be greater than ten")
except customexception as c:
    print(c)


# ### 
#     In this example, we define a custom exception class MyCustomException that takes a message as input and stores it as an
#     attribute of the exception object. We then use this custom exception to raise an exception if the user enters a number 
#     less than or equal to 10. If the exception is raised, we catch it using a try-except block and print the error message.
