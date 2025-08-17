# def is_anagram(s1, s2):
#     s1 = s1.lower()
#     s2 = s2.lower()
#     l = []

#     for i in s1:
#         a = s1[1:] + s1[0]
#         l.append(a)
#         s1 = a
#     print(l)
#     if s2 in l:
#         return True
#     return False



# print(is_anagram(input(), input()))


def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

print(is_anagram(input(), input()))