
# add soms for better reading
its_my_great_variable = "GREAT!!!!!"

'''
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
'''
is_my_var_false = False
PI = 3.141549
side_a = 5
sibe_b = 7

'''
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
'''
print("2 % 2", 2 % 2)
print("5**12", 5**12)
print("25**(1/2)", 25**(1/2))

div_num = 0.0000000000000001
big_var = 1/div_num
print(big_var)
small_var = big_var * div_num
print(small_var)

a = 5
b = 2
result = a // b 
print(result)
result_2 = a % b
print(result_2)

apples = True
shugar = True

print("and")
result_3 = apples and not shugar
print(result_3)
result_3 = not apples and shugar
print(result_3)
result_3 = not apples and not shugar
print(result_3)
result_3 = apples and shugar
print(result_3)

print("or")
buryak = True
green_shpinat = True
result_4 =  buryak or not green_shpinat
print(result_4)
result_4 =  not buryak or green_shpinat
print(result_4)
result_4 =  buryak or green_shpinat
print(result_4)
result_4 =  not buryak or not green_shpinat
print(result_4)

"""
(       )       [       ]       {       }
,       :       .       ;       @
"""
voice_yes = 304
voice_no = 2

result_5 = (voice_yes + voice_no) / 2
print("(voice_yes + voice_no) / 2 ==", result_5)

my_list = ["Mary", "Helen", "Oleksandra", "Viktoria"]
print(my_list)
print(my_list[2])

dictionary = {"name": "Alex", "job_title": "SDET", "years_counter": 10}
my_set = {"Mary", "Helen", "Oleksandra", "Viktoria", 1.2345}

my_tuple = ("Mary", "Helen", "Oleksandra", "Viktoria")

if result_5 > 100 or my_list[2] == "Alex":
    print("yes, all fine")

for i in dictionary:
    print(i)

def my_fumction_name():
    pass # пропуск
    # if result_5 == 2:
    #     pass

class MyClass:
    a = 5
    pass

print(MyClass.a)

str_value_1 = "Print 1"; str_value_2 = "Out 2"

# @decorator
# def function():
#     pass
single_quotes = 'Це рядок з одинарними лапкми подовжений'
double_quotes = "Це рядок з звичайними, подвійими лапкми"

long_quotes = '''Це 
рядок з тикратним
повторенням лапок'''

print(long_quotes)

"""
    Обмеження цілих чисел у Python залежить від архітектури вашої системи. 
    У зазвичай 32-бітних системах це може бути від -2,147,483,648 до 2,147,483,647, 
    а на 64-бітних системах це може бути від 
    -9,223,372,036,854,775,808 до 9,223,372,036,854,775,807.
"""
decimal_int = 42
octal_int = 0o52
hexadecimal = 0x2a
bin_int = 0b101010
print(decimal_int, octal_int, hexadecimal, bin_int)

0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0E0 # Floating-point literals*

a = 0.1 + 0.2
b = 0.3

print("a =", repr(a))
print("b =", repr(b))
print("a == b:", a == b)
print("(a) == b:", round(a, 6) == b)
print("Різниця (a - b):", a - b)

print(single_quotes[0]) # 1 CHAR FOR STRING
len_single = len(single_quotes)
print("len for string", len_single)
string_out = f"len for '{single_quotes}' is {len_single}"
print(string_out)
string_out_2 = "len for ", single_quotes, " is ", len_single
print("len for", single_quotes, "is", len_single, sep="_")
print("a", "b", "c", sep="_", end="$")
print("a", "b", "c", sep="_", end="_")
print("a", "b", "c", sep="_", end="$")
