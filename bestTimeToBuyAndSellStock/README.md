# Best Time to Buy and Sell Stock

## 📋 Problema

Dado um array `prices`, onde `prices[i]` é o preço da ação no dia `i`, encontre o lucro máximo com uma única transação: comprar uma vez e vender uma vez. Se não houver lucro, retorne `0`.

---

## 🎯 Objetivo

Comparar o método ingênuo com a solução ótima em um passe, com foco em explicar a intuição para entrevistas.

---

## 💪 Solução 1: Força Bruta (O(n²))

### Código

```python
def max_profit_bruteforce(prices):
    n = len(prices)
    best = 0
    for buy in range(n):
        for sell in range(buy + 1, n):
            profit = prices[sell] - prices[buy]
            if profit > best:
                best = profit
    return best
```

### Como funciona

1. Testa todos os pares `(buy, sell)` com `buy < sell`  
2. Atualiza o melhor lucro observado

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| Tempo | `O(n²)` | Todos os pares possíveis |
| Espaço | `O(1)` | Apenas variáveis auxiliares |

---

## 🚀 Solução 2: Um Passe (O(n)) — RECOMENDADA

### Código

```python
def max_profit(prices):
    min_price = float('inf')
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > best:
            best = profit
    return best
```

### Como funciona

1. Mantém `min_price` (menor preço visto até agora)  
2. Calcula o lucro se vendesse hoje: `price - min_price`  
3. Atualiza o melhor lucro global

### Análise de Complexidade

| Aspecto | Valor | Explicação |
|---------|-------|------------|
| Tempo | `O(n)` | Um único passe pelo array |
| Espaço | `O(1)` | Constante |

### Observações

- Garante a ordem (não vende antes de comprar) pois `min_price` vem de dias anteriores

---

## 📊 Comparação

| Método | Tempo | Espaço | Quando usar |
|--------|-------|--------|-------------|
| Força Bruta | `O(n²)` | `O(1)` | Didático, validação |
| Um Passe | `O(n)` | `O(1)` | Entrevistas/produção |

---

## 🧪 Testes

```python
assert max_profit([7,1,5,3,6,4]) == 5
assert max_profit([7,6,4,3,1]) == 0
```

---

## 💡 Pontos-Chave para Memorizar

1. Invariante: `min_price` é o menor preço visto até o dia atual  
2. Lucro do dia = `price - min_price`  
3. Atualize a resposta global com `max`
