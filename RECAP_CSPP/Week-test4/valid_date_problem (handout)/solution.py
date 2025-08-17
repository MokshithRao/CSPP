def leap_year(n):
    if n%100 == 0:
        if n%400 == 0:
            return True
        else:
            False
    elif n%4 == 0:
        return True
    else:
        return False
# print(leap_year(int(input())))



def is_valid_date(s):
    s = s.split("/")

    date = int(s[0])
    month = int(s[1])
    year = int(s[2])

    if year<1000 or year>9999:
        return False
    if month<1 or month>12:
        return False
    
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year):
        days[2] = 29
    if date<1 or date>days[month]:
        return False

    else:
        return True



print(is_valid_date(input()))