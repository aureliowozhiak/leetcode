# 🚀 LeetCode - Problemas Clássicos de Array

Este repositório contém **4 problemas clássicos de array numérico** essenciais para entrevistas técnicas e competições de programação. Cada problema inclui múltiplas soluções, análise de complexidade e dicas práticas.

---

## 📚 Problemas Incluídos

### 1. 🔍 [Two Sum](./twoSum/)
**Problema**: Encontrar dois números que somam um valor alvo  
**Dificuldade**: Fácil  
**Padrão**: Hash Map + Complemento

- ✅ Força bruta O(n²) 
- ✅ Hash map O(n) - **Recomendada**
- 🎯 **Foco**: Primeiro problema clássico, base para muitos outros

### 2. 📈 [Maximum Subarray (Kadane)](./maximumSubarray/)
**Problema**: Maior soma de subarray contíguo  
**Dificuldade**: Médio  
**Padrão**: Programação Dinâmica + Kadane

- ✅ Força bruta O(n²)
- ✅ Algoritmo de Kadane O(n) - **Recomendada**
- 🎯 **Foco**: DP 1D, otimização de subproblemas

### 3. 💰 [Best Time to Buy and Sell Stock](./bestTimeToBuyAndSellStock/)
**Problema**: Maior lucro com uma transação de compra/venda  
**Dificuldade**: Fácil  
**Padrão**: Varredura Linear + Invariante

- ✅ Força bruta O(n²)
- ✅ Um passe O(n) - **Recomendada**
- 🎯 **Foco**: Invariantes, otimização de busca

### 4. 🏔️ [Peak Index in Mountain Array](./peakIndexInMountainArray/)
**Problema**: Encontrar índice do pico em array montanhoso  
**Dificuldade**: Médio  
**Padrão**: Busca Binária + Propriedade Especial

- ✅ Força bruta O(n)
- ✅ Busca binária O(log n) - **Recomendada**
- 🎯 **Foco**: Busca binária, propriedades especiais

---

## 🎯 O Que Você Vai Encontrar

### 📁 Estrutura de Cada Problema

```
problema/
├── first.py      # Solução força bruta (didática)
├── second.py     # Solução otimizada (entrevista)
└── README.md     # Documentação completa
```

### 📖 Conteúdo dos READMEs

Cada README inclui:

- 📋 **Problema**: Enunciado claro e exemplos
- 🎯 **Objetivo**: O que aprender
- 💪 **Solução 1**: Força bruta com análise
- 🚀 **Solução 2**: Versão otimizada recomendada
- 📊 **Comparação**: Tabela de complexidades
- 🎓 **Big O**: Explicação didática
- 🏆 **Entrevistas**: Dicas práticas
- 🧪 **Testes**: Casos de teste prontos
- 💡 **Memorização**: Pontos-chave essenciais

---

## 🚀 Como Usar Este Repositório

### 1. **Para Estudar**
```bash
# Navegue para qualquer problema
cd twoSum

# Leia o README.md
# Execute as soluções
python first.py   # Força bruta
python second.py  # Otimizada
```

### 2. **Para Entrevistas**
- Comece sempre pela **força bruta**
- Explique a **complexidade** em voz alta
- Evolua para a **solução otimizada**
- Use os **pontos-chave** para memorizar

### 3. **Para Competições**
- Foque nas **soluções otimizadas**
- Pratique a **implementação rápida**
- Estude os **padrões** de cada problema

---

## 📊 Padrões de Algoritmos Cobertos

| Padrão | Problemas | Complexidade Típica |
|--------|-----------|-------------------|
| **Hash Map** | Two Sum | O(n) tempo, O(n) espaço |
| **Programação Dinâmica** | Maximum Subarray | O(n) tempo, O(1) espaço |
| **Varredura Linear** | Buy/Sell Stock | O(n) tempo, O(1) espaço |
| **Busca Binária** | Peak Index | O(log n) tempo, O(1) espaço |

---

## 🎓 Por Que Esses Problemas?

### ✅ **Essenciais para Entrevistas**
- Aparecem frequentemente em FAANG
- Testam conceitos fundamentais
- Base para problemas mais complexos

### ✅ **Cobertura Completa**
- **Fácil**: Two Sum, Buy/Sell Stock
- **Médio**: Maximum Subarray, Peak Index
- **Padrões**: Hash, DP, Linear, Binary Search

### ✅ **Progression Natural**
1. **Two Sum** → Introdução a hash maps
2. **Buy/Sell Stock** → Varredura linear
3. **Maximum Subarray** → Programação dinâmica
4. **Peak Index** → Busca binária

---

## 🏆 Dicas para Sucesso

### 📚 **Estude Sistematicamente**
1. Leia o problema e entenda completamente
2. Implemente a força bruta primeiro
3. Analise a complexidade
4. Otimize para a solução recomendada
5. Pratique explicar em voz alta

### 🎯 **Foque na Clareza**
- Código limpo e legível
- Comentários explicativos
- Nomes de variáveis descritivos
- Estrutura lógica clara

### ⚡ **Pratique Regularmente**
- Implemente cada solução do zero
- Cronometre seu tempo
- Explique para outras pessoas
- Revise os pontos-chave

---

## 🔗 Próximos Passos

Após dominar estes 4 problemas:

1. **Problemas Similares**: 3Sum, Container With Most Water, Product of Array Except Self
2. **Padrões Avançados**: Sliding Window, Two Pointers, Prefix Sums
3. **Estruturas de Dados**: Heaps, Trees, Graphs
4. **Algoritmos Avançados**: Backtracking, Greedy, Graph Algorithms

---

## 📝 Contribuições

Sinta-se à vontade para:
- Adicionar novos problemas clássicos
- Melhorar as explicações existentes
- Corrigir bugs ou melhorar código
- Sugerir novos casos de teste

---

**Boa sorte nas suas entrevistas! 🚀**

*Lembre-se: a prática leva à perfeição. Implemente, explique, repita!*
