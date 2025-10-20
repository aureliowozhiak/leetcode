def max_subarray(nums):
    """Kadane: O(n) tempo, O(1) espaço."""
    best = nums[0]
    current = nums[0]
    for value in nums[1:]:
        current = max(value, current + value)
        if current > best:
            best = current
    return best


if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(max_subarray([1]))                      # 1
    print(max_subarray([5,4,-1,7,8]))             # 23

