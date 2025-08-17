# print("Enter a 2D list (each row separated by a new line, numbers separated by spaces):")

# # Step 2: Create an empty list to hold the 2D list
# my_2d_list = []

# # Step 3: Read the input line by line until the user presses Enter without input
# while True:
#     # Read one line of input
#     x = []
#     input_str = input()
    
#     # If the user just pressed Enter (empty line), break the loop
#     if not input_str:
#         break
    
#     # Step 4 & 5: Use list comprehension to split the line and convert to integers
#     input_str = input_str.split() #[1,2,3]
#     print(input_str)
#     for i in input_str:
#         x.append(int(i))
    
#     my_2d_list.append(x)

# # Step 6: Print the resulting 2D list
# print("Your 2D list is:", my_2d_list)


# 1.
x = input().split()

#2. 
print("Enter a 2D list (each row separated by a new line, numbers separated by spaces):")

# Step 2: Create an empty list to hold the 2D list
my_2d_list = []

# Step 3: Read the input line by line until the user presses Enter without input
while True:
    # Read one line of input
    x = []
    input_str = input()
    
    # If the user just pressed Enter (empty line), break the loop
    if not input_str:
        break
    
    # Step 4 & 5: Use list comprehension to split the line and convert to integers
    input_str = input_str.split() #[1,2,3]
    print(input_str)
    for i in input_str:
        x.append(int(i))
    
    my_2d_list.append(x)

# Step 6: Print the resulting 2D list
print("Your 2D list is:", my_2d_list)

# 3. 

x = input.split(',')

# 4.
x = []
while True:
    s = int(input())
    if not s:
        break

    x.append(s)
print(x)

# 5. 
n = int(input())
x = []
for i in range(n):
    y = int(input())
    x.append(y)

print(x)

# 6. 

x,y = input().split()
# x,y = map(int,input().split())
x = int(x)
y = int(y)
k = []
for i in range(x):
    # p = input().split()
    # print(p)
    # q = []
    # for j in p:
    #     q.append(int(j))
    # k.append(q)
    k.append(list(map(int,input().split())))
print(k)

# 7.
x = []

n = int(input())

for i in range(n):
    x.append(list(map(int,input().split())))

print(x)

# 8. 
s = input().split('/')
s = list(map(int,s))

# or s = list(map(int,(input().split('/'))))

# 9. 
# y = ',./#@%^&*'
x = input().replace(',',' ')
print(x)

# 10.

n=int(input())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))

print(li)

# 11. 
l = list(map(int, input().split()))
print(l)
#12
n=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    y=input()
    if y=="Sum":
        s=sum(x)
        print(s)
    elif y=='Product':
        prod=1
        for i in x:
            prod*=i
        print(prod)

#13
l = eval(input())
print(l)

#14
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
n = int(input())
x = []

while True:
    s = input()

    if not s:
        break

    s = list(map(int,s.split()))
    x.extend(s)

#15
t = int(input())
for i in range(t):
    d, k = input().split()
    x = []
    for j in range(int(d)):
        x.append(int(input()))
    
    print(x)

# 16

l = input().replace(";"," ")
l = l.replace(","," ")
l = l.replace("/"," ")
l = l.replace(":"," ")

l = list(map(int,l.split()))

#17
lst = input()
lst = lst.replace("[","").replace("]","")
lst = list(map(int,lst.split(",")))
print(lst)

# 18
d = {}
while True:
    s = input()

    if not s:
        break

    k,v = s.split(":")
    d[k.strip()] = v.strip()
print(d)

#19
s=input().replace('(','').replace(')',"")
s=s.replace(']','').replace('[','')
s=s.replace('{','').replace('}','')
s=list(map(int,s.split(',')))
print(s)

#20
d = input().split()
print(d) #[A-1, B-2, C-3]
A = d[0].split('-')[1]#[A,1]
B = d[1].split('-')[1]
C = d[2].split('-')[1]
print(A, B, C)

#21
t = input().split(',')

for i in range(len(t)):
    t[i] = t[i].replace('#', '').replace('&', '').replace('*', '')
print(t)

# 22.

l = []
while True:
    s = input()
    if not s:
        break
    s = s.replace(","," ").replace(";"," ")
    l.append(list(map(int,s.split())))
print(l)

# 24. 
s=input().split("by")
s[0]=s[0].replace("-",",")
print(s)
    
