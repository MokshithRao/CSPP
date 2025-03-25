def Makes_10():
    a=int(input())
    b=int(input())
    if (a == 10 or b == 10) or (a+b==10):
        return True
    else:
        return False
print(Makes_10())