# date and time
import time

current_time = time.localtime()
print(current_time)
# DST - Daylight Saving Time — це англомовне позначення переходу на літній час.

actual_time = time.asctime((2025,10,6,19,23,23,0,279,1))
print(actual_time)
epoch_time = time.ctime(0)
print(epoch_time)
nix_time_now = time.ctime(1756547846)
print("unix time 1", nix_time_now)
print(time.time())
time.sleep(0.0005)
print(time.time())
print(time.ctime(time.time()))

today = "Sun Oct  5 19:30:00 2025"
today_2 = "Oct 5, 2025"
some_day_2 = "Dec 21, 2022"
pattern = "%b %d, %Y"
my_datetime = time.strptime(today_2, pattern)
print(my_datetime)
print(time.strptime("19:45:55", '%H:%M:%S'))
# Рядок з часом
time_string = '2023/12/31 23:59:59'
# Формат рядка
format_string = '%Y/%m/%d %H:%M:%S'
# Перетворення рядка у структуру часу
time_obj = time.strptime(time_string, format_string)
print(time_obj)

good_time_output = time.strftime("Now year %Y %m month and day is %d time is: %H:%M",
                     time.localtime())
print(good_time_output)
