def two_sum(nums, target):
    """Retorna os índices i, j tais que nums[i] + nums[j] == target usando hash.

    Abordagem otimizada: dicionário para guardar valor->índice. O(n) tempo, O(n) espaço.
    """
    value_to_index = {}
    for j, value in enumerate(nums):
        need = target - value
        if need in value_to_index:
            return [value_to_index[need], j]
        value_to_index[value] = j
    return []


if __name__ == "__main__":
    print(two_sum([2,7,11,15], 9))      # [0,1]
    print(two_sum([3,2,4], 6))          # [1,2]
    print(two_sum([3,3], 6))            # [0,1]

