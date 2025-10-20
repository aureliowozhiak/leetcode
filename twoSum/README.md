# Two Sum

## 📋 Problema

Dado um array de inteiros `nums` e um inteiro `target`, retorne os índices de dois números que somam `target`. Há exatamente uma solução e você não pode usar o mesmo elemento duas vezes.

---

## 🎯 Objetivo

Implementar uma solução correta e eficiente, explicando claramente a evolução de força bruta para uma abordagem ótima com hash map.

---

## 💪 Solução 1: Força Bruta (O(n²))

### Código

```python
def two_sum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

### Como funciona

1. Percorre todos os pares `(i, j)` com `i < j`
2. Retorna o primeiro par cuja soma é `target`

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| Tempo | `O(n²)` | Compara todos os pares |
| Espaço | `O(1)` | Apenas variáveis auxiliares |

### Prós e Contras

✅ Simples de implementar e explicar  
❌ Lento para arrays grandes

---

## 🚀 Solução 2: Hash Map (O(n)) — RECOMENDADA

### Código

```python
def two_sum(nums, target):
    value_to_index = {}
    for j, value in enumerate(nums):
        need = target - value
        if need in value_to_index:
            return [value_to_index[need], j]
        value_to_index[value] = j
    return []
```

### Como funciona

1. Para cada valor `value`, calcula `need = target - value`
2. Se `need` já foi visto, retorna os índices  
3. Caso contrário, registra `value → índice` no dicionário

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| Tempo | `O(n)` | Cada elemento é processado uma vez |
| Espaço | `O(n)` | Dicionário armazena valores já vistos |

### Prós e Contras

✅ Muito eficiente em tempo  
❌ Usa memória adicional para o dicionário

---

## 📊 Comparação

| Método | Tempo | Espaço | Quando usar |
|--------|-------|--------|-------------|
| Força Bruta | `O(n²)` | `O(1)` | Rascunho rápido, validação inicial |
| Hash Map | `O(n)` | `O(n)` | Entrevistas/produção |

---

## 🎓 Entendendo Big O

- Força Bruta cresce quadraticamente: pares de elementos  
- Hash Map cresce linearmente: um passe + consultas `O(1)` médias

---

## 🏆 Recomendações para Entrevistas

1. Explique a força bruta primeiro (garante correção)  
2. Evolua para hash map e destaque a troca tempo × espaço  
3. Atenção: retorne índices, não valores. Procure antes de inserir para evitar reutilizar o mesmo elemento

---

## 🧪 Testes

```python
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([3,2,4], 6) in ([1,2],[2,1])
assert two_sum([3,3], 6) == [0,1]
```

---

## 💡 Pontos-Chave para Memorizar

1. Padrão clássico: "complemento + hash map"  
2. Procure o complemento antes de inserir o valor atual  
3. Dicionário valor→índice mais recente é suficiente
