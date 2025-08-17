def split_by_vowels(s):

    vowels="aeiouAEIOU"
    l=[]
    r=''

    for i in s: 
        if i in vowels:
           l.append(i)
           r=''
        else:
          r=r+i
          if(len(r)>1):
             l.pop()
          l.append(r)
          
    return l

print(split_by_vowels(input()))