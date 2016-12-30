
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

def main():
    #check out how a timedelta works
    print timedelta(days=30, weeks=4,  hours =5 , minutes = 45)
    # get today's date
    now = datetime.now()

    # get the time one year five weeks from now
    oneyearlater = now + timedelta(days=365, weeks=5)
    print "one year later: ", oneyearlater

    # date one week from now
    t = now - timedelta(weeks=1)
    s= t.strftime("%A %B %d, %Y")
    print " one week ago the date was :", s

    # how much time until thanksgiving
    tnx = date(now.year, 11,13)
    if now.date()>tnx:
        print "thanksgiving this year is already done"
        difference = (now.date() - tnx).days
        print " thanksgiving was done",difference,"days ago"
    else:
        nxtyr=now.year+1
        tnxnxtyr=date(nxtyr,11,13)
        difference1 = (tnxnxtyr-now.date()).days
        print "thanksgiving next year is",difference1,"days away"



if __name__=="__main__":
    main();

