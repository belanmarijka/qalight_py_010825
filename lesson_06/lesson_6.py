is_student = True
has_experience = True
is_know_python = False
age = 17

if __name__ == "__main__":

    if 0 <= age < 18:
        print("Ти children!")
    elif age >= 18:
        print("Ти повнолітній!")
    else:
        print("Wrong age")

    print("Next code")



    if age >= 18 and is_student:
        print("Ти студент і тобі більше 18 років.")
    elif age >= 18 or has_experience:
        print("Ти або дорослий, або у тебе є досвід роботи.")
    else:
        print("Ти не можеш бути студентом або тобі менше 18 років.")

    if (age >= 18 and not is_student) or (has_experience and is_know_python):
        print("You are either an adult student or have experience and are under 18.")
    else:
        print("You don't meet any of the specified conditions.")

    # False == "", '', 0, [], {}, (), None
    grade = 75

    if grade >= 90:
        print("Відмінно")
        if has_experience:
            print("You are GREAT")
            if age >= 18:
                pass
    elif grade >= 75:
        print("Добре")
    elif grade >= 60:
        print("Задовільно")
    else:
        print("Незадовільно")

    print("WHILE")
    count = 0
    while count < 5:
        print(count)
        count += 1

    # while True:
    print("FOR")
    numbers = [1, 2, 3, 4, 5]
    for i in numbers:
        print(i)

    print("FOR in range")
    for i in range(5):
        print(i)

    print("FOR in str")
    message = "Hello"
    for char in message:
        print(char)

    person = {"name": "John", "age": 30, "city": "New York"}
    for key, value in person.items():
        print(key, ":", value)

    age = 25
    is_student = True

    if age >= 18:
        print("You are an adult.")

        if is_student:
            print("And you are a student.")

            # Вкладений цикл
            for semester in range(1, 4):
                print("Semester:", semester)
        else:
            print("But you are not a student.")
    else:
        print("You are not an adult.")


    for i in range(3):
        print("Outer loop, iteration:", i)

        # Вкладена умова
        if i % 2 == 0:
            print("This is an even iteration.")
        else:
            print("This is an odd iteration.")

    for i in range(5):
        if i == 3:
            print("Break викликаний на i =", i)
            break
        print(i)


    for i in range(5):
        if i == 3:
            print("continue викликаний на i =", i)
            continue
        print(i)

    target_value = 7
    for i in range(10):
        if i == target_value:
            print("Знайдено шукане значення:", i)
            break
        print(i)

    for i in range(10):
        if i % 2 == 0:
            continue
        print("Непарне число:", i)