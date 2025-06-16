


def createAddressBook(address_list):
    #start your code here
    address_book={}
    for name,phone in address_list:
        address_book[name]=phone
    return address_book



def displayAddressBook(address_book):
    #start your code here
    for name,phone in address_book.items():
        print(f"{name}: {phone}")






def readInput():

    input_str = input().strip()
    
    if input_str == '[]':
        return []
    
    input_str = input_str.strip('[]')  
    pairs = input_str.split('), (')
    
    address_list = []
    for pair in pairs:
        pair = pair.strip('()')
        name, phone = pair.split(', ')
        name = name.strip('"')
        phone = phone.strip('"')
        
        address_list.append((name, phone))
    
    return address_list


address_list = readInput()

address_book = createAddressBook(address_list)

displayAddressBook(address_book)
