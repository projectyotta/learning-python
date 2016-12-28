
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

    # locale specific information


if __name__=="__main__":
    main();