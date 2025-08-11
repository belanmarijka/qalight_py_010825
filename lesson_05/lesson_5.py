# tuple

single_element_tuple = (42,)
# single_element_tuple =  42,

mixed_tuple = (1, 'hello', 3.14, True)
# mixed_tuple = 1,'hello', 3.14, True

first = mixed_tuple[0]
last = mixed_tuple[-1]
print(first, last)
print(mixed_tuple.count('hello'))

my_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = my_tuple.count(2)
print("count_of_2", count_of_2)
index_of_2 = my_tuple.index(2)
print("index_of_2", index_of_2)
index_of_2_2 = my_tuple.index(2, index_of_2 + 1)
print("index_of_2_2", index_of_2_2)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
subset = my_tuple[2:7]
print(subset)
subset_2 = my_tuple[2:8:2]
print(subset_2)

one, two, thre, four = mixed_tuple
print("four vals", one, two, thre, four)
*one, two, thre = mixed_tuple
print("unpack to 1", one, two, thre)
one, *two, thre = mixed_tuple
print("unpack to 2", one, two, thre)
one, two, *thre = mixed_tuple
print("unpack to 3", one, two, thre)
one, *two = mixed_tuple
print(one, two)

my_string = "Привіт, світ!"
tuple_from_string = tuple(my_string)
print(tuple_from_string)

my_list = [1, 2, 3, 'Python', True]
tuple_from_list = tuple(my_list)
print(tuple_from_list)

# list
my_list_2 = [1, 2, 3, 'a', 'b', 'c']
print(my_list_2[0])
print(my_list_2[-1])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subset = my_list[2:7]
print(subset)
subset_2 = my_list[2:9:2]
print(subset_2)
my_list.append(4)
print(my_list)
jolm = [4, 5, 6]
my_list.append(jolm)
print(my_list)
print(len(my_list))
print(my_list[-1][1])
my_list.append((12, 33, 445))
print(my_list[-1][1])

my_list.extend(jolm)
print("extend", my_list)
my_list.extend((12, 33, 445, ("foo", "bar")))
print("extend 2", my_list)

my_list.insert(7, "fun-fun-fun")
print("insert", my_list)

my_list.remove(4)
print("remove", my_list)

popped_element = my_list.pop(10)

print("popped_element", popped_element)  
print("my_list", my_list)

index_of_4 = my_list.index(4) 
print(index_of_4)

count_of_2 = my_list.count(4)
print(count_of_2)


small =  [0, 1, 2, 3, 4]
*one, two, thre = small
print("3 vals small", one, two, thre)
one, *two, thre = small
print("3 vals small", one, two, thre)
one, two, *thre = small
print("3 vals small", one, two, thre)

numbers = [1, 2, 3, 4, 5, 7, 2, 4, 2, 0]

sorted_list = sorted(numbers)
print("sorted_list", sorted_list)
print("numbers after sorted", numbers)
print(numbers.sort())
print("numbers after sort", numbers)

fruits = ["яблуко", "апельсин", "бана", "груша", "слива"]
sorted_words = sorted(fruits, key=lambda x: len(x))
print(sorted_words)


my_string = "Привіт, світ!"
list_from_string = list(my_string)
print(list_from_string)
split_by_coma = my_string.split(", ")
print(split_by_coma)

my_tuple = (10, 20, 30, 40, 50)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# Генерацiя спискiв (List Comprehension)

squares = [x**2 for x in range(10)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

lengths_fruits = [len(word) for word in fruits]
print(lengths_fruits)

# set

fruits = {"яблуко", "банан", "апельсин", "apple", "apple", "яблуко"}
print(fruits)

print("apple" in fruits)
print(1 in numbers)
popped_element = fruits.pop()
print(f"Видалений елемент: {popped_element}, Залишок: {fruits}")
fruits.update({"apple"})
fruits.remove("apple") # можке бути помилка
print(f"Множина після видалення: {fruits}")

my_set = {1, 2, 3, 4}
add_set = {3, 4, 5, 6, 7}

uni_set = my_set.union(add_set)
# або
# uni_set = my_set | add_set
print(uni_set)

# logical_intersection = my_set.intersection(add_set)
# або
logical_intersection = my_set & add_set
print(logical_intersection)
logical_difference_1 = my_set - add_set
print(logical_difference_1)
logical_difference_2 = add_set - my_set
print(logical_difference_2)
# logical_difference = set1.difference(set2)

# logical_symmetric_difference = set1.symmetric_difference(set2)
# або
logical_symmetric_difference = add_set ^ my_set
print(logical_symmetric_difference)

my_text_set = set("Приклади створення множини в Python з інших типів даних за допомогою")
print(my_text_set)

f_list = ["яблуко", "банан", "апельсин", "apple", "apple"]
set_from_list = set(f_list)
print(set_from_list, len(set_from_list) == len(f_list))
