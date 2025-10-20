# Peak Index in Mountain Array

## 📋 Problema

Dado um array montanhoso (mountain array), encontre o índice do elemento pico.

**Array montanhoso**: Um array que:
- Cresce até um pico
- Depois decresce
- Garantido ter exatamente um pico

**Exemplo**: `[0,1,3,1,0]` → Pico no índice 2 (valor 3)

## 🎯 Objetivo

Implementar uma solução eficiente para encontrar o índice do pico em um array montanhoso.

---

## 💪 Solução 1: Força Bruta (O(n))

### Código

```python
def peakIndexInMountainArray(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            return i
```

### Como funciona

1. **Percorre o array** do início ao fim
2. **Compara** cada elemento com o próximo
3. **Retorna** o índice quando encontra o pico

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| **Tempo** | `O(n)` | No pior caso, percorre todo o array |
| **Espaço** | `O(1)` | Usa apenas variáveis constantes |

### Vantagens e Desvantagens

✅ **Vantagens:**
- Código simples e fácil de entender
- Funciona para qualquer tamanho de array
- Fácil de debugar

❌ **Desvantagens:**
- Ineficiente para arrays grandes
- Não aproveita a propriedade montanhosa do array

---

## 🚀 Solução 2: Busca Binária (O(log n)) - **RECOMENDADA**

### Código

```python
def peakIndexInMountainArray(arr):
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
```

### Como funciona

1. **Define** os limites inicial (`left = 0`, `right = len(arr)-1`)
2. **Calcula** o meio do intervalo atual
3. **Compara** o elemento do meio com o próximo:
   - Se `arr[mid] < arr[mid+1]`: pico está à direita → `left = mid + 1`
   - Se `arr[mid] >= arr[mid+1]`: pico está à esquerda → `right = mid`
4. **Repete** até `left == right`
5. **Retorna** o índice encontrado

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| **Tempo** | `O(log n)` | Divide o espaço de busca pela metade a cada iteração |
| **Espaço** | `O(1)` | Usa apenas variáveis constantes |

### Vantagens e Desvantagens

✅ **Vantagens:**
- **Muito eficiente** para arrays grandes
- Aproveita a propriedade montanhosa
- **Tempo cresce muito devagar**

❌ **Desvantagens:**
- Lógica um pouco mais complexa
- Requer entendimento de busca binária

---

## 📊 Comparação de Performance

### Exemplo Prático

| Tamanho do Array | Força Bruta (O(n)) | Busca Binária (O(log n)) |
|------------------|-------------------|--------------------------|
| 10 elementos     | ~10 comparações   | ~3 comparações           |
| 100 elementos    | ~100 comparações  | ~7 comparações           |
| 1,000 elementos  | ~1,000 comparações| ~10 comparações          |
| 1,000,000 elementos | ~1,000,000 comparações | ~20 comparações |

### Visualização

```
Array: [0, 1, 2, 3, 4, 3, 2, 1, 0]
        ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑
        0  1  2  3  4  5  6  7  8

Força Bruta: 0→1→2→3→4→5 (6 comparações)
Busca Binária: 4→2→3→4 (4 comparações)
```

---

## 🎓 Entendendo Big O

### O que é Big O?

**Big O** é uma notação matemática que descreve como o tempo de execução ou espaço de memória de um algoritmo cresce conforme o tamanho da entrada aumenta.

### Tipos de Complexidade

| Complexidade | Nome | Exemplo | Tempo para 1000 elementos |
|--------------|------|---------|---------------------------|
| `O(1)` | Constante | Acesso a array | 1 operação |
| `O(log n)` | Logarítmica | Busca binária | ~10 operações |
| `O(n)` | Linear | Busca linear | ~1000 operações |
| `O(n²)` | Quadrática | Bubble sort | ~1,000,000 operações |

### Por que O(log n) é melhor que O(n)?

```
n = 1,000
O(n): 1,000 operações
O(log n): log₂(1,000) ≈ 10 operações

n = 1,000,000  
O(n): 1,000,000 operações
O(log n): log₂(1,000,000) ≈ 20 operações
```

**Conclusão**: O(log n) é **100x mais rápido** para arrays grandes!

---

## 🏆 Recomendações para Entrevistas

### Para Entrevistas Técnicas

1. **Comece com força bruta** (O(n))
   - Mostra que você entende o problema
   - Código simples e correto

2. **Identifique a otimização**
   - "Posso usar busca binária?"
   - "O array tem propriedade especial?"

3. **Implemente a solução otimizada** (O(log n))
   - Explique o raciocínio
   - Demonstre conhecimento de Big O

### Resposta Ideal

> "Vou começar com uma solução O(n) que percorre o array até encontrar o pico. Depois posso otimizar para O(log n) usando busca binária, já que o array é montanhoso e posso eliminar metade das possibilidades a cada comparação."

---

## 🧪 Testes

### Casos de Teste

```python
test_cases = [
    [0, 1, 3, 1, 0],     # Pico no índice 2
    [0, 2, 1, 0],        # Pico no índice 1  
    [1, 3, 5, 4, 2],     # Pico no índice 2
    [0, 10, 5, 2],       # Pico no índice 1
    [1, 2, 3, 4, 1],     # Pico no índice 3
]
```

### Executando os Testes

```bash
# Testar força bruta
python first.py

# Testar busca binária  
python second.py
```

---

## 💡 Pontos-Chave para Memorizar

1. **Array montanhoso** = cresce até pico, depois decresce
2. **Força bruta** = O(n), simples mas ineficiente
3. **Busca binária** = O(log n), eficiente e recomendada
4. **Big O** = como o algoritmo escala com o tamanho da entrada
5. **Para entrevistas** = sempre mencione complexidade e otimizações

---

## 🔗 Próximos Passos

- Pratique implementar busca binária
- Estude outros problemas de busca binária
- Entenda quando usar cada tipo de busca
- Pratique explicar Big O em voz alta

**Boa sorte nas entrevistas! 🚀**
