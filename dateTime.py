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

