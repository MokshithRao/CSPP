def expression(l):
    try:
        r = eval(l)
        print(r)
    except ZeroDivisionError:
        print("Division by zero error")
expression(input())