# %%

# Author: Corey Schafer

# In this Python tutorial, we will be learning about decorators. 
# Decorators are a way to dynamically alter the functionality of your functions. 
# So for example, if you wanted to log information when a function is run,
# you could use a decorator to add this functionality without modifying the source code 
# of your original function. 
# So let's take a look at how these decorators work and a few ways in which we can use them. 
# Let's get started.

# link: https://www.youtube.com/watch?v=FsAPt_9Bf3U


def outer_function():
    message = "Hi"

    def inner_function():
        print(message)
    return inner_function()

outer_function()

# "Hi"

# %%

def outer_function_0():
    message = "Hi"

    def inner_function_0():
        print(message)
    return inner_function_0 # <- removing "()"

my_func_0 = outer_function_0()
my_func_0()

# "Hi"

# %%

def outer_function_1(msg): # <- add message variable
    def inner_function_1():
        print(msg)
    return inner_function_1 

hi_func_1 = outer_function_1("Hi")
bye_func_1 = outer_function_1("Bye")

hi_func_1()
bye_func_1()

# "Hi"
# "Bye"

# %%

def decorator_function_0(msg): # <- change the names
    def wrapper_function_0(): # <- change the names
        print(msg)
    return wrapper_function_0 

hi_func_2 = decorator_function_0("Hi")
bye_func_2 = decorator_function_0("Bye")

hi_func_2()
bye_func_2()

# "Hi"
# "Bye"

# %%

def decorator_function_1(original_function): # <- call function instead variable
    def wrapper_function_1(): 
        return original_function() # <- return called function
    return wrapper_function_1 

def display():
    print("display function executed")

decorated_display = decorator_function_1(display)
decorated_display()

# "display function executed"

# %%

def decorator_function_2(original_function):
    def wrapper_function_2(): 
        # v v v adding some functionality on wrapper
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function_2 

def display():
    print("display function executed")

decorated_display = decorator_function_2(display)
decorated_display()

# wrapper executed this before display
# display function executed

# %%

def decorator_function_3(original_function):
    def wrapper_function_3():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function_3

# v v v adding decorator
@decorator_function_3 # is the same as display = decorator_function_3(display)
def display():
    print("display function executed")

display()

# %%

def decorator_function_4(original_function):
    def wrapper_function_4(*args, **kwargs): # <- take any kind arguments passing by wrapper function
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function_4

@decorator_function_4
def display_info_0(name, age):
    print("display with arguments {} {}".format(name, age))

display_info_0("Mario",210)

# wrapper executed this before display_info_0
# display with arguments Mario 210

# %%

# Class Decorators (doing same thing as before)

class decorator_class_0(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class_0
def display_info_0(name, age):
    print("display with arguments {} {}".format(name, age))

display_info_0("Mario",210)

# call method executed this before display_info_0
# display with arguments Mario 210

# %%

# helps in the case of the usage of two decorators

from functools import wraps

def decorator_function_5(original_function):

    @wraps(original_function) # <- here to keep the original function
    def wrapper_function_5(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function_5

@decorator_function_5
def display_info_0(name, age):
    print("display with arguments {} {}".format(name, age))

display_info_0("Mario",210)

# wrapper executed this before display_info_0
# display with arguments Mario 210

# %%
