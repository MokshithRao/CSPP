l = input()
lst=l.split(",")
def square(a):
    for i in range (len(a)):
        a[i] = int(a[i])**2
    return a  
        
print(square(lst))