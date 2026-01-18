
def add_numbers(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add_numbers(1, 2, 3))  # 6
print(add_numbers(10, 20, 30, 40))  # 100