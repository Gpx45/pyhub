"""working further with dates."""
import datetime
time = datetime.date
# print(time)
# This will show me the date class within the datetime library

timeToday = datetime.date.today()
print(timeToday)
# this will return the current date.

timeDay = datetime.date.today().day, 'Day'
print(timeDay)
# This shows me the day of today. By calling on the attribute that is in
# today() function.

timeMonth = datetime.date.today().month, 'Month'
print(timeMonth)
# This shows me the month. By calling on the attribute that is in
# today() function.

timeYear = datetime.date.today().year, 'Year'
print(timeYear)
# This shows me the year. By calling on the attribute that is in
# today() function.

isoFormatted = datetime.date.isoformat(datetime.date.today())
print(isoFormatted)
# This uses the isoformat function and apply it to today() function
# This will return a formmated version of the date.
'''
this is a comment
'''
# Now lets take a look at how we can tell the time and also structure
# How it looks

import time
hour = time.strftime("%H:%M") # By default this will be 24h format
print(hour)

# Now for the day of the week and also tell if its night or day like 12h clock
dayOfW = time.strftime("%A %p")
print(dayOfW)
