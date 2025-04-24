a,b = input().split()
a=int(a)
b=int(b)
def power_cal():
    d = 1
    for i in range(1,b+1):
        d = d * a
    return d
print(power_cal())
