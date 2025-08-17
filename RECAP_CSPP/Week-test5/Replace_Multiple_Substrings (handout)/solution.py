# def replace_substring(s, m):
#     s = s.split(" ")
#     # print(s)
#     s1 = ""
#     # print(len(s), len(m))
#     for i in range(len(s)):
#         for j in range(len(m)):
#             if s[i] == m[i][j]:
#                 s1 += m[j][i+1]
#             else:
#                 s1 += s[i]
#     return s1



# print(replace_substring(input(), eval(input())))



def replace_sub(string, matrix):
    string1 = string.split(" ")

    if not string1:
        return []
    
    for i in matrix:
        for j in range(len(string1)):
            if i[0] == string1[j]:
                string1[j] = i[1]
    return ' '.join(string1)


string = input()
matrix = eval(input())
print(replace_sub(string, matrix))