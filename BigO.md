## Big O – explicação simples

- **O que é**: Big O descreve como o tempo (ou memória) de um algoritmo cresce conforme o tamanho da entrada n aumenta. É uma medida assintótica: ignora constantes e foca no comportamento quando n fica grande.
- **Para que serve**: comparar algoritmos, prever escalabilidade e escolher soluções mais eficientes.
- **Como identificar**: conte quantas vezes o trabalho cresce quando você aumenta n. Loops, loops aninhados e divisões da entrada são as principais pistas.

---

### Gráfico comparativo

O gráfico abaixo ilustra qualitativamente o crescimento de cada complexidade.

![Gráfico Big O](assets/big-o.png)

---

### O(1) – tempo constante (mais performático)
- **Ideia**: o trabalho não aumenta com n. Sempre faz a mesma quantidade fixa de operações.
- **Como identificar**: acesso direto por índice, operações com tamanho fixo, atribuições simples.

```python
# Exemplo: acessar o primeiro elemento (constante)
nums = [10, 20, 30, 40]
primeiro = nums[0]  # O(1)

# Exemplo: inserir/remover no fim de list como pilha (amortizado O(1))
nums.append(50)     # O(1) amortizado
nums.pop()          # O(1)
```

---

### O(log n) – tempo logarítmico
- **Ideia**: a cada passo, você reduz o problema por um fator (ex.: metade). Típico de busca binária, árvores balanceadas, dividir-para-conquistar sem percorrer tudo.
- **Como identificar**: enquanto divide por 2 (ou por fator constante), ou usa busca binária/árvores balanceadas.

```python
# Exemplo: busca binária em lista ORDENADA
# Retorna índice de alvo ou -1

def busca_binaria(nums, alvo):
    esquerda, direita = 0, len(nums) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if nums[meio] == alvo:
            return meio
        if nums[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1  # O(log n)
```

---

### O(n) – tempo linear
- **Ideia**: o trabalho cresce proporcionalmente a n. Percorre toda a lista uma vez.
- **Como identificar**: um único loop simples sobre a entrada; nenhuma repetição aninhada proporcional a n.

```python
# Exemplo: encontrar o maior elemento

def maximo(nums):
    maior = float('-inf')
    for x in nums:   # passa uma vez por cada elemento
        if x > maior:
            maior = x
    return maior  # O(n)
```

---

### O(n log n) – tempo quase-linear
- **Ideia**: divide e conquista com trabalho linear por nível; típico de ordenações eficientes (merge sort, heap sort) e certas estruturas.
- **Como identificar**: divide em subproblemas (geralmente em 2), resolve recursivamente e combina em O(n).
 - **Diferença para O(log n)**: em O(log n) você reduz por fator sem varrer toda a entrada; em O(n log n) existem ~log n níveis e em cada nível processa-se O(n) elementos (ex.: ordenar toda a lista a cada nível de divisão).

```python
# Exemplo: merge sort (ordenação estável O(n log n))

def merge(a, b):
    i = j = 0
    r = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            r.append(a[i]); i += 1
        else:
            r.append(b[j]); j += 1
    r.extend(a[i:]); r.extend(b[j:])
    return r

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    esquerda = merge_sort(nums[:m])
    direita  = merge_sort(nums[m:])
    return merge(esquerda, direita)  # O(n log n)
```

---

### O(2^n) – tempo exponencial
- **Ideia**: cada passo duplica o número de possibilidades (decisão binária por elemento). Ex.: gerar subconjuntos.
- **Como identificar**: recursão que faz duas chamadas por nível (incluir/excluir), percorrendo todas as combinações.

```python
# Exemplo: todos os subconjuntos (power set)

def subconjuntos(nums):
    res = []
    atual = []

    def backtrack(i):
        if i == len(nums):
            res.append(atual.copy())
            return
        # escolher não incluir nums[i]
        backtrack(i + 1)
        # escolher incluir nums[i]
        atual.append(nums[i])
        backtrack(i + 1)
        atual.pop()

    backtrack(0)
    return res  # O(2**n)
```

---

### O(n!) – tempo fatorial (muito custoso)
- **Ideia**: explora todas as permutações possíveis dos n elementos.
- **Como identificar**: backtracking que fixa posições e permuta o restante; número de estados cresce como n!.
 - **Backtracking na prática**: modela-se o problema como uma árvore de decisões em que cada nível fixa uma escolha (ex.: qual elemento vai na próxima posição). Sem podas, todas as permutações são geradas, resultando em n! estados. Podas (restrições/heurísticas) podem reduzir casos, mas o pior caso permanece fatorial.

```python
# Exemplo: gerar todas as permutações

def permutacoes(nums):
    res = []
    usado = [False] * len(nums)
    atual = []

    def backtrack():
        if len(atual) == len(nums):
            res.append(atual.copy())
            return
        for i in range(len(nums)):
            if usado[i]:
                continue
            usado[i] = True
            atual.append(nums[i])
            backtrack()
            atual.pop()
            usado[i] = False

    backtrack()
    return res  # O(n!)
```

---

### O(n²) – tempo quadrático (pior entre os listados)
- **Ideia**: para cada elemento, percorre todos os outros; loops aninhados dependentes de n.
- **Como identificar**: dois loops aninhados que vão até n (ou operações de comparação de todos com todos).

```python
# Exemplo: checar se há pares duplicados por comparação ingênua

def tem_duplicado_ingenuo(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False  # O(n**2)
```

---

## Dicas rápidas para identificar Big O
- **Constante O(1)**: operações com quantidade fixa de passos (acesso por índice, swap de duas variáveis).
- **Logarítmica O(log n)**: reduz pela metade (ou fator) repetidamente; busca binária.
- **Linear O(n)**: um único passeio completo pela entrada.
- **Quadrática O(n²)**: dois loops aninhados sobre n; compara todos com todos.

Observação: existem outras classes (por exemplo O(n log n), O(2^n), O(n!) etc.). Aqui listamos das mais eficientes para piores entre as mais comuns do dia a dia.

