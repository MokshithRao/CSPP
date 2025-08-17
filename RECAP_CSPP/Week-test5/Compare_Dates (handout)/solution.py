# def leap_year(year):
#     if year%100 == 0:
#         if year%400 == 0:
#             return True
#     elif year%4 == 0:
#         return True
#     else:
#         return False




# # def is_valid_date(s):
# #     s = s.split("/")

# #     date = int(s[0])
# #     month = int(s[1])
# #     year = int(s[2])

# #     if year<1000 or year>9999:
# #         return False
# #     if month<1 or month>12:
# #         return False
    
# #     if date < 26 and month < 10 and year < 2024:
# #         return False
    
# #     days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# #     if leap_year(year):
# #         days[2] = 29
# #     if date<1 or date>days[month]:
# #         return False

# #     else:
# #         return True


# # # print(is_valid_date(input()))



# def compare_dates(date1 , date2):
#     date11 = date1.split("/")
#     date22 = date2.split("/")

#     d1 = int(date11[0])
#     m1 = int(date11[1])
#     y1 = int(date11[2])


#     d2 = int(date22[0])
#     m2 = int(date22[1])
#     y2 = int(date22[2])

#     days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#     if leap_year(y1) or leap_year(y2):
#         days[2] = 29

    

#     if d1 < d2 and m1 < m2 and y1 < y2:
#         print("-1")
#     elif d1 > d2 and m1 > m2 and y1 > y2:
#         print("1")
#     elif d1 == d2 and m1 == m2 and y1 == y2:
#         print("0")
#     elif d1 > d2 and m1 == m2 and y1 == y2:
#         print("1")
#     elif d1 < d2 and m1 == m2 and y1 == y2:
#         print("-1")
#     elif d1 > d2 and m1 < m2 and y1 == y2:
#         print("-1")
#     elif d1 > d2 and m1 > m2 and y1 < y2:
#         print("-1")
#     elif d1 < d2 and m1 < m2 and y1 > y2:
#         print("1")
#     elif d1 == d2 and m1 > m2 and y1 == y2:
#         print("-1")
#     elif d1 == d2 and m1 < m2 and y1 == y2:
#         print("1")
    

#     if d1<1 or d1>days[m1]:
#         print(f"Invalid date {date1}")
#     if d2<1 or d2>days[m2]:
#         print(f"Invalid date {date2}")
    
    
    

# compare_dates(input(), input())
    
    

def leap_Year(Y):
    if Y%4 == 0:
        if Y%100 == 0:
            if Y%400 == 0:
                return True
            return False
        return True
    return False
def Vaidate_Date(date1):
    date1 = date1.split("/")
    D = int(date1[0])
    M = int(date1[1])
    Y = int(date1[2])
    if Y<1000 or Y>2024:
        return False
    if Y == 2024:
        if M>10:
            return False
        elif M==10:
            if D>26:
                return False
    if M<1 or M>12:
        return False
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_Year(Y):
        days[2] = 29
    if D>days[M]:
        return False
    return True
def Compare_Date(date1,date2):
    if not Vaidate_Date(date1):
        return f"Invalid date {date1}"
    if not Vaidate_Date(date2):
        return f"Invalid date {date2}"
    date1 = date1.split("/")
    date2 = date2.split("/")
    D1 = int(date1[0])
    D2 = int(date2[0])
    M1 = int(date1[1])
    M2 = int(date2[1])
    Y1 = int(date1[2])
    Y2 = int(date2[2])
    if Y1<Y2:
        return -1
    elif Y1>Y2:
        return 1
    else:
        if M1<M2:
            return -1
        elif M1>M2:
            return 1
        else:
            if D1<D2:
                return -1
            elif D1>D2:
                return 1
            else:
                return 0
print(Compare_Date(input(),input()))