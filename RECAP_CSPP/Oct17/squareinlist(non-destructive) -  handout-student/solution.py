l = input()
list = l.split(",")
def list_squaring(list):
    lst = []
    for element in list:
        a = int(element)**2
        lst.append(a)
    return lst
print(list_squaring(list))



