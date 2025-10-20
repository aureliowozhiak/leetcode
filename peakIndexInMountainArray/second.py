# Solução O(log n) - Busca Binária
def peakIndexInMountainArray(arr):
    """
    Encontra o índice do pico em um array montanhoso usando busca binária.
    Complexidade: O(log n) tempo, O(1) espaço
    
    Array montanhoso: cresce até um pico, depois decresce
    Exemplo: [0,1,3,1,0] -> pico no índice 2 (valor 3)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Se o elemento atual é menor que o próximo,
        # o pico está à direita
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        # Senão, o pico está à esquerda (incluindo mid)
        else:
            right = mid
    
    return left

# Teste
test_cases = [
    [0, 1, 3, 1, 0],           # pico no índice 2
    [0, 2, 1, 0],              # pico no índice 1
    [1, 3, 5, 4, 2],          # pico no índice 2
    [0, 10, 5, 2],            # pico no índice 1
    [1, 2, 3, 4, 1],          # pico no índice 3
]

print("=== Solução O(log n) - Busca Binária ===")
for i, test in enumerate(test_cases):
    result = peakIndexInMountainArray(test)
    print(f"Teste {i+1}: {test} -> Pico no índice {result} (valor {test[result]})")

# Análise de complexidade
print("\n=== Análise de Complexidade ===")
print("Tempo: O(log n) - Divide o espaço de busca pela metade a cada iteração")
print("Espaço: O(1) - Usa apenas variáveis constantes")
print("\nVantagens:")
print("- Muito mais eficiente para arrays grandes")
print("- Tempo de execução cresce muito devagar")
print("\nExemplo:")
print("Array com 1000 elementos: ~10 comparações")
print("Array com 1,000,000 elementos: ~20 comparações")
