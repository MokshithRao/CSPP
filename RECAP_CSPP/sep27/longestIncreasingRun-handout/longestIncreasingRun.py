def longestIncreasingRun(n):
    n = abs(n)

    max_run = 0
    max_run_value = 0

    current_run = 1 
    current_run_value = n % 10 
    
    prev_digit = n % 10 
    n //= 10
 
    while n > 0:
        current_digit = n % 10 
        n //= 10 
        
        if current_digit < prev_digit:
            current_run_value = current_digit * (10 ** current_run) + current_run_value 
            current_run += 1
        else:
            if current_run > max_run or (current_run == max_run and current_run_value > max_run_value): 
                max_run = current_run
                max_run_value = current_run_value
            current_run = 1
            current_run_value = current_digit

        prev_digit = current_digit

    if current_run > max_run or (current_run == max_run and current_run_value > max_run_value):
        max_run_value = current_run_value

    return max_run_value


print(longestIncreasingRun(int(input())))