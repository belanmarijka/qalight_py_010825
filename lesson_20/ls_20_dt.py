from datetime import datetime
from datetime import timedelta
from datetime import timezone

print(datetime.today())

mydatetime = datetime.fromtimestamp(1706551390)
print(mydatetime, type(mydatetime))
ord_day = 278
dt = datetime.fromordinal(ord_day)
print(dt)
day_number = datetime.today().toordinal()
print(f'Порядковий номер сьогоднішнього дня: {day_number}')

current_datetime = datetime.now()
print("Поточна дата і час:", current_datetime)

incoming_date = "Aug 24, 1991"
dt_incoming_date = datetime.strptime(incoming_date, '%b %d, %Y')
print(dt_incoming_date)
dt_incoming_time_out = dt_incoming_date.strftime("%H:%M:%S and %Y-%m-%d")
print(dt_incoming_time_out)

dt_01 = "19:45:23"  # Germany
dt_02 = "20:00:22"
dt_03 = "20:45:11"
dt_04 = "20:45:23"  # Kyiv

def to_hour(time_in_hour:str):
    return datetime.strptime(time_in_hour, "%H:%M:%S")

dt_01_1 = to_hour(dt_01)
dt_02_1 = to_hour(dt_02) 
dt_03_1 = to_hour(dt_03)
dt_04_1 = to_hour(dt_04)

diff_time = dt_02_1 - dt_01_1
print("Diff", diff_time, type(diff_time))

if dt_02_1 - dt_01_1 <= timedelta(minutes=15):
    print("yes")
else:
    print("false")

if dt_04_1 - dt_03_1 > timedelta(seconds=30):
    print("error")

print(datetime.today() + timedelta(days=1))
print("UTC+++++++++++++++++++")
d = datetime.now(tz=timezone.utc)
print(d)
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.timetuple())
print(d.weekday())
dd = d.replace(day=5)
print(dd)
print(dd.isoweekday())

td = timedelta(days=5, hours=3, minutes=30)
print(td)
total_seconds = td.total_seconds()
print(total_seconds)

unknow_tz = timezone(timedelta(hours=3))
dt = datetime.now(unknow_tz)
print(dt)
