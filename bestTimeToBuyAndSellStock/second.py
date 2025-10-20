def max_profit(prices):
    """Uma varredura: mantém menor preço e melhor lucro. O(n) tempo, O(1) espaço."""
    min_price = float('inf')
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > best:
            best = profit
    return best


if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))  # 5
    print(max_profit([7,6,4,3,1]))    # 0

