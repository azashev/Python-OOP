# Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the result of a function with the
# given tag and return the new result.

def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper

    return decorator


# Test code:
@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

# Expected output:
# <p>Hello you!</p>


print()


# Test code:
@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

# Expected output:
# <h1>HELLO</h1>
