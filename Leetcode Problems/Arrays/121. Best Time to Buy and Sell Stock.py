def solution(prices):
    buy_price = float("inf")
    profit = 0
    for price in prices:
        if price < buy_price:
            buy_price = price
        profit = max(profit, price - buy_price)
    return profit
