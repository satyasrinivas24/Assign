#---------------------------------------------------------------WHILE LOOP-------------------------------------------------------------
#

#1. Write a function that accepts any number of numbers using *args and returns the sum of all
# numbers
def add_number(*args):
    return sum(args)
a = add_number(1,4,78,67)
print(a)