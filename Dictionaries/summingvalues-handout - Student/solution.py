
# def sum_values(dictionary):
#     #start your code here
#     sum=0
#     for key in dictionary:
#         sum +=dictionary[key]
#     return sum 
#     pass

# def display_sum(dictionary):
#     #start your code here
#     print("Sum:", sum_values(dictionary))

#     pass

# def read_input():
    
#     input_str = input().strip()
    
#     if input_str == 'values = {}':
#         return {}
#     input_str = input_str.strip('{}')
#     pairs = input_str.split(', ')
#     dictionary = {}
#     for pair in pairs:
        
#         key, value = pair.split(': ')
#         key = key.strip('"')
#         value = int(value.strip('"'))
#         dictionary[key] = value
    
#     return dictionary


# dictionary = read_input()

# display_sum(dictionary)


my_dict = {"apple": 2, "banana": 3}
print(my_dict["apple"])