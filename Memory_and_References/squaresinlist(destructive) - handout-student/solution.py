a = input()
lst=a.split(",")

def square(l):
    for i in range (len(l)):
        l[i] = int(l[i])**2
    return l 
        
print(square(lst))

