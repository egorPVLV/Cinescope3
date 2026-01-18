
def filter_kwargs(**kwargs):
    nums = kwargs.copy()
    for key, value in kwargs.items():
        if value <= 10:
            del nums[key]
    return nums




print(filter_kwargs(a=5, b=20, c=15, d=3))
# Вывод: {'b': 20, 'c': 15}