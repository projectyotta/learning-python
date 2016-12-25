# testing out how loops function in python
def main():
    x=0
    # only two ways of doing loops in python - you either use while loops or for loops .

    # a simple while loop

    while (x<5):
        print x
        x=x+1
# a simple for loop
    print '\n'
    for y in range(5,10):
     print y
# you can also run a for loop through a collection
# this is a collection
    print '\n'
    days = ["mon", "tue","wed","thu","fri","sat","sun"]
    for d in days:
        print d

# break and continue statements in python run pretty much like you would expect them to
# break is used for terminating a statement if a particular condition is encountered
# continue skips over the rest of the statements below it if the condition is encountered.

   # you can also use the enumerate function if you really need to count the ietsm in your collection

    print '\n'
    days = ["mon", "tue","wed","thu","fri","sat","sun"]
    for i,d in enumerate(days):
        print i,d



if __name__=="__main__":
    main()


