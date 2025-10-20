def max_profit_bruteforce(prices):
    """Maior lucro comprando e vendendo uma vez. Força bruta O(n^2)."""
    n = len(prices)
    best = 0
    for buy in range(n):
        for sell in range(buy + 1, n):
            profit = prices[sell] - prices[buy]
            if profit > best:
                best = profit
    return best


if __name__ == "__main__":
    print(max_profit_bruteforce([7,1,5,3,6,4]))  # 5
    print(max_profit_bruteforce([7,6,4,3,1]))    # 0

