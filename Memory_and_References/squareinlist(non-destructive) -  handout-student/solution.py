a = input()
lst=a.split(",")

def square(l):
    list= []
    for i in l:
        list1 = int(i)**2
        list.append(list1)
    return list   
        
print(square(lst))