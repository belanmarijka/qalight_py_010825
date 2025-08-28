# def, lambda
def lazy():
    pass


def print_lyrics():
    """Друкує пісню"""
    print("Ой у лузі червона калина похилилася")
    print("Чогось наша славна Україна зажурилася")

def one():
    return 1+1

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    return f"My {animal_type}'s name is {pet_name.title()}."

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def greet(name: str, greeting: str = "Hello") -> str:
    """
    Функція виводить привітання для заданого імені.

    :param name: Ім'я для привітання
    :param greeting: Привітання (за замовчуванням "Привіт")
    """
    return f"{greeting.title()}, {name.title()}!"

out = describe_pet("cat", "marsik")
print(out)
out2 = describe_pet("dog", "bingo")
print(out2)

c = add(1, 4)
print("add(1, 4) ==", c)

d = minus(1, 4)
e = minus(4, 1)
print("1-4, 4-1", d, e)
print(greet("alex", 'hi'))
print(greet("viktoria",))
print(greet("олено","добрий вечір"))
print(greet("hi"))

print(greet(greeting="hello", name="alice"))

def describe_person(name="John Dou", age=18, country="Unknown"):
    print(f"{name} is {age} years old and is from {country}.")

describe_person("Alice", 30)
describe_person("Bob", 25, country="USA")
describe_person(age=30, country="Japan", name="Helga")

def describe_person_ext(name, age=18, country="Unknown", gender="X", last_visit="today"):
    print(f"{name} is {age} years old and is from {country}. You are {gender}, last time we see you {last_visit}")

describe_person_ext("Alice",
                    gender="w",
                    last_visit="yesterday")

describe_person_ext("Alex",
                    age=25,
                    country="Ukraine",
                    gender="m",
                    )

def print_args(*args):
    for arg in args:
       print(arg)
    
print_args()
print_args(1)
print_args("alo", "garazh")
print_args(23456, "gjiof", [], ("solo", "salo"))
# print_args("alo", name="garazh") # TypeError: print_args() got an unexpected keyword argument 'name'

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John", age=25, city="New York")

def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_args_and_kwargs(1, "hello", 3.14, name="John", age=25)

print(all([1, "sss", 3.15, True]))
print(all([1, "sss", 0, True]))
print(any([1, 2, 3]))
print(any([0, 2, 0, 0, 0, 0, 0, 0,]))
print(any([0, 0, 0]))
print(ascii("Україна"))
print(bin(7) ,  bin(8))
print(chr(1111))
print(ord("ї"))
code = '''
def greet(name):
    print("Hello, " + name)

greet("World")
'''
compiled_code = compile(code, '<string>', 'exec')
exec(compiled_code)

print(dict(a="b", b=123))
print(hash("Hello, World!"))

hello = "hello"  
print(id(hello))

# value = input("Input value:")
x = 5
print(isinstance(x, int))  # True
print(isinstance(x, (str, float, bool)))
print(len("len"))
print(max([3, 1, 4]))
print(min([3, 1, 4]))
print(pow(3, 3), 3 ** 3)
print(range(5))
print(round(2.60))  # 3
print(round(2.45, 1))
print(sum([1, 1, 1]))

def square_b(a:int):
    return a ** 2

square = lambda a: a ** 2
print(square(5))

append = lambda x, y: x + y
print(append(3, 4))

my_dict = {'apple': 5, 'banana': 10, 'kiwi': 3, 'orange': 8, 'a':100}
# Знаходження ключа з максимальним значенням
max_key = max(my_dict, key=lambda k: my_dict[k])
print(max_key)
