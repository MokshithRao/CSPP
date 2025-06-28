def convert_uppercase(str):
    s = ""
    count = 0
    for char in str:
        if char.islower():
            s += char.upper()
            count+=1
        else:
            s += char
    return s, count
    
print(convert_uppercase(input()))
