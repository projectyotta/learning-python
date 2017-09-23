
from datetime import date
from datetime import datetime
from datetime import time

def main():

    # get today's date
    today = date.today()
    print "today's date is" , today

    # print the individual components of a date
    print "today's date is", today.month , " , ", today.day," , ", today.year

# can also get the weekday as a number ( 0 for monday and 6 for sunday )
    print "the weekday is", today.weekday()
    # get the date and time
    today = datetime.now()
    print "the date and time is",today;

# how do you get the time from the datetime class
    t = datetime.time(datetime.now())
    print " the time is", t

# how do you make the day appear using the weekday property
    t1=today.weekday()
    print t1
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # first print the weekday number
    print "The weekday number is", t1
    # print the day of the week by indexing it with days
    print "The day of the week is", days[t1]



if __name__=="__main__":
    main();

