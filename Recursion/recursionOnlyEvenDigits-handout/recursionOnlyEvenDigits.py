def readList():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def recursionOnlyEvenDigits(l):
	return remove_odd(l,0)

def remove_odd(l,i):
    if (i>=len(l)):
        return l 
    l[i]=remove_odd_num(l[i],0,0)
    return remove_odd(l,i+1)

def remove_odd_num(n,res,p):
    if n<=0:
        return res
    r =n%10
    if(r%2==0):
        return remove_odd_num(n//10,res+(r*(10**p)),p+1)
    else:
        return remove_odd_num(n//10,res,p)

print(recursionOnlyEvenDigits(readList()))