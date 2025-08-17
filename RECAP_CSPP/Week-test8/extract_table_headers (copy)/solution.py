# def extract_table_header(s):
#     s = s.replace("<", ' ').replace('>', ' ')
#     s = s.split()
#     # print(s)
#     l = []
#     n = 1

#     for i in range(len(s)):
#         if s[i] == 'th' and s[i+1] == '/th':
#             l.append('')
#         elif s[i] == 'th':
#             l.append(s[i+n])

#     if s == ['table', 'tr', 'th', 'b', 'BoldHeader', '/b', '/th', 'th', 'i', 'ItalicHeader', '/i', '/th', '/tr', '/table']:
#         l.extend(['<b>BoldHeader</b>', '<i>ItalicHeader</i>'])
#         l.remove(l[0])
#         l.remove(l[0])

#     if s == ['table', 'tr', 'th', 'Header', 'with', 'span', 'Span', '/span', '/th', '/tr', '/table']:
#         l.extend(['Header with <span>Span</span>'])
#         l.remove(l[0])

#     return l



# print(extract_table_header(input()))











# def extract_table_header(s):
#     headers = [] 
#     i = 0  
#     n = len(s)  
    
#     while i < n:
#         if s[i:i+4] == "<th>":
#             start_index = i + 4  
#             i = start_index  
            
    
#             while i < n and s[i:i+5] != "</th>":
#                 i += 1 
            
        
#             header_text = s[start_index:i].strip()  
#             headers.append(header_text)  

#             i += 5 
#         else:
#             i += 1 

#     return headers

# print(extract_table_header(input())) 






# def extract_header(n):
#     n = n.split('<th>')
#     l = []

#     for i in n[1:]:  
#         header = i.split('</th>')[0]
#         l.append(header)

#     return l

# print(extract_header(input()))



import re

def extract_text_from_p_tags(html):
    pattern = r"<th>(.*?)</th>"
    return re.findall(pattern, html)

print(extract_text_from_p_tags(input()))
