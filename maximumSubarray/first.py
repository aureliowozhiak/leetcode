def max_subarray_bruteforce(nums):
    """Soma máxima de subarray contínuo por força bruta. O(n^2)."""
    best = float('-inf')
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > best:
                best = current_sum
    return best


if __name__ == "__main__":
    print(max_subarray_bruteforce([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(max_subarray_bruteforce([1]))                      # 1
    print(max_subarray_bruteforce([5,4,-1,7,8]))             # 23

