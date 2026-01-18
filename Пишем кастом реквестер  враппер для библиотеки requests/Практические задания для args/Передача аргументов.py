
def pass_arguments(*args):
    print_args(args)

def print_args(args):
    for arg in args:
        print(arg)

pass_arguments("Hello", 42, False)
# Вывод:
# Hello
# 42
# False