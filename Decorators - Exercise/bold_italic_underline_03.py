# Create three decorators: make_bold, make_italic, make_underline, which will have to wrap a text returned from a
# function in <b></b>, <i></i> and <u></u> respectively.

def make_bold(func):
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"

    return wrapper


def make_italic(func):
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"

    return wrapper


def make_underline(func):
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"

    return wrapper


# Test code:
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))

# Expected output:
# <b><i><u>Hello, Peter</u></i></b>


print()


# Test code:
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))

# Expected output:
# <b><i><u>Hello, Peter, George</u></i></b>