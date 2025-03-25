talking=str(input())=="True"
hour=int(input())
def parrot():
    if talking and (hour<7 or hour>20):
        return True
    else:
        return False
print(parrot())