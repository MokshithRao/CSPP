def total_hamming_distance(nums):
    if not nums:
        return 0
    n = len(nums)
    t_d = 0
    maxbit = max(nums).bit_length()
    for bit in range(maxbit):
        count1 = 0
        for i in nums:
            if i & (1 << bit):
                count1 += 1
        count0 = n - count1
        t_d += count1 * count0
    return t_d

if __name__ == "__main__":
    # Read input from the command prompt
    input_string = input()
    nums = list(map(int, input_string.split()))
    
    try:
        # Call the total_hamming_distance function and print the result
        result = total_hamming_distance(nums)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

