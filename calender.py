import calendar
# calendar which starts with Monday to the left ( check output to get the hang of it
c=calendar.TextCalendar(calendar.MONDAY)
# you're telling the compiler which year , month etc you want the calendar for
str=c.formatmonth(2016,12,2,0)
print str

#creating an html formatted calendar
html = calendar.HTMLCalendar(calendar.SUNDAY)
str1 = html.formatmonth(2016,12)
print str1

# LOOP over the days of the month
# zeroes ( both before and after ) mean that day of week we started with is part of an overlapping month
for i in c.itermonthdays(2016,12):
    print i
# print list of months and days in a week , specific to locale .
for name in calendar.month_name:
    print name
for day in calendar.day_name:
    print day

print "\n"

# trying to get the first friday of each month. The logic behind weekone and weektwo is that the first two weeks of each monnth
# will have a friday , and this is being run for every month .

for m in range(1,13):
    cal = calendar.monthcalendar(2016,m)
    weekone= cal[0]
    weektwo= cal[1]

    if weekone[calendar.FRIDAY] !=0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print calendar.month_name[m],meetday


