# http://strftime.org/ , has everything that you need.
from datetime import datetime

def main():

    # get the current date to be able to format it
    now = datetime.now()
    print now

# to format, the following structure is used :
# for year : %y or %Y , for weekday : %a or %A , for month : %b or %B , for day of month : %d
    # NOTE : putting in %y gives you 16 (abbreviated year), and putting in %Y gives you 2016 (the entire year) ( considering the current year to be 2016 )

    x=now.strftime("%Y")
    print x

    print now.strftime("%a , %B %d , %Y ")

    # locale specific information - used for trying to understand if datetime can be printed accordig to the region that you are in
    # I guess this is useful especially for web applications , where users tend to access the webpage data from multiple locations
    # codes used for this kind of thing : %c ( date and time , %x ( only date )  , %X ( only time )
    print now.strftime(" locale specific one :  %c")
    print now.strftime(" locale specific two :  %x")
    print now.strftime(" locale specific three :  %X")

    # locale specific for time
    # %I %H : 12 or 24 hour , %M : Minute , %S : Second , %p : locale's AM/PM
    print now.strftime("current time now is %I:%m %S %p")
    # 24 hour clock
    print now.strftime("time in 24 hour format is %H:%M")


if __name__=="__main__":
    main();