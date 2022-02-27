
# In this Python Object-Oriented Tutorial, we will be learning about classmethods
# and staticmethods. Class methods are methods that automatically take 
# the class as the first argument. Class methods can also be used as alternative
# constructors. Static methods do not take the instance or the class as the first argument.
# They behave just like normal functions, yet they should have some logical connection 
# to our class. We will look at some examples of both of these in order to understand 
# both in depth. Let's get started.

# link: https://www.youtube.com/watch?v=rq8cL2XMM5M
# !!! ADAPTED !!!

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

    @classmethod # <- Using class method
    def from_fixed(cls, n): # <- decorator_class_1 (current) as cls

        c = cls("#"*n) # <- calling like c = decorator_class_1
        return c  

    def __call__(self, original_function):
        def wrapper(*args, **kwargs):
            print(self.prefix, "Executed Before",original_function.__name__)
            result = original_function(*args, **kwargs)
            print(self.prefix, "Executed After",original_function.__name__, "\n")
            return result
        return wrapper

@decorator_class_1.from_fixed(5) # using from_fixed instead of __init__
def display_info(name, age):
    print("display_info with arguments {} {}".format(name, age))

display_info("John", 25)
display_info("Travis", 30)

# ##### Executed Before display_info
# display_info with arguments John 25
# ##### Executed After display_info 

# ##### Executed Before display_info
# display_info with arguments Travis 30
# ##### Executed After display_info 

# %%
