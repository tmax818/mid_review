
# write a function, hello(), that prints "Hello, World!" to the screen

def hello():
    print("Hello, World!")


# write a function that will say hello to a name provided as an argument. For example, if the function is called with hello_name('Tom'), it will print "Hello, Tom" to stdout.

def hello_name(name):
    print(f"Hello, {name}")

# write a function that will return True if the number supplied as an argument is even


def is_even(number):
    return number % 2 == 0


# write a fizzbuzz function

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
