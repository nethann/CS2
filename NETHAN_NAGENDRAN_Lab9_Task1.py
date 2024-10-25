# Write a Python function named ‘exception_handler()’ that generates and handles the following five different types of built-in exceptions. Make sure to print a meaningful error message whenever an exception occurs.

# 	- TypeError
# 	- ValueError
# 	- IndexError
# 	- KeyError
# 	- AttributeError


def exception_handler():
    try:
        result = 'test' + 129
    except TypeError as error:
        print(f"TypeError: {error}")

    try:
        number = int('computer_science')
    except ValueError as error:
        print(f"ValueError: {error}")

    try:
        lst = [4,2,3,1,2]
        element = lst[5]
    except IndexError as error:
        print(f"IndexError: {error}")

    try:
        dct = {'Object1': 'Bmw', 'Object2' : 'Benz'}
        value = dct['Object9']
    except KeyError as error:
        print(f"KeyError: {error}")

    try:
        obj = 10
        obj.append(23)
    except AttributeError as error:
        print(f"AttributeError: {error}")

exception_handler()
