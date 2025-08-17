def count_vowels(s):
    s = s.split()
    count = 0
    for i in s:
        if i[0] in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels(input()))