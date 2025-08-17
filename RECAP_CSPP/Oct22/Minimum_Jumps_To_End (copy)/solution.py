def min_jumps(nums):
    def backtrack(index):
        if index >= len(nums) - 1:
            return 0
        
        if index in memo:
            return memo[index]

        max_jump = nums[index]
        min_steps = float('inf')

        for step in range(1, max_jump + 1):
            next_index = index + step
            if next_index < len(nums):
                jumps = backtrack(next_index)
                if jumps != float('inf'):
                    min_steps = min(min_steps, jumps + 1)

        memo[index] = min_steps
        return min_steps

    if not nums or len(nums) == 0:
        return 0

    memo = {}
    result = backtrack(0)
    return result if result != float('inf') else -1


print(min_jumps(eval(input())))