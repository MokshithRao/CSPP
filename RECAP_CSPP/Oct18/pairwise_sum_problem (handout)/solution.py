def pairwise_sum(numbers):
    
    list = []
    for i in range(len(numbers)-1):
        sum = 0
        sum += numbers[i] + numbers[i+1]
        list.append(sum)
    return list
    

if __name__ == "__main__":
    # Read input from the command prompt
    input_string = input()
    
    try:
        numbers = eval(input_string)
        
        # Call the pairwise_sum function and print the result
        result = pairwise_sum(numbers)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")
