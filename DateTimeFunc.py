from datetime import datetime

dt = datetime.now()

print '%s/%s/%s' % (dt.month, dt.day, dt.year)
print dt

print dt.month
print dt.day
print dt.year 

print '%s-%s-%s' % (dt.month, dt.day, dt.year)

print dt.hour
print dt.minute
print dt.second

print '%s:%s:%s' % (dt.hour, dt.minute, dt.second)

print '%s/%s/%s %s:%s:%s' % (dt.month, dt.day,
dt.year, dt.hour, dt.minute, dt.second)

import datetime

today = datetime.date.today()
print(today)
oneday = datetime.timedelta(days=1)
tomorrow = today + oneday
print("Tomorrow is: ", tomorrow)


bdate = datetime.date(1952,11,11)
print(bdate.strftime("%A"))


from datetime import datetime, timedelta

d1 = datetime(year=2017, month=9, day=11,hour=16, minute=34)
d2 = datetime(year=1952, month=11, day=11,hour=9, minute=2)
td = d1 - d2

ts = td.total_seconds()
print 'total seconds: ', ts

seconds_in_day = timedelta(days=1).total_seconds()
print 'seconds in day', seconds_in_day
days = ts/seconds_in_day
print 'days: ', days
years = days/365.2524
print years

d1 = datetime(year=2017, month=9, day=11,hour=16, minute=34)
d2 = datetime(year=1952, month=11, day=11,hour=9, minute=2)

def age_years(d1, d2):
    
    td = d1 - d2

    ts = td.total_seconds()
    seconds_in_day = timedelta(days=1).total_seconds()
    days = ts/seconds_in_day
    years = days/365.2524
    return years
    
print 'Years: ',age_years(d1, d2)
##
import datetime

print(dir (datetime))

gvr = datetime.date(1952,11,11)

print(gvr)

print(gvr.year)
print(gvr.month)
print(gvr.day)
print(gvr.strftime("%A,%B,%d,%Y"))
message = "John was born on {:%A,%B,%d,%Y}."
print(message.format(gvr))

mill = datetime.date(2000,1,1)
dt = datetime.timedelta(100)

print (mill + dt)

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22,27,0)
launch_datetime = datetime.datetime(2017, 3, 30, 22,27,0)

print(launch_date)
print(launch_time)
print(launch_datetime)

now = datetime.datetime.today()
print(now)

moon_landing = "7/20/1969"
moon_landing_dt = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print (moon_landing_dt)
print (type(moon_landing_dt))

xmas = datetime.date(2017, 12, 25)
print xmas

diff = xmas - today
print diff


import datetime
Year = int(input("Enter year born"))
Month = int(input("Enter month born"))
Day = int(input("Enter day born"))

dob = datetime.datetime(Year, Month, Day)
age = (datetime.datetime.now() - dob)

print("You are " + str(age.days)+ " days old.")

convertdays = int(age.days)
ageyears = convertdays/365.0

print("Or " + str(ageyears) + " years old.")

def age_of_human(Year, Month, Day):
    dob = datetime.datetime(Year, Month, Day)
    age = (datetime.datetime.now() - dob)

    print("You are " + str(age.days)+ " days old.")

    convertdays = int(age.days)
    ageyears = convertdays/365.0

    print("Or " + str(ageyears) + " years old.")
    
age_of_human(Year, Month, Day)



