# using if , else and elseif functions

def main():
    x,y=1000,100

    if(x<y):
        st = " x is less than y "
    elif(x==y):
        st="x is equal to y"
    else:
        st="x is greater than y"
    print st
    str = " x is less than y " if (x < y) else "x is greater than or equal to y "
    print str
    if __name__=="__main__":
        main()



    # python also allows you to nest a if else statement in a single line , which is also pretty easy to do .

