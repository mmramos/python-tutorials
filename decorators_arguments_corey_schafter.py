# %%

# Author: Corey Schafer

# In this Python tutorial, we will be learning how to create decorators with parameters 
# that accept arguments. This was a highly requested video in response to my
# original decorator tutorial video. Accepting arguments allows us to add even more
# functionality to our decorators. You will see this throughout many frameworks and libraries, 
# so it's a good skill to know. Let's get started

# link: https://www.youtube.com/watch?v=KlBPCzcQNU8

def decorator_function_0(original_function):
    def wrapper_function_0(*args, **kwargs):
        print("Executed Before",original_function.__name__)
        result = original_function(*args, **kwargs)
        print("Executed After",original_function.__name__, "\n")
        return result
    return wrapper_function_0

@decorator_function_0
def display_info(name, age):
    print("display_info with arguments {} {}".format(name, age))

display_info("John", 25)
display_info("Travis", 30)

# Executed Before display_info
# display_info with arguments John 25
# Executed After display_info 

# Executed Before display_info
# display_info with arguments Travis 30
# Executed After display_info 

# %%

def prefix_decorator_1(prefix): # <- Another function created before the execution
    def decorator_function_1(original_function):
        def wrapper_function_1(*args, **kwargs):
            print(prefix, "Executed Before",original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, "Executed After",original_function.__name__, "\n")
            return result
        return wrapper_function_1
    return decorator_function_1

@prefix_decorator_1("TESTING:")
def display_info(name, age):
    print("display_info with arguments {} {}".format(name, age))

display_info("John", 25)
display_info("Travis", 30)

# TESTING: Executed Before display_info
# display_info with arguments John 25
# TESTING: Executed After display_info 

# TESTING: Executed Before display_info
# display_info with arguments Travis 30
# TESTING: Executed After display_info 

# %%

class decorator_class_0(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, original_function):
        def wrapper(*args, **kwargs):
            print(self.prefix, "Executed Before",original_function.__name__)
            result = original_function(*args, **kwargs)
            print(self.prefix, "Executed After",original_function.__name__, "\n")
            return result
        return wrapper

@decorator_class_0("CLASS TEST:")
def display_info(name, age):
    print("display_info with arguments {} {}".format(name, age))

display_info("John", 25)
display_info("Travis", 30)

# CLASS TEST: Executed Before display_info
# display_info with arguments John 25
# CLASS TEST: Executed After display_info 

# CLASS TEST: Executed Before display_info
# display_info with arguments Travis 30
# CLASS TEST: Executed After display_info 

# %%

class decorator_class_1(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, original_function):
        def wrapper(*args, **kwargs):
            self.wrapper_obj(original_function, *args, **kwargs)
        return wrapper

    def wrapper_obj(self, function, *args, **kwargs):
        print(self.prefix, "Executed Before",function.__name__)
        result = function(*args, **kwargs)
        print(self.prefix, "Executed After",function.__name__, "\n")
        return result

@decorator_class_1("ANOTHER CLASS TEST:")
def display_info(name, age):
    print("display_info with arguments {} {}".format(name, age))

display_info("John", 25)
display_info("Travis", 30)

# ANOTHER CLASS TEST: Executed Before display_info
# display_info with arguments John 25
# ANOTHER CLASS TEST: Executed After display_info 

# ANOTHER CLASS TEST: Executed Before display_info
# display_info with arguments Travis 30
# ANOTHER CLASS TEST: Executed After display_info 

# %%