a=int(input())
def decrementGlobal():
    global a
    a-=2
    return a
print(decrementGlobal())
print(a)
