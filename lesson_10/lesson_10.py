# excepton

def divide(a, b):
    result = a / b
    return result


def main():
    a, b = 10, 1
    try:
        result = divide(a, b)
    except ZeroDivisionError as e:
        print(f"ERROR: {e}")
    else:
        print(f"Результат ділення {a} на {b}: {result}")
    finally:
        print("Цей блок виконається завжди")
    print("hello")


def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    return age

# try:
#     user_age = int(input("Введіть ваш вік: "))
#     user_age = check_age(user_age)
#     print(f"Ваш вік: {user_age}")
# except Exception as e:
#     print(f"Error {e}")


def get_input_age(msg = "Введіть ваш вік: " ):
    try:
        user_age = int(input(msg))
    except ValueError as e:
        print("Invalid input. Expected number value")
        return get_input_age()
    return user_age


def print_checked_age():
    user_age = get_input_age()
    try:
        user_age = check_age(user_age)
    except ValueError as e:
        print(f"Error age value: {e}")
        user_age = None
    print(f"Ваш вік: {user_age}")


# class intro
class TooLargeValueError(Exception):

    def __init__(self, limit):
        self.limit = limit
        message = f"Значення перевищує ліміт {limit}"
        super().__init__(message)


def get_money(user_input:int = 0):
    limit = 100_000
    if user_input == 0:
        user_input= get_input_age("Введіть сумму зняття: ")
    if user_input > limit:
        raise TooLargeValueError(limit)
    else:
        print("Дякую! Ви ввели припустиме значення. Отримайте кошти в віконечку")
        return True


class Car:
    speed = 0
    __engine = False
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        self.__engine = True
    
    def get_engine(self):
        return self.__engine


class Fruit:
    def __init__(self, color="green"):
        self.color = color


class BankAccount:

    def __init__(self, initial_balance):
        self.__balance = initial_balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if isinstance(value, (int, float)):
            self.__balance = value


class Animal:
    def birth(self):
        return "this animal has births"

    def speak(self):
        pass  # Загальний метод для всіх тварин

class Dog(Animal):
    def speak(self):
        return "Гав!"  # Собака видає свій власний зв

class Cat(Animal):
    def speak(self):
        return "Мяв!"


if __name__ == "__main__":

    my_firt_car = Car("Nissan", "Patrol")
    print(type(my_firt_car))
    print(my_firt_car.model)
    print(my_firt_car.brand)
    my_second_car = Car("Toyota", "Corolla")
    print(my_second_car.model)
    print(my_second_car.brand)

    apple = Fruit()
    orange = Fruit("orange")
    print(apple.color)
    apple.color = "dark"
    print(apple.color)
    print(orange.color)

    account = BankAccount(1000)
    print(account.get_balance())
    account.__balance = 10000000 # incapsulo

    account.set_balance(2000)
    print(account.get_balance())

    bingo = Dog()
    murzik = Cat()
    print(bingo.birth(), bingo.speak())
    print(murzik.birth(), murzik.speak())

    my_3d_car = Car("Volvo", "Command")
    print(my_3d_car.brand)
    print(my_3d_car.model)
    my_3d_car.speed = 180
    print(my_3d_car.speed)
    print(my_3d_car.get_engine())
    print(my_3d_car.start_engine())
    print(my_3d_car.get_engine())
    print(my_firt_car.get_engine())
