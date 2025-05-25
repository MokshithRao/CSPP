# Problem 2: Check Divisibility
# Description: 
# Write a program that checks whether a given number is divisible by both 3 and 5. If it is, print "Divisible by both 3 and 5". If it's only divisible by 3, print "Divisible by 3". If it's only divisible by 5, print "Divisible by 5". If it's not divisible by either, print "Not divisible by 3 or 5". 


def Check_div():
    a=int(input())
    if a%3==0 and a%5==0:
        return "divisible by both 3 and 5"
    elif a%3==0:
        return "divisible by 3"
    elif a%5==0:
        return "divisible by 5"
    else:
        return "not divisible by 3 or 5"
print(Check_div())