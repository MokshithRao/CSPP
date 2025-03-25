# def posneg():
#     a=int(input())
#     b=int(input())
#     negative=str(input())=="True"
#     if (a<0 and b>0) or (a>0 and b<0) or (negative and a<0 and b<0):
#         return True
#     else:
#         return False

# print(posneg())

def posneg():
    a=int(input())
    b=int(input())
    negative=str(input())=="True"
    if negative:
        return a<0 and b<0
    else:
        return (a<0 and b>0) or (a>0 and b<0)

print(posneg())