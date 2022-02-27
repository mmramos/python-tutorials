

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
# %%
