a_smile=str(input())=="True"
b_smile=str(input())=="True"
def Monkey():
    if (a_smile==True and b_smile==True) or (not(a_smile) and not(b_smile)):
        return True
    else:
        return False
print(Monkey())
