def semi_palindrome(s):
    a = len(s)//2
    b = s[:a]
    c = s[a:]
    str = ""
    if len(s)==1:
        return True
    for i in c:
        str = i + str
    return b == str

print(semi_palindrome(input()))