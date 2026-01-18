def log_kwargs(func):
    def wrapper(*args, **kwargs):
        print(f"Called with kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_kwargs
def my_function(a, b, **kwargs):
    return a + b

my_function(5, 10, debug=True, verbose=False)
# Вывод:
# Called with kwargs: {'debug': True, 'verbose': False}