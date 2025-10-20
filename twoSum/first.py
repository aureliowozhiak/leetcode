def two_sum_bruteforce(nums, target):
    """Retorna os índices i, j tais que nums[i] + nums[j] == target (i < j).

    Abordagem força bruta: testa todos os pares. O(n^2).
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    # Casos básicos
    print(two_sum_bruteforce([2,7,11,15], 9))      # [0,1]
    print(two_sum_bruteforce([3,2,4], 6))          # [1,2]
    print(two_sum_bruteforce([3,3], 6))            # [0,1]

