head_01 = "заготовка для файла lesson4.py"

text_01 = """Цей  файл буде містити код для уроку 4.
Він може містити функції, класи або інші елементи, які будуть
використовуватися в рамках лекції.
"""
print(head_01[0])
print(head_01[1])
print(head_01[2])
print(head_01[-1])
print(head_01[-2])
print(head_01[-3])


print(text_01[5:15])
print(text_01[5:11115])
# print(text_01[11111]) # IndexError
print(text_01[15:])
print(text_01[:27])

print(text_01[5:115:2]) #

print(text_01[:3])

print(head_01[::-1])

print("len for head_01:", len(head_01))
print("len for text_01:", len(text_01))

for i in head_01:
    print(i)

result_str = "Hello" + " my students!"
print(result_str)
""
a_1 = "Aseeedfgh"
a_2 = "Kdlxeefjdklf"
a_3 = "Seekdjsk"

result_second_names = a_1 + "," + a_2 + "," + a_3
print(result_second_names)

result_second_names_v2 = " | ".join((a_1, a_2, a_3))
print(result_second_names_v2)

splitted = result_str.split()
print(splitted)

splitted_names = result_second_names.split(",")
print(splitted_names)
splitted_names = result_second_names.split("e")
print(splitted_names)

line = "apple,orange,banana,grape,orange,banana,grape"
parts = line.split(',', 2)
print(parts)

print(line.startswith("orange"))
print(line.startswith("ap"))
print(line.startswith("apple,orange,banana,grape,orange,banana,grape"))
print(line.endswith("orange"))
print(line.endswith("grape"))
print(line.endswith("grape,orange,banana,grape"))

hi_up = "HELLO ALL!"
print(hi_up, hi_up.isupper())

hi_small = 'helooooo'
print(hi_small, hi_small.islower())

hi_title = 'Helooooo'
print(hi_title, hi_title.istitle())

user_input = "HELLO all!"
small_ui = user_input.lower()
print(user_input, small_ui)

big_ui = user_input.upper()
print(user_input, big_ui)

title_ui = user_input.title()
print(title_ui)

capi_ui = user_input.capitalize()
print(capi_ui)

swap_ui = user_input.swapcase()
print(user_input, swap_ui)

word_for_finr = "міст"
index = text_01.find(word_for_finr)
print(index, text_01[index:index+10])
index_2 = text_01.find(word_for_finr, index + 1)
print(index_2, text_01[index_2:index_2+10])
verses = "ой у лузі чорна калина похилилася, ой то чорна Україна"
new_verses = verses.replace("чорна", "жовта")
print(new_verses)

vers_for_strips = "     Show   must go     on!    "
strip_1 = vers_for_strips.strip()
print(f"|{vers_for_strips}|{strip_1}|")

vers_for_strips_2 = "zooovv   Show   must go     on!    vvvvoooozzz"
strip_2 = vers_for_strips_2.strip("z").strip("o").strip("v").strip()
print(f"|{strip_2}|")

print(f"|{vers_for_strips.rstrip()}|")
print(f"|{vers_for_strips.lstrip()}|")

str_list = ["apple", "orange", "banana"]
joined_strs = ', '.join(str_list)
print(joined_strs)

# user_data = input("що ввести?")
number = int("123") 
print(number, type(number))
pi = float("3.141596")
print(pi, type(pi))
data_vals = "11,2,3,44,5"
data_list = data_vals.split(",")
print(data_list)

" " == True
"" == '' == """""" == '''''' == False
print(bool("False"))
