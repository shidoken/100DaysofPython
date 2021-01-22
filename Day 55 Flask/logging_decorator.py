# Create the logging_decorator() function 👇
def logger(function):
    def wrapper(*args):
        function()
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
    return wrapper


# Use the decorator 👇
@logger
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)