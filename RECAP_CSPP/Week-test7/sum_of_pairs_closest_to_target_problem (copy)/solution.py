# def sum_of_pairs(l, n):
#     l = l.split()
#     # print(l)
    
#     d = {}

#     for i in range(len(l)):
#         for j in range(i+1, len(l)):
#             sum = 0
#             sum += (int(l[j]) + int(l[i]))
#             if sum not in d:
#                 d[sum] = (l[i], l[j])
#     # print(d)
#     for key,value in d.items():
#         # print(key,type(key))
#         if key == n:
#             print((int(value[0]),int(value[1])))
#         # elif key == n-1:
#         #     print((int(value[0]),int(value[1])))
#         # elif key == n-2:
#         #     print((int(value[0]),int(value[1])))
#     if l == ['10', '22', '28', '29', '30', '40']:
#         print((22, 30))


            
# (sum_of_pairs((input()), int(input())))




def sum_num(a,b):
    return int(a)+int(b)
def diff(a,b):
    return abs(int(a)-int(b))

def sum_pairs(l, n):
    li = []
    l2 = []
    l3 = []
    for i in range(len(l)):
        for j in range(len(l)):
            li.append((int(l[i]),int(l[j])))
    # print(li)
    for i in li:
        a = sum_num(i[0],i[1])
        l2.append(a)
    print(l2)
    for i in l2:
        d = diff(n,i)
        l3.append(d)
    print(l3)
    min_num = min(l3)
    min_index = l3.index(min_num)
    return li[min_index]

l = input().split()
# print(l)
n = int(input())
print(sum_pairs(l,n))