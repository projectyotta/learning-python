

def func1():
    print"this is a function"
    return "this is what is being returned"
# when you define a function , and then just call it , it prints whatever is in it .
# But when you try to say print function () , you are in effect calling for a return value in there.
func1()
print func1()

# try something with arguments

def func2(arg1,arg2):
    return arg1+arg2
print "the answer is"
print func2(10,20)
print "\n"
# keep in mind that you cannot concatenate a string and an integer . That does not work
# even if you try stuff like print 123 + "text" . Gives yiu an error.

# default value for arguments in a function
# define a value of z=7
# if you give values , it will calculate for that.
# if you don't give , it will calculate for default values.
def func3(x=2,y=3):
    z=1
    for i in range(z):
        print x*y
        return x+x

print func3(3,4)
print func3()
func3(3,4)
func3()
print "\n"
func3(3)
print "\n"
# python can also figure out if the values of the variables that you have assigned are in the same order or not

func3(y=4,x=3)

# variable number of arguments

print"\n"

def func4(*args):
    x=0
    for y in args:
        x=x+y
    return x
print " the answer for func 4 is "
print func4(1,2,3,4,5)
