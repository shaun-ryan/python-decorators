from decorators import debug, do_twice

# debug(do_twice(greet()))
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


greet("Eva")