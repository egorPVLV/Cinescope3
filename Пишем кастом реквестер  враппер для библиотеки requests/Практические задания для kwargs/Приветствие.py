def greet(**kwargs):
    print(f'Hello, {kwargs["name"]}! You are {kwargs["age"]} years old. ')

greet(name="Alice", age=25)
# Вывод: Hello, Alice! You are 25 years old.