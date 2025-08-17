def Intersection_of_Two_List(list1, lits2):
    return list(set(list1) & set(lits2))
print(Intersection_of_Two_List(eval(input()), eval(input())))