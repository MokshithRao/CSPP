a=int(input())
def incrementGlobal():
    global a
    a+=1
    return a
print(incrementGlobal())
print(a)
