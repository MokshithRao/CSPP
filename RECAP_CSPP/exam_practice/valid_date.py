def is_valid_date(date):
    if len(date) != 10 or date[2] != '/' or date[5] != '/':
        return False
    
    day, m, y= date.split('/')
    
    if not (day.isdigit() and m.isdigit() and y.isdigit()):
        # print("1")
        return False
    
    day = int(day)
    m = int(m)
    y= int(y)

    if y< 1000 or y> 9999:
        # print("2")
        return False

    if m < 1 or m > 12:
        # print("3")
        return False

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_y(y):
        # print("4")
        days[1] = 29

    if day < 1 or day > days[m - 1]:
        return False

    return True

def leap_y(y):
    return (y% 4 == 0 and y% 100 != 0) or (y% 400 == 0)

print(is_valid_date(input()))



from datetime import datetime

def is_valid_date(date):
    try:
        p = datetime.strptime(date, "%d/%m/%Y")
        # print()
        return True
    except ValueError:
        return False
# print(is_valid_date(input()))



def is_valid_date1(date):
    try:
        p = datetime.strptime(date, "%m/%d/%Y")
        return True
    except ValueError:
        return False
# print(is_valid_date(input()))

def is_valid_date2(date):
    try:
        p = datetime.strptime(date, "%Y/%m/%d")
        return True
    except ValueError:
        return False
# print(is_valid_date(input()))

def valid(a):
    if is_valid_date(a) or is_valid_date1(a) or is_valid_date2(a):
        return True
    else:
        return False
print(valid(input()))