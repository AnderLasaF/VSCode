def my_wrapper_function(original_function):
    def wrapper(*args, **kwargs):
        print("Before calling the original function")
        result = original_function(*args, **kwargs)
        print("After calling the original function")
        return result
    return wrapper

@my_wrapper_function
def my_function(*args):
    my_sum = 0
    for value in args:
        my_sum += value
    return my_sum

#this is the same as using the decorator
#my_function_wrapped = my_wrapper_function(my_function)
#result = my_function_wrapped(3, 4)
#print("Result: ", result)

result2= my_function(3,4,5)
print("Result: ", result2)


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    return "Whee!"

#In this case print returns None because the wrapper function (wrapper) is not returning the return value of the decorated function (say_whee),
#since there is no return statement, the "return wrapper" returns None
print(say_whee())