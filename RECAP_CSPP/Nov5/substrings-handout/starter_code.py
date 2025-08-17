s = input()
s = s.replace("s =",'')
s = s.lstrip()
s = s.strip("'")



def find_all_substrings(s):
    # Write your code here
    l = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            a = s[i:j+1]
            l.append(a)
        
    return l

        
print(find_all_substrings(s))

