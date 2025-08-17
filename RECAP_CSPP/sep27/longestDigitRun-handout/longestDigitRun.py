def LongestDigitRun(x):
    x=abs(x)
    cur_num=0
    cur_count=0
    max_num=0
    max_count=0
    if x==0:
        return 0
    while(x>0):
        if cur_num!=(x%10):
            cur_num=x%10
            cur_count=1
        else:
            cur_count=cur_count+1
        x=x//10
        if(cur_count>max_count)or(cur_count==max_count and cur_num<max_num):
            max_num=cur_num
            max_count=cur_count
    return max_num
print(LongestDigitRun(int(input())))