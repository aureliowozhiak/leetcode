# Maximum Subarray (Kadane)

## 📋 Problema

Dado um array de inteiros, encontre a soma máxima possível de um subarray contíguo.

---

## 🎯 Objetivo

Apresentar a versão simples (força bruta) e a versão ótima (Kadane), com foco em clareza para entrevistas.

---

## 💪 Solução 1: Força Bruta (O(n²))

### Código

```python
def max_subarray_bruteforce(nums):
    best = float('-inf')
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > best:
                best = current_sum
    return best
```

### Como funciona

1. Fixa um início `i` e expande o fim `j` somando incrementos  
2. Mantém o melhor valor encontrado

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| Tempo | `O(n²)` | Para cada `i`, percorre `j` até o fim |
| Espaço | `O(1)` | Usa apenas acumuladores |

---

## 🚀 Solução 2: Kadane (O(n)) — RECOMENDADA

### Código

```python
def max_subarray(nums):
    best = nums[0]
    current = nums[0]
    for value in nums[1:]:
        current = max(value, current + value)
        if current > best:
            best = current
    return best
```

### Como funciona

1. `current` representa a melhor soma que termina no índice atual  
2. Se for melhor recomeçar em `value`, reinicia; caso contrário, estende  
3. `best` guarda a melhor soma global

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| Tempo | `O(n)` | Um único passe |
| Espaço | `O(1)` | Constante |

### Observações

- Arrays com todos negativos: inicialize com `nums[0]` (evita zerar incorretamente)

---

## 📊 Comparação

| Método | Tempo | Espaço | Quando usar |
|--------|-------|--------|-------------|
| Força Bruta | `O(n²)` | `O(1)` | Didático, validação |
| Kadane | `O(n)` | `O(1)` | Entrevistas/produção |

---

## 🧪 Testes

```python
assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert max_subarray([1]) == 1
assert max_subarray([5,4,-1,7,8]) == 23
```

---

## 💡 Pontos-Chave para Memorizar

1. Relação de transição: `current = max(value, current + value)`  
2. `best` armazena a resposta global  
3. Um passe, `O(1)` espaço — excelente para entrevistas
