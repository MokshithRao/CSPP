def sleep():
    weekday=str(input())=="True"
    vacation=str(input())=="True"
    return not(weekday) or vacation
print(sleep())
